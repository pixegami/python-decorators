def repeat(times: int):
    def repeat_inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return repeat_inner


def green(func):
    def wrapper(text: str):
        green_text = f"\033[32m{text}\033[0m"
        func(green_text)

    return wrapper


def obfuscate_input(func):
    def wrapper(text: str):
        obfuscated_text = text[0] + "*" * len(text)
        func(obfuscated_text)

    return wrapper


@repeat(times=5)
@obfuscate_input
@green
def say_hello(name: str):
    print(f"Hello {name}!")


say_hello("pixegami")
