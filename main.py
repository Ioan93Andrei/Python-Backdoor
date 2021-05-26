import socket
import os
import platform

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

def get_info():
    answer = input("Would you like to discover information about the machine? yes/no ")
    if(answer == "yes"):
        machine = platform.uname()
        print(machine)
    else:
        print("Suit yourself.")

scan_port()
get_info()

#Scan for infomation about the machine and operating system



#Browse the file system