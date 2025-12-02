# FALL 2025 Assignment 2
#This is the Security Audit report
My Service/Port Checker script is a simple Bash tool that helps the user see what is happening on their Linux system.
It performs three main checks:

1. Lists all currently running services using systemctl


2. Shows which ports are open/listening using either ss or netstat


3. Checks the status of specific important services (like ssh, apache2, mysql, etc.)



The goal is to quickly understand what’s running on the system and whether essential services are active.

This script does not take any arguments.
You simply run it:

./serviceportchecker

It automatically performs all checks without requiring any user input.

If you want to customize the list of services, you can edit the script and modify this array:

SERVICES=("ssh" "apache2" "nginx" "mysql" "mariadb" "vsftpd")

But no command-line arguments are required.


---

What output it produces

The script prints three sections to the terminal are running services, ports and if any of the services are running.
