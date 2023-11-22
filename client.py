# bibbe@oregonstate.edu
# emma bibb

import socket
import json

HOST = "127.0.0.1"
PORT = 15153

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client_socket.connect((HOST, PORT))

def list_menu():
    # displays menu for store lists

    print("""
    1. Bobs Grocery
    2. Quick Mart
    3. Super Saver
    4. Exit
    """)

while True:
    list_menu()
    choice = input("Which list would you like to view? ")

    # if 4, exit
    if choice == "4":
        break

    # send client choice to server
    client_socket.sendall(choice.encode('utf-8'))

    # receive JSON data from server
    data = client_socket.recv(1024).decode('utf-8')

    # convert JSON data to a dictionary and print
    items = json.loads(data)
    for item, price in items.items():
        print(f"{item}: ${price}")

client_socket.close()