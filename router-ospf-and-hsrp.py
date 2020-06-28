import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

f = open ('routers.txt') #'routers.txt' is just a text file with router management ips

for IP in f:
    IP=IP.strip()
    print ("Configuring Switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
    tn.write(b"enable\n")
    tn.write(b"Jazzmusic70\n")
    tn.write(b"conf t\n")
    tn.write(b"interface f0/0\n")
    tn.write(b"standby 1 ip 192.168.122.115\n")
    tn.write(b"router ospf 1\n")
    tn.write(b"network 0.0.0.0 0.0.0.0 area 0\n")
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
