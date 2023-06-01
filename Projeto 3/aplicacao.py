#####################################################
# Camada Física da Computação
#Carareto
#11/08/2022
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 

import random
from enlace import *
import time
import numpy as np




serialName = "COM5"                  # Windows(variacao de)


def main():
    try:


        print("Iniciou o main")
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com1 = enlace(serialName)
        com1.enable()
        time.sleep(.2)
        com1.sendData(b'\x00')
        time.sleep(1)

        rodando =True

        #HandShake

        header = bytearray()

        header += b'\x00' * 11 + b'\x01'

        eop = bytearray()

        eop += b'\xbb\xbb\xbb'

        pacote_handshake = header + eop

        com1.sendData(pacote_handshake)

                    

        while rodando:
            # Ativa comunicacao. Inicia os threads e a comunicação seiral 
            print("Rodando")
            print("Rodando")
            print("Rodando")
            print("Rodando")

            time.sleep(5)

            print(com1.rx.getBufferLen())

            if com1.rx.getBufferLen() == 0:
                print("Handshake nao realizado")
                tentativa = input("Deseja tentar novamente? (S/N)")
                if tentativa == "S":
                    rodando = True
                    com1.sendData(pacote_handshake)
                    feito = False
                else:
                    rodando = False
                    break
            

            else:
                print("Conexão com Servidor estabelecida")

                imageR = "pequeno.png"

                txBuffer = open(imageR, 'rb').read() #isso é um array de bytes
        
                print("meu array de bytes tem tamanho {}" .format(len(txBuffer)))

                imagem = len(txBuffer)# numero de bits
                pacotes_completos = imagem // 50
                pacote_restante = imagem % 50

                if pacote_restante == 0 : 
                    total_de_pacotes = pacotes_completos
                else:
                    total_de_pacotes = pacotes_completos + 1

                erro = 0 

                if erro == 1:
                    total_de_pacotes += 1


                for i in range(0, total_de_pacotes):
                    com1.rx.clearBuffer()

                    pacote_full = bytearray()

                    #Payload

                    payload = txBuffer[i*50:(i+1)*50]


                    #Header
                    header = bytearray()

                    header +=  total_de_pacotes.to_bytes(4, byteorder='big') #Qtd de pacotes total

                    header +=  len(payload).to_bytes(4, byteorder='big') #Tamanho do payload

                    #Numero do Payload
                    n_p = i + 1
                    header +=  n_p.to_bytes(4, byteorder='big') #Numero do pacote

                    #fim
                    # print("header:{}".format(header))
                    # print ("len header:{}".format(len(header)))

                    pacote_full += header + payload + eop

                    # print("pacote completo:{}".format(pacote_full))

                    com1.sendData(pacote_full)

                    print("Pacote enviado")

                    rfxBufferHeader, nRx = com1.getData(15)
                    server = rfxBufferHeader[11]

                    # print(f"oq foi recebido: {server}")
                    print("*"*50)
                    print(f"Pacote recebido {i+1}")
                    print("*"*50)

                    if server == 0:
                        print("Erro na comunicação - Erro no numero de Pacotes")
                        feito = True
                        break
                    
                    if server == 3:
                        print("Erro na comunicação - Tamanho do pacote incorreto")
                        feito = True
                        break

                    if server == 2 and i+1 != 9:
                        print("Pacote recebido com sucesso")
                        continue
                    elif server == 2 and i+1 == 9:
                        print("Imagem enviada com sucesso")
                        feito = True
                        break
                    else:
                        print("Pacote corrompido")

            if feito == True:
                break

        

    
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()


        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()

