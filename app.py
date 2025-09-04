import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
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
    app = App()
    app.mainloop()
