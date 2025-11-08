import threading
import time

# Shared resource
counter = 0
lock = threading.Lock()

# Worker function
def increment(name):
    global counter
    for _ in range(5):
        time.sleep(0.1)  # simulate work
        lock.acquire()   # acquire the lock
        counter += 1
        print(f"{name} incremented counter to {counter}")
        lock.release()   # release the lock

# Create threads
thread1 = threading.Thread(target=increment, args=("Thread-1",))
thread2 = threading.Thread(target=increment, args=("Thread-2",))

# Start threads
thread1.start()
thread2.start()

# Wait for both to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")
