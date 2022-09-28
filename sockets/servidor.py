import socket 

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
porta = 80

try:
    servidor.bind((ip, porta))
    servidor.listen(5)
    print("Escutando...\nIP: "+ip+":"+str(porta))

    print(servidor.accept())

except Exception as erro:
    print("Algo deu erro")
    print(erro)