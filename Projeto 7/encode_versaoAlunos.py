
#importe as bibliotecas
from suaBibSignal import *
import numpy as np
from os import system as sys
import sounddevice as sd
import matplotlib.pyplot as plt

#funções a serem utilizadas
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)

def generateSin(freq, time, fs):
    n = time*fs #numero de pontos
    x = np.linspace(0.0, time, n)  # eixo do tempo
    s = np.sin(freq*x*2*np.pi)
    plt.figure()
    plt.plot(x,s)
    return (x, s)



def main():
    
   
    #********************************************instruções*********************************************** 
    # seu objetivo aqui é gerar duas senoides. Cada uma com frequencia corresposndente à tecla pressionada
    # então inicialmente peça ao usuário para digitar uma tecla do teclado numérico DTMF
    # agora, voce tem que gerar, por alguns segundos, suficiente para a outra aplicação gravar o audio, duas senoides com as frequencias corresposndentes à tecla pressionada, segundo a tabela DTMF
    # Essas senoides tem que ter taxa de amostragem de 44100 amostras por segundo, entao voce tera que gerar uma lista de tempo correspondente a isso e entao gerar as senoides
    # Lembre-se que a senoide pode ser construída com A*sin(2*pi*f*t)
    # O tamanho da lista tempo estará associada à duração do som. A intensidade é controlada pela constante A (amplitude da senoide). Construa com amplitude 1.
    # Some as senoides. A soma será o sinal a ser emitido.
    # Utilize a funcao da biblioteca sounddevice para reproduzir o som. Entenda seus argumento.
    # Grave o som com seu celular ou qualquer outro microfone. Cuidado, algumas placas de som não gravam sons gerados por elas mesmas. (Isso evita microfonia).
    
    # construa o gráfico do sinal emitido e o gráfico da transformada de Fourier. Cuidado. Como as frequencias sao relativamente altas, voce deve plotar apenas alguns pontos (alguns periodos) para conseguirmos ver o sinal
    

    print("Inicializando encoder")
    print("Aguardando usuário")
    numero = int(input("Digite um numero de 0 a 9: "))
    print("Gerando senoide referente ao numero {}".format(numero))
    # Definindo frequências
    if numero == 1:
        f1 = 1209
        f2 = 697
    elif numero == 2:
        f1 = 1336
        f2 = 697
    elif numero == 3:
        f1 = 1477
        f2 = 697
    elif numero == 4:
        f1 = 1209
        f2 = 770
    elif numero == 5:
        f1 = 1336
        f2 = 770
    elif numero == 6:
        f1 = 1477
        f2 = 770
    elif numero == 7:
        f1 = 1209
        f2 = 852
    elif numero == 8:
        f1 = 1336
        f2 = 852
    elif numero == 9:
        f1 = 1477
        f2 = 852
    elif numero == 0:
        f1 = 1336
        f2 = 941
    else:
        print("Numero invalido")
        exit()
    # Definindo tempo
    fs = 44100
    t = np.linspace(0, 3, 3*fs)
    # Definindo senoides
    sin1 = np.sin(2*np.pi*f1*t)
    sin2 = np.sin(2*np.pi*f2*t)
    # Definindo tom
    print("Gerando Tons base")
    tone = sin1 + sin2
    # Definindo frequência de amostragem
    
    # Definindo sinal
    signal = tone
    # Definindo número
    NUM = numero
    # Exibindo gráficos
    plt.plot(t, signal)
    plt.title("Sinal")
    plt.xlabel("Tempo")
    plt.ylabel("Amplitude")
    plt.show()


    print("Executando as senoides (emitindo o som)")
    print("Gerando Tom referente ao símbolo : {}".format(NUM))
    sd.play(tone, fs)
    # Exibe gráficos
    plt.show()
    # aguarda fim do audio2
    sd.wait()
    sinal = signalMeu()
    signalMeu.plotFFT(sinal, signal, fs)
    

if __name__ == "__main__":
    main()
