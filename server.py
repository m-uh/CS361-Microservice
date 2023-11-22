# bibbe@oregonstate.edu
# emma bibb

import json
import socket

HOST = "127.0.0.1"
PORT = 15153

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

# listen for connection
server_socket.listen()

def get_list(store_name):
    # retrieve the list of items and prices from a file and return it as a dictionary
    # returns a list containing items and their prices

    with open(f'{store_name}.txt') as f:
        list_data = f.read()
    
    # ensure data is in dictonary form
    items = json.loads(list_data)
    return items

def handle_connection(client_socket):
# talks to client connection - recieves the request and list, and then returning it

    while True:
        # receive request from client
        request = client_socket.recv(1024).decode('utf-8')

        if request == "1":
            items = get_list("bobs_grocery,")

        elif request == "2":
            items = get_list("quick_mart,")

        elif request == "3":
            items = get_list("super_saver,")

        else:
            break

        # convert to JSON and send it to the client
        client_socket.sendall(json.dumps(items).encode('utf-8'))

    client_socket.close()

# accept and handle connections
while True:
    client_socket, address = server_socket.accept()
    handle_connection(client_socket)