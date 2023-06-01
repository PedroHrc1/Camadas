#importe as bibliotecas
from suaBibSignal import *
import numpy as np
from os import system as sys
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal
import funcoes_LPF as flpf
import math


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

    sinal = signalMeu()
    fs = 44100
    t = np.linspace(0, 3, fs*3)

    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:
    sd.default.samplerate = 44100 #taxa de amostragem
    tempo = 3
    fs = 44100
    sd.default.channels = 2 #numCanais # o  numero de canais, tipicamente são 2. Placas com dois canais. Se ocorrer problemas pode tentar com 1. No caso de 2 canais, ao gravar um audio, terá duas listas
    duration =  tempo # #tempo em segundos que ira aquisitar o sinal acustico captado pelo mic
    numAmostras = duration*sd.default.samplerate
    freqDeAmostragem = fs
   
    som, samplerate = sf.read('output.wav')
    print(som)
    
    print("...     FIM")

    plt.plot(t, som)
    plt.title('Som Modulado x Dominio no Tempo')
    plt.show()
    sd.play(som, fs)
    signalMeu.plotFFT(sinal,som,fs)
    plt.title('Dominio da Frequencia')
    plt.show()

    portadora = 1* np.cos(2*np.pi*14000*t)

    st = som*portadora

    plt.plot(t, st)
    plt.title('Som modulado')
    plt.show()

    signalMeu.plotFFT(sinal, st, fs)
    plt.title("Frequencia Modulada")
    plt.show()

    

    filtro = flpf.filtro(st, samplerate, 4000)
    plt.plot(t, filtro)
    plt.title('filtro')
    plt.show()
    sd.play(filtro, fs)
    sd.wait()
    sf.write('filtro.wav', filtro, fs)

    signalMeu.plotFFT(sinal, filtro*2, fs)
    plt.title("FOURIER FILTRO")
    plt.show()
    


    


if __name__ == "__main__":
    main()
    print("Fim do programa")