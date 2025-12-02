#Service/Port Checker - OPS445 GRoup 1 
Author: Pirajeen Kandasamy  
Student Email: pkandasamy7@myseneca.ca  
Branch: Pirajeen  

Purpose of the script:
This script helps system admin or help desks to see whats happening on their linux system.
it does 3 things

1. Shows all currently running services
   (uses systemctl to list everything that is actively running)

2. Shows which ports are listening
   (uses ss or netstat depending if the system was correctly updated or not) and see whats connected

3. Check the status of specified services
   (In this script it checks, ssh, apache, ngnix, mysql, mariadb and vsftpf)

The script will tell you if it is running, not running or not installed.

Make sure that when you download the file/script make sure it is executable by using "chmod +x serviceportchecker.py

