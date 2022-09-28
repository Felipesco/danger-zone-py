import socket 

# AF_INET = IPv4
# SOCK_DGRAM = UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    cliente.sendto("Teste de mensagem", ("127.0.0.1", 666))

    resp, userServer = cliente.recvfrom(1024)

    print(str(userServer[0])+": "+ str(resp))

    cliente.close()

except Exception as erro:
    print("Ocorreu erro na conexão")
    print(erro)