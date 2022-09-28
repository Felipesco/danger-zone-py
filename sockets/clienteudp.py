import socket 

# AF_INET = IPv4
# SOCK_DGRAM = UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    cliente.sendto("Teste de mensagem", ("google.com", 80))

    resp = cliente.recvfrom(1024)

except:
    print("Ocorreu erro na conexão")