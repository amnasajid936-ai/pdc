# Python Multiprocessing Examples

This project demonstrates **core multiprocessing concepts** in Python.  
It includes examples for **process creation, communication, termination, and background execution**.


## Scripts Overview

| Script | Concept | Description |
|--------|---------|-------------|
| `communicatewpipe.py` | Pipe | Demonstrates inter-process communication using `multiprocessing.Pipe()`. |
| `communicatewqueue.py` | Queue | Demonstrates inter-process communication using `multiprocessing.Queue()`. |
| `killingprocess.py` | Terminate | Shows how to manually terminate a running process. |
| `runbgprocesses.py` | Daemon Processes | Runs a process in the background that exits when the main program ends. |
| `spawning.py` | Basic Process | Demonstrates basic process creation and execution. |

---

## Concepts Covered

- **Process Creation:** Using `Process(target=..., args=...)`  
- **Communication Between Processes:** `Pipe` and `Queue`  
- **Process Control:** `terminate()`, `daemon=True`  
- **Background Execution:** Running processes that exit automatically with the main program  

---

## How to Run

1. Make sure **Python 3.x** is installed.
2. Open a terminal in the project folder.
3. Run any script:

```bash
python communicatewpipe.py
python communicatewqueue.py
python killingprocess.py
python runbgprocesses.py
python spawning.py
