#!/usr/bin/env python3

# permissions_auditor.py
# Part of Assignment 2 - Security Auditing

# This module scans a directory and identifies files or direcotories that have dangerous (world-writable) permissions.
# It returns a text report to assignment2.py


# Author: Kaiyan Hu
# Student ID: 178557237



import os
import stat


# ---------------------
# Utility functions
# ---------------------

# Extract the UNIX permission bits (e.g.: "755") from a file using os.stat()
def get_permission_octal(path):

    try:
        # st_mode contains permission bits + file type bits
        mode = os.stat(path).st_mode

        # convert to octal string, remove "0o" prefix
        return oct(mode & 0o777)[2:]

    except (FileNotFoundError, PermissionError):
        # If the file cannot be read (e.g.: due to permissions), simply skip it by returning None.
        return None



# Check if "others" can write -> world-writeable
def is_world_writable(mode_str):
    '''
    mode_str example: "777","757","766"
    Check last digit (others permissions)
    last digit in octal:
        2 -> write
        3 -> write + execute
        6 -> read + write
        7 -> read + write + execute
    '''

    if mode_str is None or len(mode_str) != 3:
        return False

    # Extract the "others" permission (last digit)
    others_digit = int(mode_str[2])
    return others_digit in (2,3,6,7) # world writable


# Dangerous if outside /home direcotries (higher security risk)
def is_outside_home(path):
    return not path.startswith("/home/")



# Determine item type by file type macros from stat module
def get_type(path):
    try:
        mode = os.stat(path).st_mode


        if stat.S_ISDIR(mode):
            return "directory"
        elif stat.S_ISREG(mode):
            return "file"
        else:
            return "others"


    except:
        # if os.stat() fails. return unknown
        return "unknown"



# Get owner UID ( UID 0 = root)
def get_uid(path):
    try:
        return os.stat(path).st_uid
    except:
        return None



# ----------------------
#    Scanning logic
# ----------------------

def scan_directory(target_dir):
    '''
    Recursively scan the target directory. Identify dangerous files and return them as a list of a dictionary.

    How to work:
    - walk through directory using os.walk()
    - for each item, get permissions, type, owner UID
    - world-writable? -> add to findings list

    '''


    findings = []


    # os.walk walks through  all subdirectories
    for root, dirs, files in os.walk(target_dir):
        # combine directory names and file names into a single list
        items = dirs + files


        for item in items:
            # build full path
            full_path = os.path.join(root, item)

            # get permission string
            mode = get_permission_octal(full_path)


            # Only flag world-writable items
            if is_world_writable(mode):

                # determine risk serverity
                risk_label = (
                    "world-writable_outside_home"
                    if is_outside_home(full_path)
                    else "world-writable"
                )


                 # Append dictionary describing it.
                findings.append({
                    "path": full_path,
                    "mode": mode,
                    "type": get_type(full_path),
                    "uid": get_uid(full_path),
                    "risk": risk_label
                })

    return findings





# --------------------
# Report formatter
# --------------------


# Convert the findings list into a clean, readable text report.
def format_report(findings, target_dir):
    # header for the report
    header = "==== Permission Audit Report  ====\n"
    header += f"Directory Scanned: {target_dir}\n\n"


    # if no dangerous files found
    if len(findings) == 0:
        return header + "No dangerous permission found.\n"



    # if dangerous items exist
    output = header + f"{len(findings)} dangerous items found:\n\n"


    # loop with clear variable name: item
    for idx, item in enumerate(findings, start=1):
        output += f"{idx}. Path: {item['path']}/n"
        output += f"    Permission:  {item['mode']}\n"
        output += f"    Type: {item['type']}\n"
        output += f"    Owner UID: {item['uid']}\n"
        output += f"    Risk: {item['risk']}\n\n"

    return output




# ------------------
# Main interface
# ------------------

def run_permission_check(target_dir):
    '''
    public interface for assignment2.py

    assignment2.py will do:
        print(run_permission_check('/etc'))

    this function runs:
    - scan_directory()
    - format_report()
    And returns the final report.

    '''

    results = scan_directory(target_dir)
    return format_report(results, target_dir)










