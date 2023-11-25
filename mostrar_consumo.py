from imports import *
from app import *

tela_mostrar_consumo = customtkinter.CTkFrame(
    master=app,
    fg_color='gray',
    width=720,
    height=480
)

# def comparar_consumos(): # ajustar essa função
    # if (consumo_mensal_ordenado
    #     [
    #         f'{datetime.date.today().year}-{datetime.date.today().month}'
    #     ] 
    #     <= consumo_mensal_ordenado
    #     [
    #         f'{datetime.date.today().year}-{datetime.date.today().month-1}'
    #     ]):
    #     texto_comparacao.configure(text=f"Você economizou R${consumo_mensal_ordenado[f'{datetime.date.today().year}-{datetime.date.today().month-1}']-consumo_mensal_ordenado[{datetime.date.today().year}-{datetime.date.today().month}]:.2f}")
    # else:
    #     texto_comparacao.configure(text=f"Seu consumo aumentou em R${consumo_mensal_ordenado[f'{datetime.date.today().year}-{datetime.date.today().month}']-consumo_mensal_ordenado[f'{datetime.date.today().year}-{datetime.date.today().month-1}']:.2f}")


ano_mes = ''
consumo = ''
diferenca = ''
consumo_mensal_decrescente = dict(sorted(consumo_mensal_ordenado.items(), reverse = True))

i = 0
for chave in consumo_mensal_decrescente.keys():
    ano_mes = ano_mes + list(consumo_mensal_decrescente.keys())[i] + '\n'
    consumo = consumo+ "R$ " + list(consumo_mensal_decrescente.values())[i] + '\n'
    if i+1 != len(list(consumo_mensal_decrescente.keys())):
        diferenca = diferenca + str(round((((float(list(consumo_mensal_decrescente.values())[i])/float(list(consumo_mensal_decrescente.values())[i+1])))*100)-100,2)) + '%' +'\n'
    i+=1
def render_mostrar_consumo():
    titulo = customtkinter.CTkLabel(
        master=tela_mostrar_consumo, 
        text="Acompanhe aqui o seu consumo!", 
        text_color="white",
        font=('Helvetica',25)
    )
    titulo.place(x=250,y=30)

    titulo_periodo = customtkinter.CTkLabel(
        master=tela_mostrar_consumo, 
        text="Ano/Mês", 
        text_color="white",
        font=('Helvetica', 20)
    )
    titulo_periodo.place(x=100,y=180)

    periodo = customtkinter.CTkLabel(
        master=tela_mostrar_consumo, 
        text=ano_mes, 
        text_color="white",
        font=('Helvetica',18)
    )
    periodo.place(x=100,y=200)

    titulo_valor = customtkinter.CTkLabel(
        master=tela_mostrar_consumo, 
        text="Ano/Mês", 
        text_color="white",
        font=('Helvetica', 20)
    )
    titulo_valor.place(x=250,y=180)

    valor = customtkinter.CTkLabel(
        master=tela_mostrar_consumo, 
        text=consumo, 
        text_color="white",
        font=('Helvetica', 18)
    )
    valor.place(x=250,y=200)

    diferenca_consumo = customtkinter.CTkLabel(
        master=tela_mostrar_consumo, 
        text=diferenca, 
        text_color="white",
        font=('Helvetica', 18)
    )
    diferenca_consumo.place(x=400,y=200)