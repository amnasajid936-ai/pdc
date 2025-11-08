import threading
from queue import Queue
import time

# Create a thread-safe queue
queue = Queue()

# Producer function
def producer():
    for i in range(5):
        print(f"Producing item {i}")
        queue.put(i)  # put item in queue
        time.sleep(0.1)  # simulate work

# Consumer function
def consumer():
    while True:
        item = queue.get()  # get item from queue
        print(f"Consumed item {item}")
        queue.task_done()  # mark task as done
        if item == 4:      # exit after last item
            break

# Create threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start threads
producer_thread.start()
consumer_thread.start()

# Wait for both threads to finish
producer_thread.join()
consumer_thread.join()

print("All tasks completed.")
