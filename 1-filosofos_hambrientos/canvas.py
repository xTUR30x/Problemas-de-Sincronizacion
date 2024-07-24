import os, math
from consts import NUM_FILOSOFOS, TEXT
import tkinter as tk
from PIL import Image, ImageTk

class Canvas:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Canvas, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.root = tk.Tk()
        self.philosopher_images = []
        self.radius = 200
        self.center_x = 400
        self.center_y = 300

        self.run()
        
    
    def config(self):
        self.root.title("Problema de los Filósofos") 
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.configure(bg="white")

        # Agregar descripción en la parte inferior de la ventana
        description_label = tk.Label(self.root, text=TEXT, wraplength=300)
        description_label.pack(side=tk.BOTTOM, padx=10, pady=10)


    def load_resources(self):
         # Cargar las imágenes de los filósofos
        self.thinking_image = ImageTk.PhotoImage(Image.open(os.path.join("assets", "thinking.png")))
        self.eating_image = ImageTk.PhotoImage(Image.open(os.path.join("assets", "eating.png")))
        self.resting_image = ImageTk.PhotoImage(Image.open(os.path.join("assets", "resting.png")))

    def draw_canvas(self):
        for i in range(NUM_FILOSOFOS):
            angle = i * 2 * 3.14159 / NUM_FILOSOFOS
            x = self.center_x + self.radius * math.cos(angle)
            y = self.center_y + self.radius * math.sin(angle)
            self.philosopher_images.append(self.canvas.create_image(x, y, image=self.thinking_image))

    def change_philosopher_images(self, index:int, image: str) -> None:
        if image == 'thinking':
            self.canvas.itemconfig(self.philosopher_images[index], image=self.thinking_image)

        if image == 'resting':
            self.canvas.itemconfig(self.philosopher_images[index], image=self.resting_image)

        if image == 'eating':
            self.canvas.itemconfig(self.philosopher_images[index], image=self.eating_image)

    def repeat(self, time: int, function) -> None:
        self.root.after(time, function)

    def start(self):
        self.canvas.pack()
    
    def loop(self):
        self.root.mainloop()

    def run(self):
        self.config()
        self.load_resources()
        self.draw_canvas()