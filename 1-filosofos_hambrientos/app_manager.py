from canvas import Canvas
from logger import Logger
from consts import *
from philosophers_logic import philosopher
from multiprocessing import Process, Semaphore, Lock, Queue

def main(app_canvas) -> None:

    # Crea una lista de bloqueos simulando los tenedores
    forks = [Lock() for _ in range(NUM_FILOSOFOS)]
    
    # Inicia la aplicacion
    app_canvas.start()

    # Crear una cola para comunicar los cambios de estado
    queue = Queue()

    # Creando los filósofos y ejecutando la lógica del problema
    philosophers = [Process(target=philosopher, args=(i, forks, queue)) for i in range(NUM_FILOSOFOS)]

    # Ejecutando los filósofos de manera simultánea
    for p in philosophers:
        p.start()

    # Actualizar la interfaz gráfica con los cambios de estado
    def update_gui():
        while True:
            try:
                state, index = queue.get_nowait()
                if state == "thinking":
                    app_canvas.change_philosopher_images(index, 'thinking')
                elif state == "eating":
                    app_canvas.change_philosopher_images(index, 'eating')
                elif state == "resting":
                    app_canvas.change_philosopher_images(index, 'resting')
            except:
                break
        app_canvas.repeat(100, update_gui)

    update_gui()
    app_canvas.loop()

    # Esperando que todos los procesos concluyan
    for p in philosophers:
        p.join()