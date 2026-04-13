import time

class Timer:
    def __init__(self, name="Execution") -> None:
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc, tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"{self.name}: {self.elapsed:.6f} seconds")