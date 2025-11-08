# Array Sum with Multithreading and Multiprocessing

This Python project demonstrates how to calculate the **sum of an array** using three different approaches:

1. **Normal (single-threaded)**
2. **Multithreading**
3. **Multiprocessing**

It is designed to show the performance differences between **threading and multiprocessing** for CPU-bound tasks.

---

## Features

- Generates a random array of numbers.
- Divides the array into chunks for threads or processes.
- Calculates the sum of the array using:
  - Single-threaded Python `sum()`
  - `threading` module
  - `multiprocessing` module
- Compares execution times for each approach.

---

## Installation

Make sure you have Python 3.x installed. No additional libraries are required.  

Clone the repository:

```bash
git clone https://github.com/amnasajid936-ai/pdc.git
cd pdc
