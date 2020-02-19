from socket import *
from time import time
import sys

# Prevent extra or missing arguments from casuing error


# Preparing the socket
hostname = gethostname()
s = socket(AF_INET, SOCK_DGRAM)
s.settimeout(1)

for ping in range(1,11, 1):
    startTime = time() # Retrieve the current time
    try:
        # Sending the message and waiting for the answer
        s.sendto(message.encode(),(serverHost, int(serverPort)))
        encodedModified, serverAddress = clientSocket.recvfrom(1024)

        # Checking the current time and if the server answered
        endTime = time()
        modifiedMessage = encodedModified.decode()
        print(modifiedMessage)
        print("Ping %i: Response Received  RTT: %.3fs\n" % ((endTime - startTime)*1000))
    except:
        print("Ping %i: Timed out\n" % (ping))

s.close()