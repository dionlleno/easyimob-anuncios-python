import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class PendentesView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # --- T�tulo ---
        ttk.Label(self, text="Pend�ncias", font=("TkDefaultFont", 14, "bold")).pack(anchor="w", padx=10, pady=10)

        # --- Tabela de pend�ncias ---
        colunas = ("tipo", "descricao", "status")
        self.tree = ttk.Treeview(self, columns=colunas, show="headings", height=15)

        self.tree.heading("tipo", text="TIPO")
        self.tree.heading("descricao", text="DESCRI��O")
        self.tree.heading("status", text="STATUS")

        self.tree.column("tipo", width=150, anchor="center")
        self.tree.column("descricao", width=500, anchor="w")
        self.tree.column("status", width=150, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        # --- Bot�es de a��o ---
        botoes_frame = ttk.Frame(self)
        botoes_frame.pack(fill="x", padx=10, pady=10)

        ttk.Button(botoes_frame, text="MARCAR CONCLU�DO", bootstyle="success").pack(side="left", padx=5)
        ttk.Button(botoes_frame, text="REMOVER", bootstyle="danger").pack(side="left", padx=5)
        ttk.Button(botoes_frame, text="ATUALIZAR", bootstyle="secondary").pack(side="left", padx=5)
