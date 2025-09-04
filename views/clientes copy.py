import ttkbootstrap as tb
from tkinter import ttk
from ttkbootstrap.constants import *

from controllers.cliente import ClienteJson
from models.pesquisa import Pesquisa
from utils.extrator_anuncios import ExtratorAnuncios

class ClientesView(tb.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.cliente_json = ClienteJson()
        self.extrator = ExtratorAnuncios()
        self.pesquisa = Pesquisa(None,None,None,None,None,None,None)

        # Divisão em PanedWindow (Lista | Detalhes)
        paned = ttk.PanedWindow(self, orient=HORIZONTAL)
        paned.pack(fill=BOTH, expand=YES)

        # Frame esquerdo (lista + filtros)
        left_frame = tb.Frame(paned)
        paned.add(left_frame, weight=1)

        # Frame direito (detalhes do cliente)
        right_frame = tb.Frame(paned)
        paned.add(right_frame, weight=1)

        # Botoes



        # Filtros
        filtros_frame = tb.Labelframe(left_frame, text="Filtros")
        filtros_frame.pack(fill=X, padx=5, pady=5)

        self.nome_var = tb.StringVar()
        tb.Entry(filtros_frame, textvariable=self.nome_var, width=25).grid(row=0, column=0, padx=5, pady=5)
        tb.Button(filtros_frame, text="Pesquisar", command=self.carregar_clientes).grid(row=0, column=1, padx=5, pady=5)

        self.filtros = {
            "cidade": tb.Combobox(filtros_frame, values=["", "São Paulo", "Rio de Janeiro"], width=15),
            "estado": tb.Combobox(filtros_frame, values=["", "SP", "RJ"], width=10),
            "orcamento": tb.Combobox(filtros_frame, values=["", "Até 200k", "200k-500k", "500k+"], width=15),
            "tipo_imovel": tb.Combobox(filtros_frame, values=["", "Casa", "Apartamento", "Terreno"], width=15),
            "tipo_pagamento": tb.Combobox(filtros_frame, values=["", "À Vista", "Financiamento", "Aluguel"], width=15),
        }

        row = 1
        for key, widget in self.filtros.items():
            widget.grid(row=row, column=0, columnspan=2, padx=5, pady=2, sticky=W)
            row += 1

        # Listagem de clientes
        self.treeL = ttk.Treeview(left_frame, columns=("nome", "tipo_imovel", "tipo_aquisicao", "orcamento"), show="headings")
        self.treeL.heading("nome", text="Nome")
        self.treeL.heading("tipo_imovel", text="Tipo Imovel")
        self.treeL.heading("tipo_aquisicao", text="Tipo Aquisição")
        self.treeL.heading("orcamento", text="Orçamento")
        self.treeL.pack(fill=BOTH, expand=YES, padx=5, pady=5)

        self.treeL.bind("<<TreeviewSelect>>", self.mostrar_detalhes)

        rowC = 1
        for key, widget in self.filtros.items():
            widget.grid(row=rowC, column=0, columnspan=2, padx=5, pady=2, sticky=W)
            rowC += 1

        # Listagem de clientes
        self.treeR = ttk.Treeview(right_frame, columns=("nome", "tipo_imovel", "tipo_aquisicao", "orcamento"), show="headings")
        self.treeR.heading("nome", text="Nome")
        self.treeR.heading("tipo_imovel", text="Tipo Imovel")
        self.treeR.heading("tipo_aquisicao", text="Tipo Aquisição")
        self.treeR.heading("orcamento", text="Orçamento")
        self.treeR.pack(fill=BOTH, expand=YES, padx=5, pady=5)

        self.treeR.bind("<<TreeviewSelect>>", self.mostrar_detalhes)

        # Detalhes
        self.detalhes_label = tb.Label(right_frame, text="Selecione um cliente para ver detalhes", anchor=CENTER)
        self.detalhes_label.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        # Carregar clientes
        self.carregar_clientes()

    def carregar_clientes(self):
        clientes = self.cliente_json.listar_clientes()
        
        # Limpa listagem
        for i in self.treeL.get_children():
            self.treeL.delete(i)

        # Filtragem simples
        nome_filtro = self.nome_var.get().upper()
        for cliente in clientes:
            if nome_filtro and nome_filtro not in cliente.nome:
                continue
            self.treeL.insert("", "end", values=(cliente.nome, cliente.tipo_imovel, cliente.tipo_aquisicao, cliente.orcamento))

    def carregar_anuncios(self, pesquisa: Pesquisa):
        anuncios = self.extrator.extrair_anuncios()
        
        # Limpa listagem
        for i in self.treeL.get_children():
            self.treeL.delete(i)

    def mostrar_detalhes(self, event):
        selected = self.treeL.selection()
        if selected:
            valores = self.treeL.item(selected[0], "values")
            detalhes = f"""
            Nome: {valores[0]}
            Tipo de Imovel: {valores[1]}
            Tipo de Aquisição: {valores[2]}
            Orçamento: {valores[3]}
            """
            self.detalhes_label.config(text=detalhes)
    def atualizar_clientes(self, clientes):
        self.clientes = clientes
