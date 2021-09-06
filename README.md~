# with-tunnel
Create an SSH tunnel and keep-it running as long as your program runs
## What with-tunnel does?
with-tunnel allows to create SSH tunnels running as long as the process that will use the tunnel run, but also there is option to create persistent tunnels.

## Options explaination
### SSH Proxy options
* --proxy_host: The ssh proxy to be used (Required).
* --proxy_port: The port of the ssh proxy to be used (Not required, default is port 22).
* --proxy_user: The user to be connected to ssh proxy (Not required, default is the running user).
* --proxy_pass: The password to be used to connect to the ssh proxy (Not required).
* --proxy_key:  The ssh key to be used to connect to the ssh proxy (Not required).

Note: if no proxy_pass or proxy_key given with-tunnel will try to use the default ssh key of the running user. Giving at the same time proxy_pass and proxy_key is not allowed.

### Target options
* --target_host: The host on the end of the tunnel that we want to establish connection (Required).
* --target_port: The port of the host on the end of the tunnel that we want to establish connection (Required).

### Local options
* --local_ip: A local machine ip to be used to create the start of the tunnel (Not required, default is 127.0.0.1).
* --local_port: A port of the local machine to be used to create the start of the tunnel (Required).

### Process options
* --process: The program to be executed, with-tunnel will exit when the program is completed, in case that process option is not given, with-tunnel will keep the tunnel open until is terminated with a ctrl+c.

Note: if your program has parammeters you need to pass the program and its parameters surrounded with quotes. 
