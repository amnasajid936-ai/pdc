from multiprocessing import Process

def greet(name):
    print(f"Hello {name}")

if __name__ == "__main__":
    p = Process(target=greet, args=("Amna",))
    p.start()
    p.join()
