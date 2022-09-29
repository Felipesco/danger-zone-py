from encodings import utf_8
import socket 

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
porta = 80

try:
    servidor.bind((ip, porta))
    servidor.listen(5)
    print("Escutando...\nIP: "+ip+":"+str(porta))

    (cliente, endereco) = servidor.accept()
    print("Conexão -> IP: "+ endereco[0])

    while True:
        dados = cliente.recv(1024)
        
        if dados == "ProtocoloX-SECRETE":
            cliente.send(utf_8("Segredos de estado :o"))
        
        else:
            cliente.send(utf_8("Protocolo incorreto :x"))

    servidor.close()

except Exception as erro:
    print("Algo deu erro")
    print(erro)