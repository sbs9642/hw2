#The client program will interact with the user reading a line of input from standard input,
#send the line to the server program over a socket connection,
#receive a response line(s)from the server,
#echo all output from the server to standard output,
#and then wait for another line of input from the user.
#A separate new socket should be created for each interaction between the client and the server.


#HTTP client program should take one command line argument: the port number of the HTTP server to
#connect to. As in HW1, your client should accept input requests from a human user using standard input. The
#client should echo each user input line to standard output along with the corresponding response line specified
#in HW1. The client program will terminate when end-of-file is reached on standard input in exactly the same
#manner as in your solution to Homework 1.


import sys
from socket import *
global port_number



port_number = sys.argv[1]


def client():
    global port_number
    clientSocket = socket(AF_INET, SOCK_STREAM)
    try:
        clientSocket.connect((gethostname(), int(port_number)))
#    print('Connection Error1')
#35

        while(True):
            request = input()
            clientSocket.send(request.encode())
#            print('Connection Error2')


            reply = clientSocket.recv(1024).decode()
 #       print('Connection Error3')
            answer = ''
        #print(reply.decode())
            for line in reply.splitlines():
                print(line)
            #print("Connection closed");
            clientSocket.close()
            return
    except:
        print("Connection Error")
client()
