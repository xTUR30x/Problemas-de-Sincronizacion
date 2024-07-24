from time import sleep, perf_counter
from multiprocessing import Lock, Process, Queue
from consts import *
from logger import Logger

log = Logger('philosophers.log', 'info')

# Código del problema
def philosopher(index: int, forks: list[Lock], queue: Queue) -> None:
    start_time = perf_counter()

    while perf_counter() - start_time < TEIMPO_EJECUCION:
        # Pensando
        print(f"El filosofo #{index} esta pensado\n")
        logging.info(f"El filosofo #{index} esta pensado\n")
        queue.put(("thinking", index))
        sleep(TIEMPO_PENSANDO)  # Simulando que piensa

        # Tomando los tenedores
        with forks[index], forks[(index + 1) % NUM_FILOSOFOS]:
            # Comer
            print(f"Filósofo {index} está comiendo\n")
            logging.info(f"Filósofo {index} está comiendo\n")
            queue.put(("eating", index))
            sleep(TIEMPO_COMIENDO)

            # Descansando
            print(f"El filosofo #{index} termino de comer \n")
            logging.info(f"El filosofo #{index} termino de comer \n")
            queue.put(("resting", index))