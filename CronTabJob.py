"""
CronTab Job Maker

This script regularly runs a cron job at boot.

-SysAdminTask.py creates a NEW file with all information
-A Crontab job ran the Client.py script and sent the NEW file over to server
-The NEW file is opened on the server machine to prove that all content exists in that file

Abigail Sauco
000860402
07.07.22

Skeleton code for crontab provided by Marcel Toszer in CPRG 261 Module 8.

Run (pip3 install python-crontab) on linux machine to install crontab.

"""

#import crontab from crontab (pip3 install python-crontab)
from crontab import CronTab

userName = 'abigail2'
cron = CronTab(user=userName)

# create new cron job & define parameters for the job
job = cron.new(command='/usr/bin/python /home/abigail2/Documents/CPRG-261/Project_3/SysAdminTask.py >> /home/abigail2/Documents/CPRG-261/Project_3/Cron3.log')
#job.minute.every(1) RUN AT STARTUP

cron.write()

# create new cron job to run Client.py
job = cron.new(command='/usr/bin/python /home/abigail2/Documents/CPRG-261/Project_3/Client.py')
job.minute.every(1)

# Clearing the restrictions of a job
job.clear()
