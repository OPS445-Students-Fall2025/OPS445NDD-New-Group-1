#!/usr/bin/env python3
#Author: Pirajeen Kadnasamy
#Group 1 
#Service port checker
import subprocess

print("============================================")
print("        PYTHON SERVICE/PORT CHECKER GROUP 1")
print("===========================================\n")


def run_cmd(cmd):
    try:
        # run the command and capture output
        result = subprocess.check_output(cmd, shell=True, text=True)
        return result
    except subprocess.CalledProcessError:
        # if the command fails, just return empty text
        return ""



# SECTION 1: shows what systemctl says is currently running.

print(" Checking running services...\n")

running_services = run_cmd("systemctl list-units --type=service --state=running --no-pager")
print(running_services)

print("---------------------------------------\n")



# SECTION 2: CHECK OPEN PORTS
# We try 'ss' first because it's newer.
# If it's not installed, we fall back to 'netstat'.

print(" Checking open ports (listening)...\n")

# check which command exists by just trying to run it
ss_output = run_cmd("ss -tulnp")
netstat_output = run_cmd("netstat -tulnp")
#we will use ss and netstat
if ss_output.strip():
    print("(Using ss to figure out your ports)")
    print(ss_output)
elif netstat_output.strip():
    print("(Using netstat to figure out your ports)")
    print(netstat_output)
else:
    print(" You have neither ss nor netstat installed.")
    print("Install net-tools with: sudo apt install net-tools")

print("---------------------------------------\n")



# SECTION 3: CHECK SPECIFIC COMMON SERVICES
# We check:
# - does the service exist?
# - is it running?
# Can customize in the future depending on the services that you need.

print(" Checking specific services if you require more contact ur admin\n")
#these below are the samples that we can take, we can always add more
services = ["ssh", "apache2", "nginx", "mysql", "mariadb", "vsftpd"]

for svc in services:
    # Check if service exists at all
    exists = run_cmd(f"systemctl list-unit-files | grep -q '^{svc}.service'")

        # so we just check if the service appears in the list manually.
    svc_list = run_cmd("systemctl list-unit-files")
    
    if f"{svc}.service" in svc_list:
        # Now check if it's running
        status = run_cmd(f"systemctl is-active {svc}")
        
        if "active" in status:
            print(f" {svc}.service is RUNNING (all good)")
        else:
            print(f" {svc}.service is NOT running (might be stopped or disabled)")
    else:
        print(f"! {svc}.service is NOT installed on this system!")

print("\n=======================================")
print("              CHECK COMPLETED")
print("=======================================\n")
