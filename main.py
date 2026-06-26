from firewall import *
from validator import *


def menu():
    print("\n==============================")
    print(" MINI FIREWALL CONTROLLER")
    print("==============================")
    print("1. Enable Firewall")
    print("2. Disable Firewall")
    print("3. Block Port")
    print("4. Allow Port")
    print("5. Block IP")
    print("6. Allow IP")
    print("7. Block IP on Port")
    print("8. Allow IP on Port")
    print("9. Show Status")
    print("10. Reset Firewall")
    print("11. Exit")


while True:

    menu()

    choice = input("Choice: ")

    if choice == "1":
        enable_firewall()

    elif choice == "2":
        disable_firewall()

    elif choice == "3":

        port = input("Port: ")

        if validate_port(port):
            block_port(port)
        else:
            print("Invalid port.")

    elif choice == "4":

        port = input("Port: ")

        if validate_port(port):
            allow_port(port)
        else:
            print("Invalid port.")

    elif choice == "5":

        ip = input("IP: ")

        if validate_ip(ip):
            block_ip(ip)
        else:
            print("Invalid IP.")

    elif choice == "6":

        ip = input("IP: ")

        if validate_ip(ip):
            allow_ip(ip)
        else:
            print("Invalid IP.")

    elif choice == "7":

        ip = input("IP: ")
        port = input("Port: ")

        if validate_ip(ip) and validate_port(port):
            block_ip_port(ip, port)
        else:
            print("Invalid IP or Port.")

    elif choice == "8":

        ip = input("IP: ")
        port = input("Port: ")

        if validate_ip(ip) and validate_port(port):
            allow_ip_port(ip, port)
        else:
            print("Invalid IP or Port.")

    elif choice == "9":
        status()

    elif choice == "10":

        confirm = input(
            "Reset all firewall rules? (yes/no): "
        )

        if confirm.lower() == "yes":
            reset()

    elif choice == "11":
        print("Goodbye.")
        break

    else:
        print("Invalid option.")
