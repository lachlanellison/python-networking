import getpass
import telnetlib

HOST = "<device-ip-address>"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"<enable-password / enable-secret>\n")

for vlan in vlans (2,11):
    tn.write(b"vlan " + str(vlan).encode('ascii') + b"\n")
    tn.write(b"name Python_VLAN_" + str(vlan).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")
