from imports import *
from registro_consumo import *
from tela_inicial import *
from app import app

def inicio_programa():
    render_tela_inicial()

def chama_registro_consumo():
    render_registro_consumo()
    tela_inicial.pack_forget()

def chama_tela_inicial():
    tela_inicial.pack()
    tela_registra_consumo.pack_forget()

botao_chama_registro_consumo = customtkinter.CTkButton(master=tela_inicial,text="Registrar Consumo", command = chama_registro_consumo)
botao_chama_registro_consumo.pack()

botao_voltar_inicio = customtkinter.CTkButton(master=tela_registra_consumo,text="Voltar",command=chama_tela_inicial)
botao_voltar_inicio.pack()
