import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ("aquapi-main", 6401) #Server's IP Adress and Port Number for Communication.
print (sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:
    print (sys.stderr, '\nwaiting to receive message')
    data, address = sock.recvfrom(4096)
    f= open("output.csv","w+")
    f.write(str(data, 'utf-8'))
    f.close()
    print (sys.stderr, 'received %s bytes from %s' % (len(data), address))
    print (sys.stderr, data)

    if data:
        sent = sock.sendto("recieved data".encode('utf-8'), address)
    print (sys.stderr, 'sent %s bytes back to %s' % (sent, address))
