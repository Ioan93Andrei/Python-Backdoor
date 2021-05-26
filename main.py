import socket
import os
import platform
from functions import *

#Getting the target IP addresse and the ports to scan.
target_ip = input("Please type in the target IP address: ")
target_port = input("Please type in the target ports range (ex. 0 - 500): ")

#Spliting the ports from the lowes number to the highest and converting them into int.
lowpoint = int(target_port.split("-")[0])
highpoint = int(target_port.split("-")[1])

#Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Scanning for open ports.
def scan_port():
    for port in range(lowpoint, highpoint):
        status = s.connect_ex((target_ip, port))
        if(status == 0):
            print("Port",port, "is OPEN.")
        else:
            print("Port",port,"is CLOSED")
            
scan_port()
    # answer = int(input("Type the port you would like to connect to: "))
    # if(answer == status):
    #     print("Connecting...")
    # else:
    #     print("Port is closed.")


#Scan for infomation about the machine and operating system

#Browse the file system