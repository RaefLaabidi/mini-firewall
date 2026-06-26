import subprocess
from logger import log_action


def execute(command, action):

    result = subprocess.run(command)

    if result.returncode == 0:
        print("\n✅ Success\n")
        log_action(action, "SUCCESS")
    else:
        print("\n❌ Failed\n")
        log_action(action, "FAILED")


def enable_firewall():
    execute(["sudo", "ufw", "enable"], "ENABLE_FIREWALL")


def disable_firewall():
    execute(["sudo", "ufw", "disable"], "DISABLE_FIREWALL")

#Do not allow any incoming TCP traffic whose destination port is 23
def block_port(port):
    execute(
        ["sudo", "ufw", "deny", f"{port}/tcp"],
        f"BLOCK_PORT_{port}",
    )

#Allow incoming TCP traffic to destination port 23
def allow_port(port):
    execute(
        ["sudo", "ufw", "allow", f"{port}/tcp"],
        f"ALLOW_PORT_{port}",
    )

#deny ALL traffic coming from this IP address
def block_ip(ip):
    execute(
        ["sudo", "ufw", "deny", "from", ip],
        f"BLOCK_IP_{ip}",
    )

#allow ALL traffic coming from this IP address
def allow_ip(ip):
    execute(
        ["sudo", "ufw", "allow", "from", ip],
        f"ALLOW_IP_{ip}",
    )


def block_ip_port(ip, port):
    execute(
        [
            "sudo",
            "ufw",
            "deny",
            "from",
            ip,
            "to",
            "any",
            "port",
            str(port),
        ],
        f"BLOCK_{ip}_{port}",
    )


def allow_ip_port(ip, port):
    execute(
        [
            "sudo",
            "ufw",
            "allow",
            "from",
            ip,
            "to",
            "any",
            "port",
            str(port),
        ],
        f"ALLOW_{ip}_{port}",
    )


def status():
    subprocess.run(["sudo", "ufw", "status", "numbered"])


def reset():
    execute(["sudo", "ufw", "reset"], "RESET_FIREWALL")
