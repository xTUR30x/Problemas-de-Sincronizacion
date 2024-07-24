import os
import tkinter as tk
from PIL import Image, ImageTk

# Imágenes
READER_IMAGE = os.path.join("assets", "reader.png")
WRITER_IMAGE = os.path.join("assets", "writer.png")
SLEEP_IMAGE = os.path.join("assets", "sleep.png")

class Canvas:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Problema del Lector-Escritor")

        # Cargar las imágenes
        self.reader_img = ImageTk.PhotoImage(Image.open(READER_IMAGE))
        self.writer_img = ImageTk.PhotoImage(Image.open(WRITER_IMAGE))
        self.sleep_img = ImageTk.PhotoImage(Image.open(SLEEP_IMAGE))

        # Mantener una referencia a los objetos PhotoImage
        self.image_refs = [self.reader_img, self.writer_img, self.sleep_img]

        # Crear el canvas y las imágenes
        self.canvas = tk.Canvas(self.root, width=400, height=200)
        self.canvas.pack()
        self.reader_image = self.canvas.create_image(100, 100, image=self.reader_img)
        self.writer_image = self.canvas.create_image(300, 100, image=self.sleep_img)

    def get_canvas(self):
        return self.canvas

    def update_gui(self, state):
        if state == "reading":
            self.canvas.itemconfig(self.reader_image, image=self.reader_img)
            self.canvas.itemconfig(self.writer_image, image=self.sleep_img)
        elif state == "finished_reading":
            self.canvas.itemconfig(self.reader_image, image=self.sleep_img)
        elif state == "writing":
            self.canvas.itemconfig(self.writer_image, image=self.writer_img)
            self.canvas.itemconfig(self.reader_image, image=self.sleep_img)
        elif state == "finished_writing":
            self.canvas.itemconfig(self.writer_image, image=self.sleep_img)

    def loop(self):
        self.root.mainloop()
        # Eliminar las referencias a los objetos PhotoImage
        self.image_refs = None

def lector(sem_leer, sem_escribir, queue):
    while True:
        sem_leer.acquire()
        print("Leyendo...")
        queue.put(("reading", None))
        time.sleep(1)
        sem_leer.release()
        queue.put(("finished_reading", None))

def escritor(sem_leer, sem_escribir, queue):
    while True:
        sem_escribir.acquire()
        print("Escribiendo...")
        queue.put(("writing", None))
        time.sleep(1)
        sem_escribir.release()
        queue.put(("finished_writing", None))

def update_gui(canvas, reader_image, writer_image, queue):
    try:
        state, _ = queue.get_nowait()
        app_canvas.update_gui(state)
    except:
        pass
    canvas.after(100, update_gui, canvas, reader_image, writer_image, queue)

if __name__ == "__main__":
    app_canvas = Canvas()
    canvas = app_canvas.get_canvas()

    # Crear la cola para comunicar los cambios de estado
    queue = multiprocessing.Queue()

    # Crear los lectores y escritores
    sem_leer = multiprocessing.Semaphore(1)
    sem_escribir = multiprocessing.Semaphore(1)
    p1 = multiprocessing.Process(target=lector, args=(sem_leer, sem_escribir, queue))
    p2 = multiprocessing.Process(target=lector, args=(sem_leer, sem_escribir, queue))
    p3 = multiprocessing.Process(target=escritor, args=(sem_leer, sem_escribir, queue))

    # Iniciar los procesos
    p1.start()
    p2.start()
    p3.start()

    # Actualizar la interfaz gráfica
    update_gui(canvas, app_canvas.reader_image, app_canvas.writer_image, queue)
    app_canvas.loop()

    # Esperar a que los procesos terminen
    p1.join()
    p2.join()
    p3.join()
