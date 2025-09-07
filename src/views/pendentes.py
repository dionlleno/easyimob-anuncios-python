import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from tkinter import messagebox as msg
from ttkbootstrap.constants import *

from controllers.cliente import ClienteJson

class PendentesView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.jsonCliente = ClienteJson()

        # --- T�tulo ---
        ttk.Label(self, text="Pend�ncias", font=("TkDefaultFont", 14, "bold")).pack(anchor="w", padx=10, pady=10)

        # --- Tabela de pend�ncias ---

        colunas = ("id", "nome", "tipo_imovel", "tipo_aquisicao", "uf_desejada", "orcamento")
        self.tree = ttk.Treeview(self, columns=colunas, show="headings", height=12)

        self.tree.heading("nome", text="NOME")
        self.tree.heading("tipo_imovel", text="TIPO DE IMOVEL")
        self.tree.heading("tipo_aquisicao", text="TIPO DE AQUISICAO")
        self.tree.heading("uf_desejada", text="UF DESEJADA")
        self.tree.heading("orcamento", text="ORCAMENTO")

        self.tree.column("id", width=0, stretch=False)
        self.tree.column("nome")
        self.tree.column("orcamento", width=20, anchor="center")
        self.tree.column("uf_desejada", width=20, anchor="center")
        self.tree.column("tipo_imovel", width=30, anchor="center")
        self.tree.column("tipo_aquisicao", width=30, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=5, pady=5)
        #self.tree.bind("<<TreeviewSelect>>", self.carregar_cliente_pendente)

        # --- Bot�es de a��o ---
        botoes_frame = ttk.Frame(self)
        botoes_frame.pack(fill="x", padx=10, pady=10)

        ttk.Button(botoes_frame, text="REMOVER", command=self.remover_pendente, bootstyle="danger").pack(side="left", padx=5)
        ttk.Button(botoes_frame, text="ATUALIZAR", command=self.atualizar_pendentes, bootstyle="secondary").pack(side="left", padx=5)

        self.carregar_clientes_pendentes()
    
    def limpar_listagem(self, itens) -> None:
        for item in itens.get_children():
            itens.delete(item)
    
    def carregar_clientes_pendentes(self):
        self.limpar_listagem(self.tree)
        for cliente in self.jsonCliente.listar_clientes_pendentes():
            self.tree.insert("", "end", values=(
                cliente.id_cliente,
                cliente.nome,
                cliente.tipo_imovel,
                cliente.tipo_aquisicao,
                cliente.uf_desejado,
                f"R$ {cliente.orcamento:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            ))
    
    def atualizar_pendentes(self):
        self.carregar_clientes_pendentes()

    def remover_pendente(self) -> None:
        selecionado = self.tree.focus()
        if selecionado:
            valores = self.tree.item(selecionado, "values")
            print(valores)
            self.jsonCliente.marcar_pendente(id_cliente=int(valores[0]), pendente=False)
            self.carregar_clientes_pendentes()
        else:
            msg.showwarning("ATENCAO", "NENHUM CLIENTE SELECIONADO.")

    def exibir_cliente_pendente(self):
        pass