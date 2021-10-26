# Lab6-TCP-Port
### Purpose of the Lab
The purpose of this lab is to understand the use of log files, which will keep track of interactions to the server from clients
The log file will keep track of the IP address, the time the server was accessed, as well as all HTTP headers sent by the client.

### Client Program
First things first. Make sure the **hostname of the client** matches what the actual **hostname of the device** running the client is.
Using **Python's Socket class, gethostname()** is called and then printed to the screen, showing that the device hostname is consistent.
The next part of the client file is the create a clientSocket object. Initially, the clientSocket is created and then attempts to connect
using the port number provided (in this case port 8000), and then using a try/except statement, will either establish connection or will
print an error message because the connection was denied. Then the TCP connection will close. Very straightforward program so far.
