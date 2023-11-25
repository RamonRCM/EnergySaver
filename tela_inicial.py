from imports import *
from app import *
from registro_consumo import *


tela_inicial = customtkinter.CTkFrame(master=app,fg_color='gray',width=720, height=480)



def render_tela_inicial():

    titulo = customtkinter.CTkLabel(
        master=tela_inicial, 
        text="Bem-vindo ao Gerenciador de Energia!",
        #fg_color="gray",
        text_color="white",
        font=('Helvetica',24)
    )
    titulo.place(x=170,y=20)


    referencia = customtkinter.CTkLabel(
        master=tela_inicial, 
        text= "Desenvolvido por:\nRamon Costa Marques | RU:4105980\nGiovanni Gomes do Prado Júnior | RU:4106394",
        text_color="black",
        font=('Helvetica',15)
    )
    referencia.place(x=190,y=400)

