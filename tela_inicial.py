from imports import *
from app import *
from registro_consumo import *

tela_inicial = customtkinter.CTkFrame(master=app,fg_color='white',width=720, height=480)
   

# def chama_render_mostra_consumo ():
#     render_mostrar_consumo()
#     tela_inicial.pack_forget()

# def render_tela_inicial(chama_render_registro_consumo):
def render_tela_inicial():
    tela_inicial.pack()
    titulo = customtkinter.CTkLabel(master=tela_inicial, text= "Bem-vindo ao Gerenciador de Energia!")
    titulo.pack()