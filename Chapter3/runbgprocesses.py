from multiprocessing import Process
import time

def worker():
    while True:
        print("Background work...")
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=worker)
    p.daemon = True
    p.start()
    time.sleep(3)
    print("Main process exits, process stops")
