import tkinter as tk
from tkinter import ttk
from models.pesquisa import Pesquisa
from tkinter import messagebox as msg
from controllers.filtros import FiltrosJson
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from models.anuncio import Anuncio
from utils.extrator_anuncios import ExtratorAnuncios

class AnunciosView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.extrator = ExtratorAnuncios()

        self.jsonFiltros = FiltrosJson()

        self.tipo_busca_var = tk.StringVar(value="aluguel")

        self.uf_var = tk.StringVar(value="TODOS")
        self.quant_paginas_var = tk.IntVar(value=5)
        self.orcamento_max_var = tk.StringVar(value="")
        self.quant_vagas_var = tk.IntVar(value=0)
        self.quant_quartos_var = tk.IntVar(value=0)
        self.quant_banheiros_var = tk.IntVar(value=0)

        ttk.Label(self, text="Anúncios", font=("TkDefaultFont", 14, "bold")).pack(anchor="w", padx=10, pady=10)

        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True)

        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        right_frame = ttk.LabelFrame(main_frame, text="DETALHES", bootstyle="secondary")
        right_frame.pack(side="right", fill="y", padx=5, pady=5)

        filtros_frame = ttk.LabelFrame(left_frame, text="FILTROS", bootstyle="secondary")
        filtros_frame.pack(fill="x", padx=5, pady=5)

        tipo_busca_frame = ttk.Frame(filtros_frame)
        tipo_busca_frame.pack(fill="x", pady=5)
        ttk.Label(tipo_busca_frame, text="TIPO DE BUSCA:").pack(side="left", padx=5)
        ttk.Radiobutton(tipo_busca_frame, text="ALUGUEL", variable=self.tipo_busca_var, value="aluguel", bootstyle="secondary").pack(side="left", padx=5)
        ttk.Radiobutton(tipo_busca_frame, text="VENDA", variable=self.tipo_busca_var, value="venda", bootstyle="secondary").pack(side="left", padx=5)
        ttk.Radiobutton(tipo_busca_frame, text="IMOVEL NOVO", variable=self.tipo_busca_var, value="lancamentos", bootstyle="secondary").pack(side="left", padx=5)
        ttk.Radiobutton(tipo_busca_frame, text="COMERCIAL E INDUSTRIAL", variable=self.tipo_busca_var, value="comercio-e-industria", bootstyle="secondary").pack(side="left", padx=5)
        ttk.Radiobutton(tipo_busca_frame, text="TERRENOS", variable=self.tipo_busca_var, value="terrenos", bootstyle="secondary").pack(side="left", padx=5) 

        ttk.Label(filtros_frame, text="UF:").pack(anchor="w", padx=5)
        uf_options = ["TODOS"] + self.jsonFiltros.listar_estados()
        uf_dropdown = ttk.Combobox(filtros_frame, textvariable=self.uf_var, values=uf_options, state="readonly")
        uf_dropdown.pack(fill="x", padx=5, pady=5)
        uf_dropdown.current(0)

        ttk.Label(filtros_frame, text="CIDADES:").pack(anchor="w", padx=5)
        cidades_options = ["TODOS"] + self.jsonFiltros.listar_cidades(self.uf_var.get())
        self.cidades_dropdown = ttk.Combobox(filtros_frame, state="disabled", values=cidades_options, textvariable=tk.StringVar(value="TODOS"))
        self.cidades_dropdown.pack(fill="x", padx=5, pady=5)
        self.cidades_dropdown.current(0)    
        def atualizar_cidades(event):
            cidades_options = ["TODOS"] + self.jsonFiltros.listar_cidades(self.uf_var.get())
            self.cidades_dropdown.config(values=cidades_options, state="readonly",textvariable=tk.StringVar(value="TODOS"))
            self.cidades_dropdown.current(0)
        uf_dropdown.bind("<<ComboboxSelected>>", atualizar_cidades)

        ttk.Label(filtros_frame, text="QUANTIDADE DE PÁGINAS:").pack(anchor="w", padx=5)
        quant_paginas_spinbox = ttk.Spinbox(filtros_frame, from_=1, to=20, textvariable=self.quant_paginas_var, bootstyle="secondary")
        quant_paginas_spinbox.pack(fill="x", padx=5, pady=5)

        ttk.Label(filtros_frame, text="ORÇAMENTO MÁXIMO:").pack(anchor="w", padx=5)
        orcamento_max_entry = ttk.Entry(filtros_frame, textvariable=self.orcamento_max_var, bootstyle="secondary")
        orcamento_max_entry.pack(fill="x", padx=5, pady=5)

        ttk.Label(filtros_frame, text="QUANTIDADE DE VAGAS:").pack(anchor="w", padx=5)
        quant_vagas_spinbox = ttk.Spinbox(filtros_frame, from_=0, to=10, textvariable=self.quant_vagas_var, bootstyle="secondary")
        quant_vagas_spinbox.pack(fill="x", padx=5, pady=5)

        ttk.Label(filtros_frame, text="QUANTIDADE DE QUARTOS:").pack(anchor="w", padx=5)
        quant_quartos_spinbox = ttk.Spinbox(filtros_frame, from_=0, to=10, textvariable=self.quant_quartos_var, bootstyle="secondary")
        quant_quartos_spinbox.pack(fill="x", padx=5, pady=5)

        ttk.Label(filtros_frame, text="QUANTIDADE DE BANHEIROS:").pack(anchor="w", padx=5)
        quant_banheiros_spinbox = ttk.Spinbox(filtros_frame, from_=0, to=10, textvariable=self.quant_banheiros_var, bootstyle="secondary")
        quant_banheiros_spinbox.pack(fill="x", padx=5, pady=5)

        ttk.Button(filtros_frame, text="BUSCAR", bootstyle="secondary", command=self.bt_buscar).pack(anchor="e", pady=5, padx=5)


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


        fotos_frame = ttk.Frame(right_frame)
        fotos_frame.pack(fill="x", pady=5)

        for i in range(3):
            lbl = ttk.Label(fotos_frame, text="FOTO", bootstyle="danger", anchor="center")
            lbl.config(width=20, relief="solid")
            lbl.pack(side="left", expand=True, padx=5, pady=5, ipadx=30, ipady=40)

        titulo_frame = ttk.Frame(right_frame)
        titulo_frame.pack(fill="x", pady=5)
        ttk.Label(titulo_frame, text="TITULO:").pack(side="left", anchor="w")
        ttk.Button(titulo_frame, text="ABRIR ANUNCIO", bootstyle="secondary").pack(side="right", padx=5)

        info_frame = ttk.Frame(right_frame)
        info_frame.pack(fill="both", expand=True, padx=5, pady=5)

    def bt_buscar(self):
        pesquisa=Pesquisa(
            tipo_busca=self.tipo_busca_var.get().lower(),
            quant_paginas=self.quant_paginas_var.get(),
            uf=self.uf_var.get().lower() if self.uf_var.get().lower() != "" else None,
            orcamento_max=int(self.orcamento_max_var.get().replace("R$ ", "").replace(".", "").replace(",", "")) if self.orcamento_max_var.get() != "" else None,
            quant_vagas=self.quant_vagas_var.get() if self.quant_vagas_var.get() != 0 else None,
            quant_quartos=self.quant_quartos_var.get() if self.quant_quartos_var.get() != 0 else None,
            quant_banheiros=self.quant_banheiros_var.get() if self.quant_banheiros_var.get() != 0 else None
        )
        msg.showinfo("INFO", "Buscando anúncios, isso pode levar alguns minutos dependendo da quantidade de páginas selecionadas. Continuar?")
        anuncios = self.extrator.extrair_anuncios(pesquisa)
        a = []
        for anuncio in anuncios:
            if self.cidades_dropdown.get() == "TODOS":
                a = anuncios
                break
            elif anuncio.cidade.upper() == self.cidades_dropdown.get().upper():
                a.append(anuncio)
        self.carregar_anuncios(a)

    def limpar_listagem(self, tree) -> None:
        for item in tree.get_children():
            self.anuncios_tree.delete(item)
    
    def carregar_anuncios(self, anuncios: list[Anuncio]) -> None:
        self.limpar_listagem(self.anuncios_tree)

        msg.showinfo("INFO", f"{len(anuncios)} anúncios encontrados.")

        for anuncio in anuncios:
            self.anuncios_tree.insert("", "end", values=(
                anuncio.id_anuncio,
                anuncio.titulo,
                f"{anuncio.uf} - {anuncio.cidade}",
                f"{anuncio.area} m²",
                f"R$ {anuncio.valor_imovel}",
                anuncio.link_anuncio
            ))
