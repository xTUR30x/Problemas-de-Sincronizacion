import time, logging, os
from multiprocessing import Queue, Semaphore, Process
from canvas import Canvas

#Log File
logfile = 'Escritores-Lectores.log'
logging.basicConfig(filename=logfile, level=logging.INFO)

if not os.path.isfile(logfile):
    with open(logfile, "w") as archivo:
        print("archivo creado")


def lector(sem_leer: Semaphore, sem_escribir: Semaphore, queue: Queue) -> None:
    while True:
        sem_leer.acquire()
        print("Leyendo...")
        logging.info("Leyendo...")
        queue.put(("reading", None))
        time.sleep(1)
        sem_leer.release()
        queue.put(("finished_reading", None))

def escritor(sem_leer: Semaphore, sem_escribir: Semaphore, queue: Queue) -> None:
    while True:
        sem_escribir.acquire()
        print("Escribiendo...")
        logging.info("Escribiendo...")
        queue.put(("writing", None))
        time.sleep(1)
        sem_escribir.release()
        queue.put(("finished_writing", None))

def update_gui(canvas: Canvas, reader_image: str, writer_image: str, queue: Queue) -> None:
    try:
        state, _ = queue.get_nowait()
        app_canvas.update_gui(state)
    except:
        pass
    canvas.after(100, update_gui, canvas, reader_image, writer_image, queue)

if __name__ == "__main__":

    #Relacionado con la Interfaz
    app_canvas = Canvas()
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
    update_gui(canvas, app_canvas.reader_image, app_canvas.writer_image, queue)
    app_canvas.loop()

    # Esperar a que los procesos terminen
    p1.join()
    p2.join()
    p3.join()
