import queue
import threading
import time
import random

class Task:
    def __init__(self, priority):
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class Producer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(10):
            priority = random.randint(0, 6)
            task = Task(priority)
            self.queue.put((task.priority, task))
        print("Producer: Done")

class Consumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            priority, task = self.queue.get()
            if task is None: # Проверка на сигнальное значение
                self.queue.task_done()
                break
            print(f"Consumer: Running\n> running Task(priority={task.priority}).")
            time.sleep(random.random())
            self.queue.task_done()
        print("Consumer: Done")

def main():
    q = queue.PriorityQueue()

    producer = Producer(q)
    consumer = Consumer(q)

    producer.start()
    consumer.start()

    q.join()

    q.put((999, None))
    q.join()

if __name__ == "__main__":
    main()
