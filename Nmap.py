#!/usr/bin/python3
import os
import sys
import nmap
import time

def cielo(s):
    for p in s + "\n":
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(1./70)
os.system("clear")
print("\033[32m")
cielo("""
    ___               _           __                        
   / _ \  ___   _ __ | |_        / _\     ___   __ _  _ __  
  / /_)/ / _ \ | '__|| __| _____ \ \     / __| / _` || '_ \ 
 / ___/ | (_) || |   | |_ |_____|_\ \   | (__ | (_| || | | |
 \/      \___/ |_|    \__|       \__/    \___| \__,_||_| |_|
""")
print()

cielo("[Info] \033[35mHerramienta para escanear los puertos abiertos en una dirección IP")
cielo("\033[36m  || \033[35m  Escrito en Python y utiliza Nmap")
cielo("\033[33m  || \033[35m  Creada por Capricornio23 and Benyamin-creator\n")


ip=input("\033[31m[\033[33m+\033[31m] \033[33mIP Objetivo ==> ")
nm = nmap.PortScanner()
puertos_abiertos="-p "
results = nm.scan(hosts=ip,arguments="-sT -n -Pn -T4")
count=0
#print (results)
print("\nHost : %s" % ip)
print("State : %s" % nm[ip].state())
for proto in nm[ip].all_protocols():
        print("Protocol : %s" % proto)
        print()
        lport = nm[ip][proto].keys()
        sorted(lport)
        for port in lport:
                print ("port : %s\tstate : %s" % (port, nm[ip][proto][port]["state"]))
                if count==0:
                        puertos_abiertos=puertos_abiertos+str(port)
                        count=1
                else:
                        puertos_abiertos=puertos_abiertos+","+str(port)

print("\nPuertos abiertos: "+ puertos_abiertos +" "+str(ip))
