
# OPS445 – Group Assignment 2 – Permissions Auditor Module

**Student:** Kaiyan Hu
**Student ID: ** 178557237
**Role in Group:** Responsible for implementing the “Permissions Auditor” modul>


This module is part of our group assignment.
My task was to implement a small tool that checks a directory and reports any
**world-writable files or directories** (e.g., permission 777).
The goal is to help identify items that may be unsafe.

## 1. What the Module Does

The script scans a target directory and checks every file and subdirectory. 
For each item, it collects:

- path 
- permission mode (octal)
- file type
- owner UID
- whether it's world-writable
- whether it's outside the user's home directory

If something is world-writable, the script adds it to the final report and labels the risk level.


## 2. How It Works (Simple Explanation)

The module mainly uses functions from the Python standard library:

- os.walk() go through subdirectories 
- os.stat() get permission bits and owner info
- string/path checks decide if it's inside /home/<user>
- helper functions to format the output in a clean way




## 3. Main Features

- Uses functions only (no global code)
- Standard library only 
- Works on Matrix / MyVMLab 
- Outputs a clear, readable report 
- Flags risky items (world-writable) 
- Marks anything outside `/home` as higher risk



## 4. How to Run

Example usage:
python3 assignment2.py

or if testing the module directly:
python3 test_permissions.py



## 5. Testing
I tested the module by creating temporary directories and files with different permissions:
* safe file (644)
* unsafe file (777)
* files inside and outside /home
The test script prints the audit results so it's easy to confirm whether detection works correctly.



## 6. Files Included
* permissions_auditor.py — my main module
* assignment2.py — the group's main script that imports and uses my module



## 7. Contribution Summary
For this group assignment, I was responsible for the Permissions Auditor.
I wrote the functions for scanning directories, checking permission bits, identifying world-writable items, and formatting the output for the main program.
I also created and ran test cases on Linux Mint to make sure the module behaves correctly.


The module follows all assignment requirements:
* Python standard library only
* Uses functions
* Clear and readable output
* Fully tested and documented
-------------------------------------------------------------------------------------------------------------------
Name: Pirajeen Kandasamy
Role in group: Responsible for adding Service and Port checks
This module is a Service and Port Checker written in Python.


#The Purpose of this Module
Its main purpose is to help users quickly see:
- Which system services are running
- Which network ports are open
- The status of a list of important services such as SSH, Apache, MySQL, etc.

#How it works
1. Running Services
It uses systemctl to pull a list of services that are currently running.
2. Open Ports
It checks which ports are listening using either:

ss or netstat 
3. Specific Service Status, the script loops through a customizable list of services and reports:
- Running
- Not running
-Not installed
This helps quickly verify if critical services are active.

#How to Run
1. Make the file executable (if needed)
chmod +x ServicePortChecker.py

Step 2 — Run it
 /ServicePortChecker.py (install python3 if you dont have)
You should see output for:
-Running services
-Listening ports
-Specific service status

#testing
To test this script for SSH i ran the script without SSH
it gave me an "!not insalled"
Then i downloaded ssh "sudo apt install openssh-server -y"
then i ran the script again, the result was ssh.service is NOT running (might be stopped or disables"
the ive done ssh start
this indicated that it was working correctly

#Files
Included are ServicePortChecker.py	Main Python script that checks services and ports
README.md	Documentation explaining how the module works

## 7. Contribution Summary
For this group assignment, I was responsible for the Service and Port checker.
I wrote the functions for  service detections by using systemctl, using ss or netstat for port detection and srv loop for checking if the requried systems are on file.
I also created and ran test cases on LinuxMint, such as SSH, apache2 etc
