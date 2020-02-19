# Import sys to retrieve the arguments
from socket import *

hostname = gethostname()

# Preparing the socket
filename = input('Input filename:')
print(filename)
s = socket(AF_INET, SOCK_STREAM)
try:
    s.connect((hostname, 12000))
except: # In case the server is not available
    print("Sorry, the server is currently offline or busy.")
    s.close()
    sys.exit()
print("Connection OK.")

httpRequest = filename 
s.sendall(httpRequest.encode()) #send all or send
print("Request message sent.")

print("Server HTTP Response:\r\n")

data = ""
while True:
    s.settimeout(5)
    newData = s.recv(4096).decode()
    data += newData
    if (len(newData) == 0):
        break
print('Received data after decoding:', data)
print(type(data))

s.close()
print("Closing Connection")