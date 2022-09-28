import socket 

# AF_INET = IPv4
# SOCK_STREAM = TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect()