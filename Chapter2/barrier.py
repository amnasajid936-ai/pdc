import threading
import time

barrier = threading.Barrier(3)  # 3 threads must wait

def worker(name):
    print(f"{name} waiting at barrier")
    time.sleep(1)
    barrier.wait()  # wait until all threads reach here
    print(f"{name} passed the barrier")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


## Output: Threads wait until all 3 reach the barrier, then continue together.