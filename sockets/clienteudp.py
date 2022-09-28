import socket 

# AF_INET = IPv4
# SOCK_DGRAM = UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    cliente.connect(("google.com", 80))

    st = 'GET /http/1.1\nHost: google.com\n\n'

    byt = st.encode()

    cliente.send(byt)

    resp = str(cliente.recv(1024))
    print(resp)

except:
    print("Ocorreu erro na conexão")