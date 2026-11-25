
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        print("Timer started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()

        total_time = self.end - self.start

        print("Timer stopped")
        print("Time taken:", total_time, "seconds")


# Using context manager
with Timer():
    for i in range(1000000):
        pass
