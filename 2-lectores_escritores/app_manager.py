from multiprocessing import Queue, Semaphore, Process
from reader_writter_logic import lector, escritor
from canvas import Canvas

app_canvas = Canvas()

def update_gui(canvas, reader_image: str, writer_image: str, queue: Queue) -> None:
    try:
        state, _ = queue.get_nowait()
        app_canvas.update_gui(state)
    except:
        pass
    canvas.after(100, update_gui, canvas, reader_image, writer_image, queue)

def main():
    #Relacionado con la Interfaz
    canvas = app_canvas.get_canvas()

    # Crear la cola para comunicar los cambios de estado
    queue = Queue()

    # Crear los lectores y escritores
    sem_leer = Semaphore(1)
    sem_escribir = Semaphore(1)
    p1 = Process(target=lector, args=(sem_leer, sem_escribir, queue))
    p2 = Process(target=lector, args=(sem_leer, sem_escribir, queue))
    p3 = Process(target=escritor, args=(sem_leer, sem_escribir, queue))

    # Iniciar los procesos
    p1.start()
    p2.start()
    p3.start()

    # Actualizar la interfaz gráfica
    update_gui(canvas,  app_canvas.reader_image, app_canvas.writer_image, queue)
    app_canvas.loop()

    # Esperar a que los procesos terminen
    p1.join()
    p2.join()
    p3.join()