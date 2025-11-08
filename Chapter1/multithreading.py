from do_something import *
import threading
import time

if __name__ == "__main__":
    start_time = time.time()
    size = 10000000
    threads = []
    for i in range(10):
        out_list = []
        t = threading.Thread(target=do_something, args=(size, out_list))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("List processing complete.")
    print("multithreading time =", time.time() - start_time)
