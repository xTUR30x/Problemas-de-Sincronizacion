import time, logging
from multiprocessing import Queue, Semaphore, Process
from logger import Logger

log = Logger('lectores_escritores.log', 'info')

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