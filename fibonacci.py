import time


def timed(inner_func):
    def wrapped_func(*args, **kwargs):
        start = time.time()
        x = inner_func(*args, **kwargs)
        end = time.time()
        duration_secs = end - start
        print(f"Executed {inner_func.__name__} in {duration_secs:.3f} secs")
        return x

    return wrapped_func


def cache_result(inner_func):
    results = {}

    def wrapped_func(k: any):
        if k not in results:
            results[k] = inner_func(k)
        return results[k]

    return wrapped_func


@cache_result
def fibonacci(n: int):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@timed
def print_fibonacci(n: int):
    result = fibonacci(n)
    print(result)


print_fibonacci(40)
