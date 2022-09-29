import socket 

# AF_INET = IPv4
# SOCK_STREAM = TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.settimeout(5)

ip = "127.0.0.1"
porta = 777

try:
    cliente.connect((ip, porta))

    st = 'ProtocoloX-SECRETE'

    byt = st.encode()

    cliente.send(byt)

    resp = str(cliente.recv(1024))
    print(resp)

except Exception as erro:
    print("Ocorreu um erro")
    print(erro)