
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


