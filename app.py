from imports import *




registro = openpyxl.load_workbook(filename='registro.xlsx')
planilha = registro.active
planilha['a1'] = 'ANO-MES'
planilha['b1'] = 'CONSUMO(R$)'

consumo_mensal={}
consumo_mensal_ordenado={}

for linha in range(2, planilha.max_row + 1):
  key = planilha.cell(linha, 1).value
  value = planilha.cell(linha, 2).value
  consumo_mensal[key] = value


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Energy Saver alpha")
