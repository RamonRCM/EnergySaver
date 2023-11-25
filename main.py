from imports import *
from registro_consumo import *
from tela_inicial import *
from app import app


# Funções



# def chama_render_registro_consumo():
#     render_registro_consumo(chama_render_tela_inicial)
#     tela_inicial.pack_forget() # foi para tela_inicial

# def chama_render_tela_inicial():
#     render_tela_inicial(chama_render_registro_consumo)
#     tela_registra_consumo.pack_forget() # foi para tela registro consumo


render_tela_inicial()

app.mainloop()
