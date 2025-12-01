import subprocess, sys

def run_a_linux_command(command):
    #Use the subprocess.Popen to run a linux command
    command_result = subprocess.Popen([command], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    #Reads the data from the stdout.
    command_result = command_result.communicate()
    
    #Gets the first index position from the tuple and stores it as bytes. This is in preparation to decode the data into utf-8.
    command_result = command_result[0]

    #Decodes the bytes into utf-8 and then splits lines before storing it as a list.
    command_result_list = command_result.decode('utf-8').splitlines()

    return command_result_list


def list_accounts_with_uid_0_and_obtain_only_user_accounts(etc_passwd_contents_list):
    accounts_with_uid_0 = []

    only_user_accounts = []

    #Go through every account from the etc_passwd_contents_list and find accounts with UID 0. Also find accounts with UID >=1000 and not 65534 (nobody account) or if the account has a home dir. Those are user accounts.
    for account in etc_passwd_contents_list:
        
        account_split_by_colon_delimiter = account.split(":")
        
        #If the 3rd colon delimited field has a value of 0, then it means that account UID is 0. It will be added to the accounts_with_uid_0 list.
        account_uid = int(account_split_by_colon_delimiter[2])

        home_dir_string = "/home"
        account_home_dir_field = (account_split_by_colon_delimiter[5])
        
        #Account with full root powers found!
        if account_uid == 0:
            accounts_with_uid_0.append(account)

        #Its a user account if UID >=1000 or if there is a '/home' in the accounts home dir field. Also the account UID cannot be 65534 as that means it is the nobody account.
        if (account_uid>= 1000 or home_dir_string in account_home_dir_field) and account_uid!=65534:
            only_user_accounts.append(account)
    
    return accounts_with_uid_0, only_user_accounts

#Return the account username field when provided with the full account details as shown in /etc/passwd for an account
def extract_account_username(account):
    account = account.split(":") #Split the account by the colon delimiter
    account_username = account[0] #The account username will be the first field
    
    return account_username

#Get contents of /etc/passwd file
etc_passwd_contents_list = run_a_linux_command('cat /etc/passwd')

#Get accounts with UID 0 as well as only the user accounts (not system accounts)
accounts_with_uid_0, only_user_accounts = list_accounts_with_uid_0_and_obtain_only_user_accounts (etc_passwd_contents_list)

print("==============================================================" + "\n" + "#1: Checking To See If Only 1 User Account (root) Has UID 0..." + "\n" + "==============================================================")

#Display critical warning message and recommendations if more than 1 account is found to have UID 0.
if len(accounts_with_uid_0) > 1:
    print("CRITICAL WARNING!!!" + "\n")
    print("You have more than 1 user account with UID 0! Only root account should have UID 0! The value of UID 0 gives the other account the same powers as root!" + "\n")

    print("List Of Users With UID 0:")
    #List every accounts full details which have uid 0.
    for account in accounts_with_uid_0:
        print("    - ",account)

    #Extract the username of the account other than root who has uid 0.
    other_account_that_has_uid_0 = accounts_with_uid_0[1]
    other_account_that_has_uid_0_username = extract_account_username(other_account_that_has_uid_0)

    #Display recommendations.
    print("\n" + "RECOMMENDATIONS: Immediately delete user account '" + other_account_that_has_uid_0_username + "'. Investigate system for possible cyber attack involving user account '" + other_account_that_has_uid_0_username + "'." + "\n\n")

#Display 'GOOD' message and give no recommendations.
else:
    print("GOOD" + "\n")
    print("Only root user account has UID 0!" + "\n")
    print("List Of Users With UID 0:")
    #List every accounts full details which have uid 0.
    for account in accounts_with_uid_0:
        print("    - ",account)
    
    #Display recommendations.
    print("\n" + "RECOMMENDATIONS: None" + "\n\n")

print("==============================================================" + "\n" + "#2: List Of Only User Accounts (Not System Accounts)" + "\n" + "==============================================================")

for account in only_user_accounts:
    account_username = extract_account_username(account)
    print("    -" + account_username)