"""
ClientScript

This file establishes a connection to the server and transmits information.
Appends information to a file created on the server.
Terminate connection once information is received and input into file.

Abigail Sauco
000860402
07.07.22

"""

#import modules
import CronTab
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
FORMAT = "utf-8"
SIZE = 1024
def main():
    
#Staring a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connecting to the server
client.connect(IP, PORT)

#Opening and reading the file data
file = open("data/SysAdminCronJob.txt", "r")
try: 
    data = file.read()
except:
    print("File does not exist.")

#Sending the filename to the server
client.send("SysAdminCronJob.txt".encode(FORMAT))
msg = client.recv(SIZE).decode(FORMAT)

print(f"[SERVER]: {msg}")

#Sending the file data to the server
client.send(data.encode(FORMAT))
msg = client.recv(SIZE).decode(FORMAT)
print(f"[SERVER]: {msg}")

#close file
file.close()

#close connection
client.close()
if __name__ == "__main__":
    
try: 
    main()
except: 
    print("An error has occured.")
 





