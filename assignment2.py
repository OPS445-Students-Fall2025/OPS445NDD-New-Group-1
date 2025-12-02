import subprocess, argparse
import permissions_auditor

#Author of this file: Jaiveer Chawla
#ID: 101618205

banner_text = """
=========================================================================
         OPS445 Assignment 2 Group 1 - Security Auditor Script
=========================================================================
This script calls upon 4 different scripts to run a quick security audit 
of your local linux system.

Note: These security scripts were only tested on a Linux Mint system.

These are the scripts used and their purpose.

#1 User Enumerator
    - Checks to see if only 1 user account (root) has UID 0.
    - Lists only user accounts (not system ones).
    - Lists groups of each user accounts, those with sudo are flagged.
    - Shows the last login for each user account, >= 2 weeks is flagged.

#2 Permissions Auditor
    - Scans the target directory recursively. 
    - Default target directory is the current user's home directory.
    - Finds world-writable files and directories.
    - Labels higher-risk items outside /home.
    - Returns a simple, human-readable report.

#3 Service Port Checker
    - Shows all currently running services via systemctl.
    - Shows which ports are listening via ss or netstat.
    - Check the status of specified services. 
    - Those services are ssh, apache, ngnix, mysql, mariadb and vsftpf

#4 SSH Audit
    - Examines the /etc/ssh/sshd_config file.
    - If that file is not found or readable, it will display typical SSH security misconfigs.
    - Produces 'CRITICAL WARNING' alert for very dangerous misconfigs like 'PermitRootLogin Yes'.
    - Produces 'WARNING' alert for misconfigs that can be hardened.
    - Produces 'GOOD' message if config follows best practices.
"""

def parse_command_args():
    parser = argparse.ArgumentParser(description=banner_text, formatter_class=argparse.RawDescriptionHelpFormatter, epilog="By Jaiveer, Kaiyan, Edwin, and Pirajeen. Copyright 2025.")
    
    #Get user home directory
    user_home_dir = subprocess.Popen(['echo $HOME'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    user_home_dir = user_home_dir.communicate() #Reads the data from the stdout.

    user_home_dir = user_home_dir[0] ##Gets the first index position from the tuple and stores it as bytes. This is in preparation to decode the data into utf-8.

    user_home_dir = user_home_dir.decode('utf-8').splitlines() #Decodes the bytes into utf-8 and then splits lines before storing it as a list.

    parser.add_argument("target", nargs="*", type=str, default=user_home_dir, help="The directory to scan for script #2 'Permission Auditor'. Default/no option given will use the current user's home directory.")

    parser.add_argument("-s", "--script", default=0, type=int, help="Select which script # (1,2,3, or 4) you want to run. Default/no option given will run all security scripts.")

    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = parse_command_args()

    target_dir = args.target[0]

    if args.script == 0:
        #Run all 4 security scripts.
        subprocess.run(["python3", "UserEnumerator.py"])
        print("\n\n\n")
        print(permissions_auditor.run_permission_check(target_dir))
        print("\n\n\n")
        subprocess.run(["python3", "serviceportchecker.py"])
        print("\n\n\n")
        subprocess.run(["python3", "ssh_audit.py"])
    
    elif args.script == 1:
        #Run only 1st security script
        subprocess.run(["python3", "UserEnumerator.py"])
        print("\n\n\n")

    elif args.script == 2:
        #Run only 2nd security script
        print(permissions_auditor.run_permission_check(target_dir))
        print("\n\n\n")

    elif args.script == 3:
        #Run only 3rd security script
        subprocess.run(["python3", "serviceportchecker.py"])
        print("\n\n\n")
    
    elif args.script == 4:
        #Run only 4th security script
        subprocess.run(["python3", "ssh_audit.py"])
        print("\n\n\n")