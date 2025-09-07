import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from controllers.cliente import ClienteJson
from models.pesquisa import Pesquisa
from utils.extrator_anuncios import ExtratorAnuncios
from views.clientes import ClientesView
from views.anuncios import AnunciosView
from views.pendentes import PendentesView
from views.ajustes import AjustesView

class App(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("Sistema de CRM")
        self.geometry("1200x700")

        # Notebook (abas)
        notebook = tb.Notebook(self, bootstyle="primary")
        notebook.pack(fill="both", expand=True)

        # Abas
        clientes_tab = ClientesView(notebook)
        anuncios_tab = AnunciosView(notebook)
        pendentes_tab = PendentesView(notebook)  # ✅ Nova aba
        ajustes_tab = AjustesView(notebook)

        notebook.add(clientes_tab, text="CLIENTES")
        notebook.add(anuncios_tab, text="ANUNCIOS")
        notebook.add(pendentes_tab, text="PENDENTES")  # ✅ Adicionada
        notebook.add(ajustes_tab, text="AJUSTES")

if __name__ == "__main__":
    jsonCliente = ClienteJson()
    extrator = ExtratorAnuncios()
    clientes_pendentes = jsonCliente.listar_clientes_pendentes()
    for cliente in clientes_pendentes:
        print(f"Cliente Pendente: {cliente.nome} - {cliente.email}")
        pesquisa = Pesquisa(
            tipo_busca = cliente.tipo_aquisicao.lower(),
            quant_paginas=5,
            uf=cliente.uf_desejado,
            orcamento_max=cliente.orcamento,
            quant_vagas=cliente.quant_vagas,
            quant_banheiros=cliente.quant_banheiros,
            quant_quartos=cliente.quant_quartos
        )
        anuncios = extrator.extrair_anuncios(pesquisa=pesquisa)
    app = App()
    app.mainloop()
