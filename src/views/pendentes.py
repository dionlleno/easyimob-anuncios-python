import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from tkinter import messagebox as msg
from ttkbootstrap.constants import *

from controllers.cliente import ClienteJson
from controllers.pendencia import PendenciaJson

class PendentesView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.jsonCliente = ClienteJson()
        self.jsonPendencia = PendenciaJson()

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
        self.tree.bind("<Double-1>", self.carregar_popup_listagem_anuncios)

        # --- Bot�es de a��o ---
        botoes_frame = ttk.Frame(self)
        botoes_frame.pack(fill="x", padx=10, pady=10)

        ttk.Button(botoes_frame, text="REMOVER", command=self.remover_pendente, bootstyle="danger").pack(side="left", padx=5)
        ttk.Button(botoes_frame, text="ATUALIZAR", command=self.atualizar_pendentes, bootstyle="secondary").pack(side="left", padx=5)
        ttk.Button(botoes_frame, text="BUSCAR ANUNCIOS", command=self.atualizar_anuncios_pendentes, bootstyle="secondary").pack(side="left", padx=5)

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

    def atualizar_anuncios_pendentes(self):
        pass

    def carregar_popup_listagem_anuncios(self, event) -> None:
        selecionado = self.tree.focus()
        if not selecionado:
            msg.showwarning("ATENCAO", "NENHUM CLIENTE SELECIONADO.")
            return None
        valores = self.tree.item(selecionado, "values")
        id_cliente = int(valores[0])
        print(f"ID CLIENTE SELECIONADO: {id_cliente}")

        pop_up = tk.Toplevel(self)
        pop_up.title("Adicionar Cliente")
        pop_up.geometry("500x500")


        anuncios_frame = tb.LabelFrame(pop_up, text="ANUNCIOS", bootstyle="secondary")
        anuncios_frame.pack(fill="both", padx=5, pady=5, expand=True)

        self.anuncios_tree = ttk.Treeview(anuncios_frame, columns=("id", "titulo", "endereco", "area", "valor", "link"), show="headings", height=8)
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

        #self.anuncios_tree.bind("<Double-1>", abrir_anuncio)

        self.limpar_listagem(self.anuncios_tree)

        anuncios = self.jsonPendencia.listar_anuncios_pendentes(id_cliente=id_cliente)
        if not anuncios:
            msg.showinfo("INFORMACAO", "NENHUM ANUNCIO PENDENTE PARA ESTE CLIENTE.")
            pop_up.destroy()
            return None
        for anuncio in anuncios:
            self.anuncios_tree.insert("", "end", values=(
                anuncio.id_anuncio,
                anuncio.titulo,
                f"{anuncio.bairro} - {anuncio.cidade}/{anuncio.uf}",
                f"{anuncio.area} m²" if anuncio.area else "N/A",
                f"R$ {anuncio.valor_imovel:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if anuncio.valor_imovel else "N/A",
                anuncio.link_anuncio
            ))
        def abrir_anuncio(self, event) -> None:
            selecionado = self.anuncios_tree.focus()
            if not selecionado:
                msg.showwarning("ATENCAO", "NENHUM ANUNCIO SELECIONADO.")
                return None
            valores = self.anuncios_tree.item(selecionado, "values")
            link = valores[5]
            print(f"LINK DO ANUNCIO: {link}")
            import webbrowser
            webbrowser.open(link)

