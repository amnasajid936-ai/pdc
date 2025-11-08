# Python Threading Examples

This project contains multiple Python scripts demonstrating **different threading concepts** using the `threading` module in Python. Each script illustrates a specific synchronization mechanism or threading technique.

## Scripts Overview

| Script | Concept | Description |
|--------|---------|-------------|
| `Barrier.py` | Barrier | Synchronizes threads so that a group of threads waits until all reach a certain point. |
| `Semaphore.py` | Semaphore | Limits the number of threads accessing a shared resource at the same time. |
| `Rlock.py` | Reentrant Lock | Allows the same thread to acquire a lock multiple times safely. |
| `MyThreadClass.py` | Thread Class | Example of creating a custom thread class. |
| `MyThreadClass_lock.py` | Thread Class with Lock | Thread class with proper locking for shared resources. |
| `MyThreadClass_lock_2.py` | Thread Class with Lock | Another example using locks in a thread class. |
| `Threading_with_queue.py` | Queue | Demonstrates safe communication between threads using `queue.Queue`. |
| `Thread_definition.py` | Basic Threads | Basic thread creation and execution. |
| `Thread_determine.py` | Thread Info | Determines thread names and IDs. |
| `Thread_name_and_processes.py` | Threads & Processes | Demonstrates thread names along with multiprocessing basics. |
| `Condition.py` | Condition Variable | Synchronizes threads using `threading.Condition()`. |
| `Event.py` | Event | Threads communicate via `threading.Event()` to trigger actions. |


## Concepts Covered

- Thread creation using `threading.Thread`
- Synchronization mechanisms:
  - `Lock`
  - `RLock` (Reentrant Lock)
  - `Semaphore`
  - `Barrier`
  - `Condition`
  - `Event`
- Using `queue.Queue` for thread-safe data sharing
- Custom thread classes
- Multithreading with safe access to shared resources
- Combining threads with processes (basic demonstration)

---

## How to Run

1. Make sure Python 3.x is installed.
2. Open a terminal in the project folder.
3. Run any example, e.g.:

```bash
python barrier.py
python semaphore.py
python rlock.py
python threadwlock.py
python threadwqueue.py
