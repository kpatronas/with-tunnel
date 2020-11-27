#!/usr/bin/env python3
import os
import sys
import signal
import getpass
import argparse
import sshtunnel

def signal_handler(sig, frame):
    server.stop()
    sys.exit(0)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Create ssh tunnels!")

    parser.add_argument('--proxy_host',
                        action   = 'store',
                        type     = str,
                        help     = "Proxy IP Address / Hostname",
                        required = True)

    parser.add_argument('--proxy_port',
                        action   = 'store',
                        type     = int,
                        help     = "Proxy Port",
                        required = False,
                        default  = 22)

    parser.add_argument('--proxy_user',
                        action   = 'store',
                        type     = str,
                        help     = "Proxy Username",
                        required = False)

    parser.add_argument('--proxy_pass',
                        action   = 'store',
                        type     = str,
                        help     = "Proxy Password",
                        required = False)

    parser.add_argument('--proxy_key',
                        action   = 'store',
                        type     = str,
                        help     = "Proxy SSH key",
                        required = False)

    parser.add_argument('--target_host',
                        action   = 'store',
                        type     = str,
                        help     = "Target IP Address / Hostname",
                        required = True)

    parser.add_argument('--target_port',
                        action   = 'store',
                        type     = int,
                        help     = "Target Port",
                        required = True)

    parser.add_argument('--local_port',
                        action   = 'store',
                        type     = int,
                        help     = "Local Port",
                        required = True)

    parser.add_argument('--local_ip',
                        action   = 'store',
                        type     = str,
                        help     = "Local IP Address",
                        default  = "127.0.0.1",
                        required = False)

    parser.add_argument('--process',
                        action   = 'store',
                        type     = str,
                        help     = "Process to execute",
                        required = False)

    args = parser.parse_args()

    process     = args.process
    local_ip    = args.local_ip
    local_port  = args.local_port
    target_port = args.target_port
    target_host = args.target_host
    proxy_host  = args.proxy_host
    proxy_port  = args.proxy_port
    proxy_user  = args.proxy_user
    proxy_pass  = args.proxy_pass
    proxy_key   = args.proxy_key

    if not proxy_user:
        proxy_user = getpass.getuser()

    if not proxy_pass and not proxy_key:
        proxy_key = '~/.ssh/id_rsa'

    if proxy_pass and proxy_key:
        msg = "Proxy SSH password and SSH key cannot exist at the same time\n"
        sys.stderr.write(msg)
        sys.exit(1)

    try:
        if proxy_pass:
            server = sshtunnel.open_tunnel( (proxy_host, proxy_port), \
            ssh_username        = proxy_user, \
            ssh_password        = proxy_pass, \
            remote_bind_address = ( target_host, target_port ), \
            local_bind_address  = ( local_ip, local_port) )
        elif proxy_key:
            server = sshtunnel.open_tunnel( (proxy_host, proxy_port), \
            ssh_username        = proxy_user, \
            ssh_pkey            = proxy_key,  \
            remote_bind_address = ( target_host, target_port ), \
            local_bind_address  = ( local_ip, local_port) )
    except Exception as ex:
        msg = "Error: %s\n"%(str(ex))
        sys.stderr.write(msg)
        sys.exit(1)

    try:
        server.start()
    except Exception as ex:
        msg = "Error: %s\n"%(str(ex))
        sys.stderr.write(msg)
        sys.exit(1)

    if process:
        os.system(process)
        server.stop()
        sys.exit()
    else:
        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()
