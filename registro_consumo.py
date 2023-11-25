from imports import *
from app import *
from json import *

#Elementos

tela_registra_consumo = customtkinter.CTkFrame(
    master=app,
    fg_color='gray',
    width=720, 
    height=480
)

meses = ["01","02","03","04","05","06","07","08","09","10","11","12"]
anos = list(map(str, range(datetime.date.today().year, 2020, -1)))

dropdown_mes = customtkinter.CTkComboBox(
    master=tela_registra_consumo, 
    values=meses
    )

dropdown_ano = customtkinter.CTkComboBox(
    master=tela_registra_consumo, 
    values=anos
)

consumo_input = customtkinter.CTkEntry(
        master=tela_registra_consumo, 
        placeholder_text="Digite seu consumo:",
        width=300,
        height=30,
        corner_radius=50
    )

consumoMensal={}


def ler_consumo_mes():
    print(f"Seu consumo no mês {dropdown_mes.get()} de {dropdown_ano.get()} foi {consumo_input.get()}")
    consumoMensal[f'{dropdown_ano.get()}-{dropdown_mes.get()}'] = consumo_input.get()
    consumo_mensal_order = dict(sorted(consumoMensal.items()))
    print(consumo_mensal_order)


def render_registro_consumo():
    dropdown_mes.place(x=180,y=100)
    dropdown_ano.place(x=380,y=100)
    consumo_input.place(x=210,y=200)

    label_registra_consumo = customtkinter.CTkLabel(
        tela_registra_consumo, 
        text="Insira seu consumo de energia e o mês de referência.", 
        text_color="white",
        font=('Helvetica',24)
    )
    label_registra_consumo.place(x=100,y=20)

    botao_input = customtkinter.CTkButton(
        master=tela_registra_consumo, 
        text="Registrar Consumo",
        command=ler_consumo_mes
    )
    botao_input.place(x=260,y=300)
