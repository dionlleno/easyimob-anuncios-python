import ttkbootstrap as tb
from tkinter import Frame, Label

class AnunciosView(Frame):
    def __init__(self, master):
        super().__init__(master)

        Label(self, text="Aqui vai a aba de Anúncios", font=("Arial", 14)).pack(pady=20)

        # Exemplo: Botão de ação
        btn = tb.Button(self, text="Cadastrar Anúncio", bootstyle="info")
        btn.pack(pady=10)
