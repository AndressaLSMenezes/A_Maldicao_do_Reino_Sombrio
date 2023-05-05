import tkinter as tk
import Game


class Menu:
    def __init__(self, master):
        self.master = master
        master.title("Minha aplicação")
        master.geometry("1100x600")

        # Carrega a imagem de fundo
        self.background_image = tk.PhotoImage(file="fundo-novo.png")
        
        # Cria um canvas com a mesma dimensão da janela
        self.canvas = tk.Canvas(master, width=1100, height=600)
        self.canvas.pack()
        
        # Adiciona a imagem de fundo ao canvas
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        
        # Adiciona os widgets (botões) no topo do canvas
        self.button_frame = tk.Frame(self.canvas, bd=0)
        self.button_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.image_play = tk.PhotoImage(file="eleonor (1).png").subsample(2, 2)
        self.image_button_play = tk.Button(self.button_frame, image=self.image_play, command=self.person_1, borderwidth=0, highlightthickness=0)
        self.image_button_play.pack(pady=0)
        
        
        self.image_credits = tk.PhotoImage(file="novo legolas.png").subsample(2, 2)
        self.image_button_credits = tk.Button(self.button_frame, image=self.image_credits, command=self.person_2, borderwidth=0, highlightthickness=0)
        self.image_button_credits.pack(pady=0)
        
        self.image_exit = tk.PhotoImage(file="2.png").subsample(2, 2)
        self.image_button_exit = tk.Button(self.button_frame, image=self.image_exit, command=self.exit, borderwidth=0, highlightthickness=0)
        self.image_button_exit.pack(pady=0)


    def person_1(self):
        print("Eleonor")
        pass
    
    def person_2(self):
        print("Legolas")
        
    
    def exit(self):
        root.destroy() #destroy window
        print("Sair")
        
        

root = tk.Tk()
app = Menu(root)
root.mainloop()