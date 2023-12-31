# CS361-Microservice

# Description:

A microservice (in progress) that creates a list of all store items with their prices. It will read the files containing the items per store, along with their prices before converting it into a list (for each store) with the prices next to them. This allows a customer to view all a store’s items with their prices and compare them to another. The list is converted to JSON and then sent back through socket to the Python.   



# How to Launch:

Download files and open the containing folder. In the terminal, type in these two steps to start the socket:

(1): python3 server.py

(2): python3 client.py

Note: Ensure you have the .txt files relative path updated in the server file


# Request Data:
In order to request data from the microservice, the requesting program must provide one of the options from the command menu (1 - 4). 


An example call for this Socket would be:

send_request("1")     # sends request for Bobs Grocery list

items = receive_data()     # receive data from server


# Receive Data:
To receive the data from the microservice, it will be sent back over through the Socket Pipeline in JSON format. 


# How to programmatically REQUEST and RECIEVE data
To programmatically request and receive data, you can use the provided client and server code. The server code listens for connections and sends the requested data, while the client code connects to the server, sends a request, and receives the data.

Here's a breakdown of the steps:

1) Run the server code on a server machine. (open the terminal and type "python3 server.py")
2) Run the client code on a client machine. (open the terminal and type "python3 client.py")
- The client will display a menu of store lists and prompt the user to choose a list.
3) Type in your choice from the menu.
- The client will send the user's choice to the server.
- The server will receive the request, retrieve the corresponding list of items and prices, and send the data back to the client.
- The client will receive the JSON data from the server, convert it to a dictionary, and print the items and prices.



# Unified Modeling Language (UML) Sequence Diagram:


<img width="576" alt="Screenshot 2023-11-22 at 2 48 26 AM" src="https://github.com/m-uh/CS361-Microservice/assets/126530073/834050de-f5e5-4f9a-8db0-ac1f1ac79581">


