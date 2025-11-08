import threading
import time

semaphore = threading.Semaphore(2)  # max 2 threads at a time

def worker(name):
    print(f"{name} trying to enter")
    with semaphore:
        print(f"{name} entered")
        time.sleep(1)
        print(f"{name} leaving")

threads = [threading.Thread(target=worker, args=(f"Thread-{i+1}",)) for i in range(4)]

for t in threads:
    t.start()
for t in threads:
    t.join()
