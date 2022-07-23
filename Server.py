"""
ServerScript

This file connects to the client and obtains information from the client.
Appends information to a file created on the server.
Terminate connection once information is received and input into file.

Server Socket:
socket
bind
listen
accept
--connect--
recieve
send
receive
close

Abigail Sauco
000860402
07.07.22

"""

#import modules
import socket
import sys

#fefine variables
IP = socket.gethostbyname()
PORT = 4455
SIZE = 1024
FORMAT = "utf-8"

#define main which is the bulk of the program that you will be running
def main(): 
    print("[STARTING]")

#initialize TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind IP and port to server
server.bind(IP, PORT)

#make server listen
server.listen()
print("[LISTENING]")

while True:

#make server accept connection
    connect, addr = server.accept()
print(f"[ESTABLISHING CONNECTION] {addr} ")

#receive file from client
filename = connect.recv(SIZE).decode(FORMAT)
print(f"[RECEIVING FILE]")

#open file
file = open(filename, "w")
connect.send("FILE RECEIVED".encode(FORMAT))

#receive file data into client, and write into file
data = connect.recv(SIZE).decode(FORMAT)
print(f"[RECV] Receiving the file data.")
file.write(data)
connect.send("File data received".encode(FORMAT))

#close file
file.close()

#close connection
connect.close()

#print disconnected
print(f"[DISCONNECTED] {addr} ")
if __name__ == "__main__":

    try:    
        main()
    except:
        print("Connection cannot be initialized.")
