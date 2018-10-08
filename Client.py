import socket
import sys

message = input("Enter your message:") #Read message to be sent

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('aquapi-main', 6401) #Server's IP Adress and Port Number for Communication.

try:

    # Send data
    print (sys.stderr, 'sending "%s"' % message) # Print the message to be sent.
    sent = sock.sendto(message.encode('utf-8'), server_address) #Send the message

    # Receive response
    print (sys.stderr, 'waiting to receive') #Listen for acknowlegement of file receival 
    data, server = sock.recvfrom(4096) #Receive acknowledgement data
    print (sys.stderr, 'received "%s"' % data) #Print acknowledgement data

finally:
    print (sys.stderr, 'closing socket') #Print prior to closure of socket
    sock.close() #Close the socket
