import matplotlib.pyplot as plt 
import numpy as np 
 
n = 20000   # numero de pontos que quero no meu gafico
Ts = 20000   # taxa de amostragem
f = 1.0/Ts
w = f  #2pif : frequencia angular : criando eixo da frequencia 

t  = np.linspace(0, Ts, n)  #criando eixo do tempo (start, end, numero de pontos)
xt1 = (5 * np.sin(2.0*np.pi*1000*t)) + (2 * np.cos(2.0*np.pi*2000*t))
xt2 = (6 * np.sin(2.0*np.pi*2000*t)) + (1 * np.cos(2.0*np.pi*3000*t))
xt3 = (7 * np.sin(2.0*np.pi*4000*t)) + (6 * np.cos(2.0*np.pi*4000*t))
xt4 = (8 * np.sin(2.0*np.pi*6000*t)) + (7 * np.cos(2.0*np.pi*5000*t))


xt = xt1 + xt2 + xt3 + xt4

eixo_freq = np.fft.fftfreq(n,f)  # criando eixo da frequencia
mascara = eixo_freq > 0

espectro = np.fft.fft(xt)
magnitude = np.abs(espectro)

fig, (plt1, plt2) = plt.subplots(2)
plt1.plot(eixo_freq[mascara], magnitude[mascara], 'tab:green')
plt1.set_title("Espectro")
plt2.plot(t, xt,'tab:orange')
plt2.set_title("Sinal")
plt.show()

