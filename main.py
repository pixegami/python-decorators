import time


def timed(inner_func):
    def wrapped_func(*args, **kwargs):
        start = time.time()
        inner_func(*args, **kwargs)
        end = time.time()
        duration_secs = end - start
        print(f"Executed {inner_func.__name__} in {duration_secs:.3f} secs")

    return wrapped_func


@timed
def do_something(n: int = 0):
    for x in range(n):
        for y in range(n):
            print(x * y)


@timed
def process_data(n: int = 0):
    pass


@timed
def please_subscribe(n: int = 0):
    pass


do_something(100)
