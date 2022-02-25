#accept HTTP connections from clients. The server program, like most servers, will conceptually never terminate.
#It will be terminated by some external means such as typing control-C in the shell.



#For testing, you
#should have your server listen for connections on port number 6000 + the last four digits of your social security
#number. This will minimize the possibilities of a port conflict, but it will not guarantee that port conflicts do not
#occur. Thus, your programs must be prepared to deal with errors that occur when trying to create a socket on a
#port number that is in use by someone else.

#If a client or server encounters a socket error then it should print “Connection Error” to st output

#If the client or server is unable to recover from the socket error then it should terminate.

import sys
from socket import *
import os.path
from os import path
global port_number

port_number = sys.argv[1]
#print('Port Error')

#line 30
server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#print('Connection Error')

server_socket.bind(("", int(port_number)))
server_socket.listen(1) # Allow only one connection at a time

while True:
    connectionSocket, addr = server_socket.accept()
    print("Client Connected to COMP431 HTTP Server")

    request = connectionSocket.recv(1024).decode()
    #print(request)
    reply = str(request)+'\n'
    #print(reply)
    text = str(request)
    #print(text)

    import os.path
    #print(text, end = "")
    index = 0
    URLs_index = 0
    URLe_index = 0
    global HTTPs
    global HTTPe
    global v404
    global v501
    Spurious = False
    HTPPe = 0
    v404 = False
    v501 = False



    def Method():
        if len(text) < 3:
            return False
        if text[0:3] == "GET":
            global index
            index  = 3
            return True
        else:
            return False


    def WhiteSpace():
        global index
        if index > len(text):
            return False
        if text[index] == " " or text[index] == "   ":
            index+=1
            if index >= len(text):
                index= index - 1
                return False
            WhiteSpace()
            return True
        else:
            return False


    def Request_URL():
        global index
        global URLs_index
        global URLe_index
        URLs_index = index
        if text[index] != "/":
            return False
        index += 1
        while (text[index] != " " and text[index] != "      "):
            if (text[index].isalpha() or text[index].isdigit() or text[index] == "." or text[index] == "/" or text[index] == "_"):
                index += 1
            else:
                return False
        URLe_index = index
        return True


    def HTTP_Version():
        global index
        global HTTPs
        global HTTPe
        global Spurious
        HTTPs = index
        HTTPe = HTTPs + 8
        if text[index:index+5] == "HTTP/":
            index = index + 5
            if text[index].isdigit():
                while text[index].isdigit():
                    index += 1
                    if index == len(text)-1:
                        return False
            else:
                return False
            if text[index] == ".":
                index +=1
                if text[index].isdigit():
#dunno
                    if text[index] == text[-1]:
                        HTTPe = index #i edit dis ho
                        return True
                    while text[index].isdigit():
                        index += 1
                        if index == len(text)-1:
                            HTTPe = index
                            return False
                    if not WhiteSpace():
                        #print(index, (len(text)-5))
                        if index <= (len(text)-5):
                            #print("this ho")
                            return False
                    HTTPe = index
                    text1 = text.replace(r"\r", "").replace(r"\n", "")
                    #print(index, len(text1))
                    if (index == (len(text1))): 
                        return True
                    else:
                        Spurious = True
                        if (text[-1].isdigit() or (text[-1] == ".")):
                            Spurious = False
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False





    while True:
        #print("method")
        if not Method():
            reply += ("ERROR -- Invalid Method token." + '\n')
            break
        #print("whitespace")
        if not WhiteSpace():
            reply += ("ERROR -- Invalid Method token." +'\n')
            break
        #print("req url")
        #print(Request_URL())
        #print(v404, v501)
        if Request_URL():
            url = text[URLs_index:URLe_index]
            valid = url.split(".")[1].casefold()
            dumbshit = len(valid)
            if valid == "html" or valid == "txt" or valid == "htm":
                if path.exists(text[URLs_index+1:(URLe_index - dumbshit)]+valid):
                    x=1
                else:
                    v404 = True
                    x=1
            else:
                x=1
                v501 = True
        else:
#            print("path 1")
            reply += ("ERROR -- Invalid Absolute-Path token." + '\n')
            break
        #print("whitespace")
#        if ((not Request_URL()) and (not v404) and (not v501)):
 #           print("path 2")
  #          reply+=("ERROR -- Invalid Absolute-Path token." + '\n')
   #         break
        if not WhiteSpace():
#            if Spurious:
 #               reply+=("ERROR -- Sputious token before CRLF." + '\n')
  #              break
            reply+=("ERROR -- Invalid Absolute-Path  token."+'\n')
            break
        #print("http version")
        if not HTTP_Version():
            if Spurious:
                reply+=("ERROR -- Spurious token before CRLF."+'\n')
                break
            reply+=("ERROR -- Invalid HTTP-Version token."+'\n')
            break
        global HTTPs
        global HTTPe
        reply+=("Method = " + text[0:3] ) +'\n'
        reply+=("Request-URL = " + url)+'\n'
        reply+=("HTTP-Version = " + text[HTTPs:HTTPe])+'\n'



        if v404:
            reply+=("404 Not Found: "+ url)
            break
        if v501:
            reply+=("501 Not Implemented: " + url)
            break
        else:
            reply+= (open(text[URLs_index+1:URLe_index], "r").read())
            break
    #print(reply.read())
    connectionSocket.send(reply.encode())
    connectionSocket.close()
