'''SysAdminTask.py

This script obtains the following:
•User name
•Computer name
•Date and time (formatted in an easily readable format such as HH:MM:SS DD/MM/YYYY )
•number of processes running
•Top 10 process NAMES/Command, ID and Memory listed and sorted from most Memory % used on machine first

AbigailSauco
000860402
12.07.22

'''

#import modules
import os
import platform
import psutil

#import datetime and pytz for correct time zone
import datetime
import pytz

#create txt file
f = ("SysAdminCronJob.txt","x")

#retrieve user name
print("USER NAME:"+ os.getlogin())

with open("SysAdminCronJob.txt", "a") as f:
	f.write("USER NAME:"+ os.getlogin())

#retrieve computer name
print("COMPUTER_NAME:"+ platform.machine())

with open("SysAdminCronJob.txt", "a") as f:
	f.write("COMPUTER_NAME:"+ platform.machine())

#retrieve date and time ( YYYY/MM/DD HH:MM:SS )
current_time = datetime.datetime.now(pytz.timezone('Canada/Mountain'))
print("DATE AND TIME:" + current_time)

with open("SysAdminCronJob.txt", "a") as f:
	f.write("DATE AND TIME:" + current_time)

#retrieve no. of processes running
c = 0

for process in psutil.process_iter ():
    c = c+1
    
print("\nThe total number of processes currently running is: ", c)

with open("SysAdminCronJob.txt", "a") as f:
	f.write("DATE AND TIME:" + current_time)

#List top ten processes NAMES/Command, ID and memory sorted from most memory.
TOP_PROC = os.system("ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head")
print("TOP 10 PROCESSESS: " + TOP_PROC)

with open("SysAdminCronJob.txt", "a") as f:
	f.write("TOP 10 PROCESSESS: " + TOP_PROC)


