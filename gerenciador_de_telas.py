from imports import *
from registro_consumo import *
from tela_inicial import *
from app import app

#Funções

def inicio_programa():
    render_tela_inicial()
    render_registro_consumo()
    tela_inicial.pack()

def chama_registro_consumo():
    tela_registra_consumo.pack()
    tela_inicial.pack_forget()

def chama_tela_inicial():
    tela_inicial.pack()
    tela_registra_consumo.pack_forget()

#Botões

#Botões Tela Inicial

botao_chama_registro_consumo = customtkinter.CTkButton(
    master=tela_inicial,
    text="Registrar Consumo\nde energia",
    command = chama_registro_consumo
)
botao_chama_registro_consumo.place(x=25,y=230)

botao_chama_registro_consumo = customtkinter.CTkButton(
    master=tela_inicial,
    text="Comparar Consumo\nmês a mês", 
    command = chama_registro_consumo
)
botao_chama_registro_consumo.place(x=205,y=230)

botao_chama_registro_consumo = customtkinter.CTkButton(
    master=tela_inicial,
    text="Vou falar com\nmeu amigo", 
    command = chama_registro_consumo
)
botao_chama_registro_consumo.place(x=385,y=230)

botao_chama_registro_consumo = customtkinter.CTkButton(
    master=tela_inicial,
    text="Ele é um\ncara legal", 
    command = chama_registro_consumo
    )
botao_chama_registro_consumo.place(x=565,y=230)

#Botões Voltar para Tela Inicial

botao_voltar_inicio = customtkinter.CTkButton(master=tela_registra_consumo,text="Voltar",command=chama_tela_inicial)
botao_voltar_inicio.place(x=1,y=450)
