#Attention.

This script, written in Python, demostrates Denial of service(DoS) attack.
This script does not intend to target any particular webiste and is used for educational purposes only.

The scripts accepts several arguments, but only one can be inserted.
Run the script in the Linux Kernel like:

root@user#: python dos.py www.somedomain.com

How It Works:
A socket is created and connected to host passed in the argument and the a junk messgae is sent as request to site.
The distributed DOS can be made by running the script from multiple machines.
