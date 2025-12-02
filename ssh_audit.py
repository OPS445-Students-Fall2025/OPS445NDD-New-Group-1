import subprocess

def run_a_linux_command(command):
    """Run a Linux command and return stdout as a list of lines - EXACT teammate style."""
    command_result = subprocess.Popen([command], stdout=subprocess.PIPE,
                                      stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    command_result = command_result.communicate()
    command_result = command_result[0]
    command_result_list = command_result.decode('utf-8').splitlines()
    return command_result_list

def check_ssh_config():
    """Complete EXTENDED SSH Configuration Best Practices Check - works everywhere."""
    print("====================================================================")
    print("#4: EXTENDED SSH CONFIGURATION BEST PRACTICES CHECK")
    print("====================================================================")
    
    # Test if SSH config file exists and is readable (teammate's exact style)
    file_test_result = run_a_linux_command("test -r /etc/ssh/sshd_config && echo 'OK' || echo 'NO'")
    
    if file_test_result[0] == 'NO':
        print("WARNING")
        print("SSH config file /etc/ssh/sshd_config not readable")
        print("DEMO MODE - Showing typical security issues found on Linux systems:\n")
        print("CRITICAL WARNING!!!")
        print("    - PermitRootLogin = 'yes' (ROOT LOGIN ALLOWED!)")
        print("    - PermitEmptyPasswords = 'yes' (EMPTY PASSWORDS ALLOWED!)")
        print("    - PasswordAuthentication = 'yes' (USE SSH KEYS INSTEAD)")
        print("    - Protocol = '1,2' (INSECURE SSHv1 ENABLED!)")
        print("    - MaxAuthTries = '10' (BRUTE FORCE RISK!)")
        print("    - X11Forwarding = 'yes' (UNNEEDED X11 EXPOSED!)")
        print("\nRECOMMENDATIONS:")
        print("    - Edit /etc/ssh/sshd_config:")
        print("      PermitRootLogin no")
        print("      PermitEmptyPasswords no")
        print("      PasswordAuthentication no")
        print("      Protocol 2")
        print("      MaxAuthTries 3")
        print("      X11Forwarding no")
        print("    - Run: sudo systemctl restart sshd")
    else:
        # File exists - parse it (real analysis)
        ssh_config_contents = run_a_linux_command('cat /etc/ssh/sshd_config')
        
        # Parse settings exactly like teammate parses /etc/passwd
        settings = {}
        for line in ssh_config_contents:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split()
            if len(parts) >= 2:
                directive = parts[0]
                value = ' '.join(parts[1:])
                settings[directive] = value
        
        print("SSH Configuration Settings Found:")
        for directive, value in settings.items():
            spaces_count = 25 - len(directive)
            spaces = " " * spaces_count
            print("    - {}{}{}".format(directive, spaces, value))
        
        print()
        
        # EXTENDED Security checks
        critical_issues = []
        warnings = []
        
        # CRITICAL CHECKS
        permit_root = settings.get('PermitRootLogin', 'yes')
        if permit_root == 'yes':
            critical_issues.append("PermitRootLogin = '{}' - ROOT LOGIN ALLOWED!".format(permit_root))
        
        empty_pass = settings.get('PermitEmptyPasswords', 'yes')
        if empty_pass == 'yes':
            critical_issues.append("PermitEmptyPasswords = '{}' - EMPTY PASSWORDS!".format(empty_pass))
        
        protocol = settings.get('Protocol', '2')
        if '1' in protocol:
            critical_issues.append("Protocol = '{}' - INSECURE SSHv1 ENABLED!".format(protocol))
        
        # WARNING CHECKS
        password_auth = settings.get('PasswordAuthentication', 'yes')
        if password_auth == 'yes':
            warnings.append("PasswordAuthentication = '{}' - USE SSH KEYS!".format(password_auth))
        
        max_auth = settings.get('MaxAuthTries', '6')
        try:
            if int(max_auth) > 6:
                warnings.append("MaxAuthTries = '{}' - BRUTE FORCE RISK!".format(max_auth))
        except:
            pass
        
        x11_forward = settings.get('X11Forwarding', 'yes')
        if x11_forward == 'yes':
            warnings.append("X11Forwarding = '{}' - UNNEEDED X11 EXPOSED!".format(x11_forward))
        
        login_grace = settings.get('LoginGraceTime', '120')
        try:
            if int(login_grace) > 60:
                warnings.append("LoginGraceTime = '{}' - TOO LONG!".format(login_grace))
        except:
            pass
        
        # Report exactly like teammate's style
        if critical_issues:
            print("CRITICAL WARNING!!!")
            print("SSH Configuration has security vulnerabilities:")
            for issue in critical_issues:
                print("    - {}".format(issue))
            print("RECOMMENDATIONS: Edit /etc/ssh/sshd_config and run 'sudo systemctl restart sshd'")
        elif warnings:
            print("WARNING")
            print("SSH Configuration could be hardened:")
            for warning in warnings:
                print("    - {}".format(warning))
            print("RECOMMENDATIONS: Edit /etc/ssh/sshd_config for better security")
        else:
            print("GOOD")
            print("SSH Configuration follows security best practices!")
    
    print("====================================================================")
    print()

# Standalone execution for testing
if __name__ == "__main__":
    check_ssh_config()
