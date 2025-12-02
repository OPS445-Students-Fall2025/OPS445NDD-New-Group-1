<<<<<<< HEAD
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
=======

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

>>>>>>> 2c81cee128217497447e379e501cc370d9cab9ea

# OPS445 – Group Assignment 2 – SSH Configuration Auditor Module

**Student:** Edwin Roshy  
**Student ID:** 169475233  
**Role in Group:** Responsible for implementing the "SSH Configuration Auditor" module.

This module is part of our group assignment.

My task was to implement a small tool that checks the SSH server configuration and reports any unsafe or weak SSH settings.

The goal is to help identify insecure options in sshd_config and suggest hardening steps.

## 1. What the Module Does

The script analyzes the SSH daemon configuration and reports security-related settings.

It can work in two modes:

- **Real mode** – When `/etc/ssh/sshd_config` is readable, it parses the actual file.
- **Demo mode** – When the file is not available (common on some course VMs), it shows typical SSH misconfigurations and recommended fixes so the script is still demonstrable.

The report focuses on:

- Whether direct root login is allowed (`PermitRootLogin`)
- Whether empty passwords are allowed (`PermitEmptyPasswords`)
- Whether password authentication is enabled (`PasswordAuthentication`)
- SSH protocol version in use (`Protocol`)
- Brute-force related settings (`MaxAuthTries`, `LoginGraceTime`)
- Extra exposure settings like `X11Forwarding` and `AllowTcpForwarding`
- For each setting the script prints:
  - The directive name
  - Its current or example value
  - A message indicating if it is safe, a warning, or critical

## 2. How It Works (Simple Explanation)

The module uses only Python's standard library and follows the same coding style as the User Enumerator module:

- A helper function wraps Linux commands using `subprocess.Popen`, `communicate()`, and `.decode().splitlines()`.
- The script first tests if `/etc/ssh/sshd_config` is readable using a simple shell command.
- If the file exists, it runs `cat /etc/ssh/sshd_config`, then:
  - Skips blank lines and comments (`# ...`)
  - Splits each remaining line on spaces
  - Stores the last seen value for each directive in a dictionary
- It then applies a series of checks to those settings and builds a list of:
  - Critical issues (e.g., `PermitRootLogin yes`)
  - Warnings (e.g., `MaxAuthTries too high`)

- Output is formatted with clear section headers, indented bullet lists, and short recommendation text.

If the config file cannot be read, the script prints a "DEMO MODE" report with typical insecure values and suggested hardening steps, so the assignment can be demonstrated on any Linux VM.

## 3. Main Features

- Uses functions only (no work done at import time)  
- Python standard library only (`subprocess`, basic string methods)  
- Compatible with Matrix / MyVMLab / standard Linux VMs  
- Produces a clear, readable terminal report with section separators  
- Checks multiple SSH best-practice settings, including:
  - `PermitRootLogin`
  - `PermitEmptyPasswords`
  - `PasswordAuthentication`
  - `Protocol`
  - `MaxAuthTries`
  - `LoginGraceTime`
  - `X11Forwarding`
  - `AllowTcpForwarding`
- Graceful fallback when `sshd_config` is not present (demo mode)

## 4. How to Run

From the group assignment main script:

python3 assignment2.py ssh


This assumes the main `assignment2.py` is wired so that the `ssh` subcommand (or equivalent option) calls the SSH Configuration Auditor function.

If you want to test this module directly during development:

python3 ssh_audit.py


## 5. Testing

Testing was done in two ways:

- With no SSH config file available (common on some course environments):  
  - Verified that the script enters demo mode and still prints a full, realistic report  
  - Confirmed the formatting matches the style of the User Enumerator output (section headers, warnings, recommendations)  
- On a Linux system with `sshd_config` present:  
  - Temporarily changed values like `PermitRootLogin`, `PasswordAuthentication`, and `MaxAuthTries` and re-ran the script  
  - Verified that:  
    - Unsafe values are reported as **CRITICAL WARNING** or **WARNING**  
    - Safer settings are not flagged  
    - The recommendation text matches the detected issues

All tests were run from the terminal with `python3`, and the output was checked for clarity and correctness.

## 6. Files Included

- `ssh_audit.py` — my main module that implements the SSH Configuration Auditor  
- `assignment2.py` — the group's main script that calls my module as part of the overall system report / security audit  

(If the code is in a shared file instead, update this section accordingly.)

## 7. Contribution Summary

For this group assignment, I was responsible for the **SSH Configuration Auditor** module.

I implemented:

- The helper function for running Linux commands in the same style as the User Enumerator module  
- The logic to detect whether `/etc/ssh/sshd_config` is readable and to support a demo mode when it is not  
- Parsing of SSH configuration lines into a dictionary of directives and values  
- Checks for multiple security-related SSH settings and classification into critical issues and warnings  
- Human-readable output, including a summary of findings and clear recommendations

The module follows all assignment requirements:

- Uses only the Python standard library  
- Organized as functions suitable for import by `assignment2.py`  
- Produces clean, readable output consistent with the other group modules  
- Tested on Linux to ensure it behaves correctly in both real and demo modes

## 8. References

- Tecmint. (2025). 20 Essential SSH Configurations and Security Tips for Linux. Retrieved from https://www.tecmint.com/ssh-security-linux-tips/  
- Blumira. (2024). Top 18 Tips to Secure SSH on Linux. Retrieved from https://www.blumira.com/blog/secure-ssh-on-linux  
- SSH.com Academy. (2019). sshd_config - How to Configure the OpenSSH Server. Retrieved from https://www.ssh.com/academy/ssh/sshd_config  
- DigitalOcean Community. (2024). SSH Essentials: Working with SSH Servers, Clients, and Keys. Retrieved from https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys  
- Linux Audit. (2025). OpenSSH security and hardening. Retrieved from https://linux-audit.com/ssh/audit-and-harden-your-ssh-configuration/  
- Red Hat. (2025). Eight ways to protect SSH access on your system. Retrieved from https://www.redhat.com/en/blog/eight-ways-secure-ssh
