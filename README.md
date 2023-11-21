# CS361-Microservice
Description:

A microservice (in progress) that creates a list of all store items with their prices. It will read the files containing the items per store, along with their prices before converting it into a list (for each store) with the prices next to them. This allows a customer to view all a store’s items with their prices and compare them to another. List is converted to JSON, then sent back thru socket to the Python.   



How to Launch:

Download files and open the containing folder. In the terminal, type in these two steps to start the socket:

(1): python3 server.py

(2): python3 client.py



Request Data:
In order to request data from the microservice, the requesting program must provide one of the options from the command menu (1 - 4). 

An example call for this Socket would be:
socket.connect("tcp://127.0.0.1:33311")

Receive Data:
To receive the data from the microservice, it will be sent back over through the Socket Pipeline in JSON format. 



Unified Modeling Language (UML) Sequence Diagram:


<img width="776" alt="Screenshot 2023-11-21 at 1 48 10 AM" src="https://github.com/m-uh/CS361-Microservice/assets/126530073/5f44aea8-e05b-4669-b00f-2a96122ef9ed">


