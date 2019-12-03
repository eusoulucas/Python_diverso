import matplotlib.pyplot as plt 
import numpy as np 
from scipy import signal
from scipy.signal import butter, filtfilt
 
n = 200000   # numero de pontos que quero no meu gafico
Ts = 200000   # taxa de amostragem
f = 1.0/Ts
nyq = 0.5 * Ts
#w = f  2pif : frequencia angular : criando eixo da frequencia 

t  = np.linspace(0, Ts, n)  #criando eixo do tempo (start, end, numero de pontos) Ts = n => grafico bonito
xt1 = (5 * np.sin(2.0*np.pi*(1000/nyq)*t)) + (2 * np.cos(2.0*np.pi*(5000/nyq)*t))
xt2 = (6 * np.sin(2.0*np.pi*(2000/nyq)*t)) + (1 * np.cos(2.0*np.pi*(3000/nyq)*t))
xt3 = (7 * np.sin(2.0*np.pi*(4000/nyq)*t)) + (6 * np.cos(2.0*np.pi*(4000/nyq)*t))
xt4 = (8 * np.sin(2.0*np.pi*(6000/nyq)*t)) + (7 * np.cos(2.0*np.pi*(5000/nyq)*t))

xt = xt1 + xt2 + xt3 + xt4

eixo_freq = np.fft.fftfreq(n,f)  # criando eixo da frequencia (comprimento, espaço entre amostras)
mascara = eixo_freq > 0 # pegando somente frequencias positivas (não existem frequencias negativas)

espectro = np.fft.fft(xt)  # calculando a tf do sinal xt
magnitude = np.abs(espectro) # calculando o modulo do espectro xt

b, a = signal.butter(3, [2000/nyq, 3000/nyq], btype ="bandpass", analog = False)  
	#(ordem do filtro, freq, tipo, tipo retorno)
	#defaut do tipo de retorno é digital

sinal_filtrado =  filtfilt(b, a, xt)

espectro2 = np.fft.fft(sinal_filtrado)
magnitude2 = np.abs(espectro2)

w, H = signal.freqs(b, a)  
	#a função freqs calcula a resposta em frequencia do filtro

fig, (plt1, plt2) = plt.subplots(2) #plotando dois graficos em uma unica janela
plt1.plot(eixo_freq[mascara], magnitude2[mascara], 'tab:green') #plotando espectro
plt1.set_title("Espectro") #configurando titulo
plt2.plot(t, sinal_filtrado,'tab:orange')  #plotando sinal no tempo
plt2.set_title("Sinal") #configurando titulo
plt.show() #mostrar graficos plotados

