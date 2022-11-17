import time


def timed(func):
    def wrapper(name: str):
        start = time.time()
        result = func(name)
        end = time.time()

        time_micro_secs = (end - start) * 1000
        function_name = func.__name__
        print(f"Executed [{function_name}] in {time_micro_secs:.0f} μs")
        return result

    return wrapper


def uppercase(func):
    def wrapper(name: str):
        return func(name.upper())

    return wrapper


def green(func):
    def wrapper(name: str):
        return func(f"\033[32m{name}\033[0m")

    return wrapper


def repeat(times: int):
    def repeat_inner(func):
        def wrapper(name: str):
            results = []
            for _ in range(times):
                results.append(func(name))
            return " ".join(results)

        return wrapper

    return repeat_inner


def clamped(lower: int, upper: int):
    def clamped_inner(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return max(lower, min(result, upper))

        return wrapper

    return clamped_inner


RESULT_MAP = {}


def memoize(func):
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in RESULT_MAP:
            RESULT_MAP[key] = func(*args, **kwargs)
        return RESULT_MAP[key]

    return wrapper


@uppercase
@green
@repeat(times=3)
def add_greeting(name: str):
    return f"Hello {name}!"


@memoize
def _inner_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return _inner_fibonacci(n - 1) + _inner_fibonacci(n - 2)


@timed
def fibonacci(n: int):
    return _inner_fibonacci(n)


x = fibonacci(36)
print(x)

message = add_greeting("jack")
print(message)
