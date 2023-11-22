# CS361-Microservice
Description:

A microservice (in progress) that creates a list of all store items with their prices. It will read the files containing the items per store, along with their prices before converting it into a list (for each store) with the prices next to them. This allows a customer to view all a store’s items with their prices and compare them to another. The list is converted to JSON and then sent back through socket to the Python.   



How to Launch:

Download files and open the containing folder. In the terminal, type in these two steps to start the socket:

(1): python3 server.py

(2): python3 client.py



Request Data:
In order to request data from the microservice, the requesting program must provide one of the options from the command menu (1 - 4). 


An example call for this Socket would be:
# Example call
send_request("1")  # sends request for Bobs Grocery list
items = receive_data()  # receive data from server


Receive Data:
To receive the data from the microservice, it will be sent back over through the Socket Pipeline in JSON format. 



Unified Modeling Language (UML) Sequence Diagram:


<img width="576" alt="Screenshot 2023-11-22 at 2 48 26 AM" src="https://github.com/m-uh/CS361-Microservice/assets/126530073/834050de-f5e5-4f9a-8db0-ac1f1ac79581">


