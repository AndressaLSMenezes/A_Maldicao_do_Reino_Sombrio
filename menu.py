import tkinter as tk
from dino_runner.components.game import Game

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("A Maldição do Reino Sombrio: A Saga do Cálice da Luz")
        master.geometry("1100x600")

        # Carrega a imagem de fundo
        self.background_image = tk.PhotoImage(file="dino_runner/assets/Buttons/fundo.png")
        
        # Cria um canvas com a mesma dimensão da janela
        # Canvas fornece uma área gráfica
        self.canvas = tk.Canvas(master, width=1100, height=600)
        self.canvas.pack()
        
        # Adiciona a imagem de fundo ao canvas
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        
        # Adiciona os widgets (botões) no topo do canvas
        self.button_frame = tk.Frame(self.canvas, bd=0)
        self.button_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.image_play = tk.PhotoImage(file="dino_runner/assets/Buttons/play.png").subsample(2, 2)
        self.image_button_play = tk.Button(self.button_frame, image=self.image_play, command=self.person_1, borderwidth=0, highlightthickness=0)
        self.image_button_play.pack(pady=0)
        
        self.image_exit = tk.PhotoImage(file="dino_runner/assets/Buttons/exit.png").subsample(2, 2)
        self.image_button_exit = tk.Button(self.button_frame, image=self.image_exit, command=self.exit, borderwidth=0, highlightthickness=0)
        self.image_button_exit.pack(pady=0)


    def person_1(self):
        root.destroy()
        game = Game()
        game.execute()
        
    def exit(self):
        root.destroy() #destroy window

root = tk.Tk()
app = Menu(root)
root.mainloop()