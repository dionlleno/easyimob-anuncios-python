import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from models.anuncio import Anuncio
from utils.extrator_anuncios import ExtratorAnuncios

class AnunciosView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.extrator = ExtratorAnuncios()

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

        self.anuncios_tree = ttk.Treeview(listagem_frame, columns=("id", "titulo", "endereco", "area", "valor", "link"), show="headings", height=8)
        self.anuncios_tree.heading("titulo", text="TITULO")
        self.anuncios_tree.heading("valor", text="VALOR")
        self.anuncios_tree.heading("endereco", text="ENDERECO")
        self.anuncios_tree.heading("area", text="AREA")
        self.anuncios_tree.pack(fill="both", expand=True)
        
        self.anuncios_tree.column("id", width=0, stretch=False)
        self.anuncios_tree.column("link", width=0, stretch=False)
        self.anuncios_tree.column("titulo", width=400, anchor="w", stretch=True)
        self.anuncios_tree.column("endereco", width=200, anchor="center")
        self.anuncios_tree.column("area", width=20, anchor="center")
        self.anuncios_tree.column("valor", width=20, anchor="center")

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

    def limpar_listagem(self, tree) -> None:
        for item in tree.get_children():
            self.anuncios_tree.delete(item)
    
    def carregar_anuncios(self, anuncios) -> None:
        self.limpar_listagem(self.anuncios_tree)
        
        anuncios: list[Anuncio]= self.extrator.extrair_anuncios()
        for anuncio in anuncios:
            self.anuncios_tree.insert("", "end", values=(
                anuncio.id_anuncio,
                anuncio.titulo,
                anuncio.endereco,
                anuncio.area,
                f"R$ {anuncio.valor},
                
            ))
