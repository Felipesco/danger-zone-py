import socket 

# AF_INET = IPv4
# SOCK_STREAM = TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.settimeout(5)

ip = "127.0.0.1"
porta = 80

try:
    cliente.connect((ip, porta))

    st = 'GET /http/1.1\n\n'

    byt = st.encode()

    cliente.send(byt)

    resp = str(cliente.recv(1024))
    print(resp)

except:
    print("Ocorreu erro na conexão")