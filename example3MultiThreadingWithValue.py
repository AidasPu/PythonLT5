from threading import Thread
import time


class ThreadWithReturnValue(Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=3600):
        super().join(timeout)
        return self.result


def print_cube(num):
    # A function that returns the third power of a number given as a parameter
    time.sleep(2)
    print(f"Cube: {num * num * num}")


def print_square(num):
    # A function that returns the square of the number given as a parameter
    time.sleep(2)
    return num * num

square_print = ThreadWithReturnValue(print_square,[5])
cube_print = ThreadWithReturnValue(print_cube, [5])
square_print.start()
cube_print.start()

cube_print.join(5000)
print(f"Square: {square_print.join()}")
