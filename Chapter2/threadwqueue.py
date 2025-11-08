import threading
from queue import Queue
import time

queue = Queue()

# Producer
def producer():
    for i in range(5):
        print(f"Producing {i}")
        queue.put(i)
        time.sleep(0.1)

# Consumer
def consumer():
    while True:
        item = queue.get()
        print(f"Consumed {item}")
        queue.task_done()
        if item == 4:  # last item
            break

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()

## Shows safe communication between threads using a queue.