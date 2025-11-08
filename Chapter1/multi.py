import threading
import multiprocessing
import time
import random


ARRAY_SIZE = 10
NUM_WORKERS = 4           # only 4 threads/processes

#random list
data = [random.randint(1, 100) for _ in range(ARRAY_SIZE)]

# single thread
def normal_sum():
    return sum(data)

# Multithreading
def partial_sum(start, end, result, index):
    result[index] = sum(data[start:end])

def threaded_sum():
    threads = []
    results = [0] * NUM_WORKERS
    chunk = len(data) // NUM_WORKERS
    for i in range(NUM_WORKERS):
        start = i * chunk
        end = (i + 1) * chunk if i != NUM_WORKERS - 1 else len(data)
        t = threading.Thread(target=partial_sum, args=(start, end, results, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return sum(results)

# Multiprocessing
def partial_sum_process(start, end, result_queue):
    result_queue.put(sum(data[start:end]))

def multiprocess_sum():
    processes = []
    result_queue = multiprocessing.Queue()
    chunk = len(data) // NUM_WORKERS
    for i in range(NUM_WORKERS):
        start = i * chunk
        end = (i + 1) * chunk if i != NUM_WORKERS - 1 else len(data)
        p = multiprocessing.Process(target=partial_sum_process, args=(start, end, result_queue))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    return total

# MAIN EXECUTION
if __name__ == "__main__":
    print("Array size:", ARRAY_SIZE)
    print("Workers:", NUM_WORKERS)

    # Single-threaded
    start = time.time()
    result = normal_sum()
    print(f"\nNormal Sum = {result}, Time = {time.time() - start:.4f}s")

    # Multithreading
    start = time.time()
    result = threaded_sum()
    print(f"Multithreading Sum = {result}, Time = {time.time() - start:.4f}s")

    # Multiprocessing
    start = time.time()
    result = multiprocess_sum()
    print(f"Multiprocessing Sum = {result}, Time = {time.time() - start:.4f}s")
