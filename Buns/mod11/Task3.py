import random
import threading
import time
import logging

TOTAL_TICKETS = 10

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Seller(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                logger.info(f'{self.getName()} sold one; {TOTAL_TICKETS} left')

        logger.info(f'Seller {self.getName()} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))

class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_printed = 0
        logger.info('Director started work')

    def run(self):
        global TOTAL_TICKETS
        while True:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 3:
                    self.print_tickets()
                    if TOTAL_TICKETS >= 10:
                        break

    def print_tickets(self):
        global TOTAL_TICKETS
        new_tickets = random.randint(4, 10)
        TOTAL_TICKETS += new_tickets
        self.tickets_printed += new_tickets
        logger.info(f'Director printed {new_tickets} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 2))

def main():
    semaphore = threading.Semaphore()
    sellers = []
    director = Director(semaphore)

    for _ in range(3):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    director.start()

    for seller in sellers:
        seller.join()

    director.join()

if __name__ == '__main__':
    main()
