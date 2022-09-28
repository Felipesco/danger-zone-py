import socket 

# AF_INET = IPv4
# SOCK_STREAM = TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("142.250.218.195", 80))

# print(cliente.send(""))

cliente.recv(1024)