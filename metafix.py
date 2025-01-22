import subprocess
import os

# Define rules to bolster Windows Firewall settings
firewall_rules = [
    {
        "name": "Block Inbound SMB Traffic",
        "action": "block",
        "direction": "in",
        "protocol": "tcp",
        "localport": "445"
    },
    {
        "name": "Block Inbound RDP Traffic",
        "action": "block",
        "direction": "in",
        "protocol": "tcp",
        "localport": "3389"
    },
    {
        "name": "Block Outbound FTP Traffic",
        "action": "block",
        "direction": "out",
        "protocol": "tcp",
        "remoteport": "21"
    }
]

def run_command(command):
    """Run a command in the Windows command line."""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"Error executing command: {command}\n{result.stderr}")
    else:
        print(f"Success: {command}\n{result.stdout}")

def add_firewall_rule(rule):
    """Add a firewall rule using Windows Firewall command."""
    command = (
        f"netsh advfirewall firewall add rule name=\"{rule['name']}\" "
        f"dir={rule['direction']} action={rule['action']} "
        f"protocol={rule['protocol']} "
        f"{'localport' if rule['direction'] == 'in' else 'remoteport'}={rule['localport' if rule['direction'] == 'in' else 'remoteport']}"
    )
    run_command(command)

def enable_firewall():
    """Ensure Windows Firewall is enabled."""
    command = "netsh advfirewall set allprofiles state on"
    run_command(command)

def configure_firewall():
    """Configure Windows Firewall with predefined rules."""
    enable_firewall()
    for rule in firewall_rules:
        add_firewall_rule(rule)

if __name__ == "__main__":
    print("Configuring Windows Firewall with enhanced security settings...")
    configure_firewall()
    print("Configuration complete.")