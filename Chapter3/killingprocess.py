from multiprocessing import Process
import time

def worker():
    while True:
        print("Working...")
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=worker)
    p.start()
    time.sleep(3)
    p.terminate()  # Kill the process
    print("Process terminated")
