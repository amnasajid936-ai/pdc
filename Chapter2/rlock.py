import threading

rlock = threading.RLock()
counter = 0


## same thread can acquire an RLock multiple times without deadlocking.
def nested_lock():
    global counter
    rlock.acquire()
    print("Outer lock acquired")
    rlock.acquire()
    print("Inner lock acquired")
    counter += 1
    rlock.release()
    rlock.release()
    print(f"Counter: {counter}")

## Normally, with a normal Lock, this would cause a deadlock because the same thread cannot acquire the lock twice

t = threading.Thread(target=nested_lock)
t.start()
t.join()

## Shows how a thread can acquire the same lock twice without deadlock.