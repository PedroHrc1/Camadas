
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

    som, samplerate = sf.read('audio.wav')
    print(samplerate)

    dados = som[:,1]

    #signalMeu.plotFFT(sinal, dados, fs)

    paranomalizar = np.max(dados)
    dados_normalizados = dados/paranomalizar

    
    #signalMeu.plotFFT(sinal, dados_normalizados, fs)

    
    
    plt.plot(t, dados_normalizados)#Normalizado
    plt.title('Som')
    plt.show()
    sd.play(dados_normalizados, fs)
    Filtrado = flpf.filtro(dados_normalizados,samplerate, 4000)

    
    plt.plot(t, Filtrado)#Normalizado
    plt.title('Som')
    plt.show()

    signalMeu.plotFFT(sinal, Filtrado, fs) #Filtrado

    portadora = 1* np.cos(2*np.pi*14000*t)

    st = Filtrado*portadora

    signalMeu.plotFFT(sinal, st, fs)
    plt.title("ST")
    plt.show()
    
    plt.plot(t, st)
    plt.title('S')
    plt.show()
    sd.play(st, fs)
    sd.wait()
    sf.write('output.wav', st, fs)

    


    
    
    
    

if __name__ == "__main__":
    main()
