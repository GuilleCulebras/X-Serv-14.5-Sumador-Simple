#!/usr/bin/python3

import socket


mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind(('localhost',1235))

mySocket.listen(5)

flag = 0

try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()

        print ('Request received:')
        peticion = recvSocket.recv(2048).decode('utf-8', "strict")
        print(peticion)

        favicon = (peticion.split()[1][1:])

        if favicon == "favicon.ico":
            recvSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n" + 
                                "<html><body><h1>Not Found</h1></body></html>\r\n","utf-8"))
            recvSocket.close()
            continue

        

        if (flag == 0):
            recurso = (peticion.split()[1][1:])
            
            try:
                recurso = int(recurso)
            except ValueError:
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body>Me has dado un: " + recurso + ". " + "Vete." + 
                                "</body></html>" +
                                "\r\n","utf-8"))
                recvSocket.close()
                break


            print ('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body>Me has dado un: " + str(recurso) + ". " + 
                                "</body></html>" +
                                "\r\n","utf-8"))
            recvSocket.close()

            flag = 1

        else:
            recurso2 = (peticion.split()[1][1:])

            try:
                recurso2 = int(recurso2)
            except ValueError:
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body>Me has dado un: " + recurso2 + ". " + "Vete." + 
                                "</body></html>" +
                                "\r\n","utf-8"))
                recvSocket.close()
                break


            print ('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                                "<html><body>Me habias dado un: " + str(recurso) + ". " + "Ahora un: " + str(recurso2) + ". " + "Suman: " + str(recurso + recurso2) + "." +
                                "</body></html>" +
                                "\r\n","utf-8"))
            recvSocket.close()

            flag = 0

except KeyboardInterrupt:
    print ("Closing binded socket")
mySocket.close()