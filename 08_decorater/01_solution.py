import time

def timer(func):
    def wrapper(*args, **kwargs):  # <-- fixed 'arg' to 'args'
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)
