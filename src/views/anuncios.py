import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class AnunciosView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # --- Título ---
        ttk.Label(self, text="Anúncios", font=("TkDefaultFont", 14, "bold")).pack(anchor="w", padx=10, pady=10)

        # --- Layout principal dividido (esquerda listagem / direita detalhes) ---
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        right_frame = ttk.LabelFrame(main_frame, text="DETALHES", bootstyle="secondary")
        right_frame.pack(side="right", fill="y", padx=5, pady=5)

        # --- FILTROS ---
        filtros_frame = ttk.LabelFrame(left_frame, text="FILTROS", bootstyle="secondary")
        filtros_frame.pack(fill="x", padx=5, pady=5)

        # Criando 3 linhas de filtros (entrada + entrada + checkbox)
        for i in range(3):
            row = ttk.Frame(filtros_frame)
            row.pack(fill="x", pady=2)

            e1 = ttk.Entry(row)
            e1.pack(side="left", fill="x", expand=True, padx=2)

            e2 = ttk.Entry(row)
            e2.pack(side="left", fill="x", expand=True, padx=2)

            c = ttk.Checkbutton(row, bootstyle="round-toggle")
            c.pack(side="right", padx=2)

        # Botão de buscar
        ttk.Button(filtros_frame, text="BUSCAR", bootstyle="secondary").pack(anchor="e", pady=5, padx=5)

        # --- LISTAGEM ---
        listagem_frame = ttk.LabelFrame(left_frame, text="LISTAGEM", bootstyle="secondary")
        listagem_frame.pack(fill="both", expand=True, padx=5, pady=5)

        colunas = ("tipo_imovel", "tipo_aquisicao", "area", "endereco")
        self.tree = ttk.Treeview(listagem_frame, columns=colunas, show="headings", height=10)

        self.tree.heading("tipo_imovel", text="TIPO DE IMOVEL")
        self.tree.heading("tipo_aquisicao", text="TIPO DE AQUISIÇÃO")
        self.tree.heading("area", text="ÁREA")
        self.tree.heading("endereco", text="ENDEREÇO")

        self.tree.pack(fill="both", expand=True)

        # --- DETALHES (lado direito) ---
        fotos_frame = ttk.Frame(right_frame)
        fotos_frame.pack(fill="x", pady=5)

        # Espaços reservados para 3 fotos
        for i in range(3):
            lbl = ttk.Label(fotos_frame, text="FOTO", bootstyle="danger", anchor="center")
            lbl.config(width=20, relief="solid")
            lbl.pack(side="left", expand=True, padx=5, pady=5, ipadx=30, ipady=40)

        # Título + botão
        titulo_frame = ttk.Frame(right_frame)
        titulo_frame.pack(fill="x", pady=5)
        ttk.Label(titulo_frame, text="TITULO:").pack(side="left", anchor="w")
        ttk.Button(titulo_frame, text="ABRIR ANUNCIO", bootstyle="secondary").pack(side="right", padx=5)

        # Informações do imóvel
        info_frame = ttk.Frame(right_frame)
        info_frame.pack(fill="both", expand=True, padx=5, pady=5)

        labels = [
            "TIPO DE IMOVEL:",
            "TIPO DE AQUISIÇÃO:",
            "CIDADE:",
            "ESTADO/UF:",
            "VALOR FINAL:",
            "VALOR IPTU:",
            "VALOR CONDOMINIO:",
            "ÁREA:",
            "QUANT. QUARTOS:",
            "QUANT. BANHEIROS:",
            "QUANT. VAGAS DE GARAGEM:"
        ]

        for text in labels:
            ttk.Label(info_frame, text=text).pack(anchor="w", pady=1)
