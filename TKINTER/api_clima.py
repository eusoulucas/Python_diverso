from tkinter import *
from PIL import ImageTk, Image
import requests

def format_resposta(clima): 	
    nome = clima['name']
    tempo = clima['weather'][0]['main']
    descricao = clima['weather'][0]['description']
    temperatura = clima['main']['temp']

    resposta = 'Cidade: %s \nCondições: %s \nDescrição: %s \n Temperatura: %sºC' % (nome, tempo, descricao, temperatura)

    return resposta

def get_clima(cidade):
    clima_chave = '086e0a60948eae45a16937731465ffe5'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parametros = {'APPID' : clima_chave, 'q': cidade , 'units': 'metric'}
    resposta = requests.get(url, params = parametros)
    clima = resposta.json()

    label_info['text'] = format_resposta(clima)

def sair():
    janela_main.destroy()

janela_main = Tk()
janela_main.geometry("450x550")
janela_main.title("Clima e Tempo")

img_back = PhotoImage(file = 'landscape.png')

background = Label(janela_main, image = img_back)
background.place(relwidth = '1', relheight = '1')

marca = Label(background, text='Software desenvolvido por:\nLucas Eduardo Oliveira Rosa'
				,bg ='#2E8B57', fg = '#000000', font = 'Garamond 8')
marca.place(relx = '0.68', rely = '0.93')

frame_geral = Frame(janela_main, bg = '#87CEFA')
frame_geral.place(relwidth = '0.8', relheight = '0.8',relx = '0.1', rely = '0.1')

label_titulo = Label(background, text = 'Clima e Tempo', font = 'Garamond 30',
					fg = '#FFFAFA', bg = '#87CEEB')
label_titulo.place(rely = '0.01', relx = '0.23')

frame_cidade = Label(frame_geral, bg = '#F5FFFA')
frame_cidade.place(relwidth = '0.95', relheight = '0.1',relx = '0.025', rely = '0.1')

label_cidade = Label(frame_cidade, text = 'Digite a cidade', fg = '#000000', bg = '#F5FFFA', font = 'Garamond')
label_cidade.place(relx = '0.08', rely= '0.15')

label_info = Label(frame_geral, fg = '#000000', bg = '#F5FFFA', font = 'Garamond 20')
label_info.place(relheight ='0.7', relwidth = '0.95', relx = '0.025', rely = '0.25')

entrada_cidade = Entry(frame_cidade, font = 'Garamond')
entrada_cidade.place(relx = '0.5', rely = '0.10', relheight = '0.8', relwidth = '0.3')

bt_ok = Button(frame_cidade, text = 'OK', command = lambda: get_clima(entrada_cidade.get()), font = 'Garamond')
bt_ok.place(relx = '0.83', rely = '0.10', relheight = '0.8', relwidth = '0.15')

bt_exit = Button(background, text = 'SAIR', command = sair, font = 'Garamond')
bt_exit.place(relx = '0.35', rely = '0.915', relheight = '0.08', relwidth = '0.3')

janela_main.mainloop()

