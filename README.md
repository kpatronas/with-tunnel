# with-tunnel
Create an SSH tunnel and keep-it running as long as your process that will use the tunnel.
## What with-tunnel does?
with-tunnel allows to create SSH tunnels running as long as the process that will use the tunnel run, but also there is an option to create persistent tunnels.
## Options explaination
### SSH Proxy options
* --proxy_host: The ssh proxy to be used (Required)
* --proxy_port: The port of the ssh proxy to be used (Not required, default is port 22)
* --proxy_user: The user to be connected to ssh proxy (Not required, default is the running user)
* --proxy_pass: The password to be used to connect to the ssh proxy (Not required)
* --proxy_key:  The ssh key to be used to cinnect to the ssh proxy (Not required)
Note: if no proxy_pass or proxy_key given with-tunnel will try to use the default ssh key of the running user.
