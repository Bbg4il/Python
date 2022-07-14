"""
ServerScript

This file connects to the client and obtains information from the client.
Appends information to a file created on the server.
Terminate connection once information is received and input into file.

Abigail Sauco
000860402
07.07.22

"""

#import module
import socket
import sys

#Define variables
IP = socket.gethostbyname()
PORT = 4455
SIZE = 1024
FORMAT = "utf-8"

def main():
    
print("[STARTING]")

#Start TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind IP and port to server
server.bind(IP, PORT)

#make server listen
server.listen()
print("[LISTENING]")

while True:

#Server has accepted the connection from the client
conn, addr = server.accept()
print(f"[ESTABLISHING CONNECTION] {addr} ")

#Receive file from the client
filename = conn.recv(SIZE).decode(FORMAT)
print(f"[RECIEVING FILE]")

#write into file
file = open(filename, "w")
conn.send("FILE RECEIVED".encode(FORMAT))

#Receive the file data from the client
data = conn.recv(SIZE).decode(FORMAT)
print(f"[RECV] Receiving the file data.")
file.write(data)
conn.send("File data received".encode(FORMAT))

#close file
file.close()

#close connection
conn.close()

print(f"[DISCONNECTED] {addr} ")
if __name__ == "__main__":
    
main()

#Put try except for error handling. If sysadmin.py does not exist.



