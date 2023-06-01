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

        n = 0

        




        print("Iniciou o main")
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com1 = enlace(serialName)
        
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com1.enable()
        time.sleep(.2)
        com1.sendData(b'00')
        time.sleep(1)

        
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print("Abriu a comunicação")


        #Client
        C1 = b'\x00\x00\x00\x00' 
        C2 = b'\x00\x00\xAA\x00' 
        C3 = b'\xAA\x00\x00' 
        C4 = b'\x00\xAA\x00' 
        C5 = b'\x00\x00\xAA' 
        C6 = b'\x00\xAA' 
        C7 = b'\xAA\x00' 
        C8 = b'\x00' 
        C9 = b'\xFF' 


        bytes_val = len(C1).to_bytes(1, byteorder='big')
        #print(bytes_val)

        

        lista_comandos = [C1, C2, C3, C4, C5, C6, C7, C8, C9]

        lista_com_select = []

        n_comandos = random.randint(10, 30)
        #print("n_comandos = {}" .format(n_comandos))

        i = 0

        while i < n_comandos:
            comando = random.choice(lista_comandos)
            comando = len(comando).to_bytes(1, byteorder='big') + comando 

            lista_com_select.append(comando)
            i += 1

        arraydebites = bytearray()
        for c in lista_com_select:
            arraydebites += c

        arraydebites += b'\xbb'

        print(arraydebites)

        #print(f"tamanho {arraydebites[0]}")  
                  
        #aqui você deverá gerar os dados a serem transmitidos. 
        #seus dados a serem transmitidos são um array bytes a serem transmitidos. Gere esta lista com o 
        #nome de txBuffer. Esla sempre irá armazenar os dados a serem enviados.
        
        #txBuffer = imagem em bytes!
        txBuffer = arraydebites


        #open(imageR, 'rb').read() #isso é um array de bytes
       
        #print("meu array de bytes tem tamanho {}" .format(len(txBuffer)))
        #faça aqui uma conferência do tamanho do seu txBuffer, ou seja, quantos bytes serão enviados.
       
            
        #finalmente vamos transmitir os todos. Para isso usamos a funçao sendData que é um método da camada enlace.
        #faça um print para avisar que a transmissão vai começar.
        #tente entender como o método send funciona!
        #Cuidado! Apenas trasmita arrays de bytes!
               
        
        time.sleep(.2)
        com1.sendData(np.asarray(txBuffer))
        time.sleep(1) 
        
        #as array apenas como boa pratica para casos de ter uma outra forma de dados
          
        # A camada enlace possui uma camada inferior, TX possui um método para conhecermos o status da transmissão
        # O método não deve estar fincionando quando usado como abaixo. deve estar retornando zero. Tente entender como esse método funciona e faça-o funcionar.
        txSize = com1.tx.getStatus()
        #print('enviou = {}' .format(txSize))
        
        #Agora vamos iniciar a recepção dos dados. Se algo chegou ao RX, deve estar automaticamente guardado
        #Observe o que faz a rotina dentro do thread RX
        #print um aviso de que a recepção vai começar.
        
        #Será que todos os bytes enviados estão realmente guardadas? Será que conseguimos verificar?
        #Veja o que faz a funcao do enlaceRX  getBufferLen
      
        #acesso aos bytes recebidos

               
        n = False
        
        while com1.rx.getBufferLen() < 1:
            time.sleep(5)
            n = True
            break

        if n:
            raise Exception ("Não recebeu nada - Timeout")
            

        rxBuffer, nRx = com1.getData(1)

        print("recebeu {} bytes" .format(len(rxBuffer)))
        
        for i in range(len(rxBuffer)):
            print("Numero de comandos mandados: {}" .format(n_comandos))
            print("Numero de comandos recebidos: {}" .format(rxBuffer[i]))
            

        if rxBuffer[0] == n_comandos:
            print("Tudo certo")
        else:
            print("Numero de Comandos Diferentes")
        

    
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

