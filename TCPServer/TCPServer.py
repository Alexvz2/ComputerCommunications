#import socket module 
from socket import  *

hostname = gethostname()

s = socket(AF_INET, SOCK_STREAM) 
s.bind((hostname, 12000))
s.listen(1)
print('Server Ready to Receive')

while True: 

    conn, addr = s.accept()
    print("Request accepted")

    try:

        recv_data = conn.recv(4096).decode()
        print('The data received by the server:', str(recv_data))
        print('Type:', type(recv_data))

        # Parse request to specific file
        filename = recv_data
        print(filename)
        f = open(filename, 'r') 
        inData = f.read()

        print('File found')

        headerTitle = "HTTP/1.1 200 OK\r\n"

        conn.send(headerTitle.encode())
        conn.send("\r\n".encode())

        for data in inData:
            conn.send(data.encode())
        conn.send("\r\n".encode())

        print('Done')
        conn.close()
        print('connnection closed')

    except IOError:
        print('Error: file not found')

        errHeader = "HTTP/1.1 404 Not Found\r\n"

        conn.send(errHeader.encode())
        conn.send("\r\n".encode())

        # Prompt error page and redirect
        errFile = open("notfound.html", 'r')
        outputErr = errFile.read()

        for data in outputErr:
            conn.send(data.encode())
        conn.send("\r\n".encode())

        print('Done')
        conn.close()
        print('connnection closed')
    s.close()
    print('Connection terminated')
