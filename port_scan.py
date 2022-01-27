
#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("IP angeben, die gescannt werden soll: ")
port = int(input("Port angeben, der gescannt werden soll: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("Port ist zu")
    else:
        print("Port ist offen")

portScanner(port)
