import serial  # Comunicação
import matplotlib.pyplot as plt # plotar graficos
import time # funçao sleep e process_time()

t = []
distancia = []

# criando uma porta 
portaUSB = serial.Serial('COM4', 500000)
#definindo tempo de aquisição
t_aqu = 1.0 #segundos

arq = open('dados.txt', 'w')

while time.process_time() < t_aqu:
	print(time.process_time())
	data = portaUSB.readline()
	info = str(data)
	info = info.replace("\\xff","") 
	info = info.replace("\\r", "")
	info = info.replace("\\n","")
	info = info.replace("'","")
	info = info.replace("b","")
	arq.write(info+'\n')

arq.close()

arq = open('dados.txt', 'r')

for line in arq: #laço para preencher vetores
	Y,X = line.split(",")
	t.append(X)
	distancia.append(Y)

arq.close()

plt.plot(t, distancia, label = "Distância")
plt.show()
