from imports import *
from app import *
from json import *

tela_registra_consumo = customtkinter.CTkFrame(master=app,fg_color='gray',width=720, height=480)

consumoMensal={}
meses = ["01","02","03","04","05","06","07","08","09","10","11","12"]
anos = list(map(str, range(datetime.date.today().year, 2020, -1)))
dropdown_mes = customtkinter.CTkComboBox(master=tela_registra_consumo, values=meses)
dropdown_ano = customtkinter.CTkComboBox(master=tela_registra_consumo, values=anos)
consumo_input = customtkinter.CTkEntry(tela_registra_consumo, placeholder_text="Digite seu consumo:",width=300,height=30,corner_radius=50)

def ler_consumo_mes():
    print(f"Seu consumo no mês {dropdown_mes.get()} de {dropdown_ano.get()} foi {consumo_input.get()}")
    consumoMensal[f'{dropdown_ano.get()}-{dropdown_mes.get()}'] = consumo_input.get()
    consumo_mensal_order = dict(sorted(consumoMensal.items()))
    print(consumo_mensal_order)


def render_registro_consumo():
    tela_registra_consumo.pack()

    label_registra_consumo = customtkinter.CTkLabel(tela_registra_consumo, text="Insira seu consumo de energia e o mês de referência.", font=('Helvetica',24))
    label_registra_consumo.pack(padx=10, pady=10)
    dropdown_mes.pack(pady=10)
    dropdown_ano.pack(pady=10)
    consumo_input.pack(pady=10)

    # Botão Input Consumo
    botao_input = customtkinter.CTkButton(tela_registra_consumo, text="Registrar Consumo",command=ler_consumo_mes)
    botao_input.pack(pady=10)

    # voltarInicio = customtkinter.CTkButton(tela_registra_consumo, text="DESTROY",command=apagar)
    # voltarInicio.pack(pady=10)