import functools
import time
from datetime import datetime

def memorize_factorial(func):
    # A decorator that caches the results of factorial function
    cache = {}
    def wrapper(n, *args):
        start_time = time.time()
        if n in cache:
            print(f"returning cached value for fatorial({n})")
            return cache[n]
        else:
            print(f"calculating and caching result for factorial({n})")
            result = func(n, *args)
            cache[n] = result
            end_time = time.time()
            print(f" function {func.__name__} took execution time: {end_time - start_time}")
            return result
    return wrapper


def timer(func):
    def wrapper(n, *args):
        start = time.time()
        result = func(n, *args)
        end = time.time()
        print(f" function {func.__name__} took execution time: {end - start}")
        return result
    return wrapper

def counter(func):
    def wrapper(n, *args):
        if not hasattr(func, 'count'):
            func.count = 0
        result = func(n,*args)
        func.count += 1
        print(f"{func.__name__} has been called {func.count} times")
        return result
    return wrapper


#@memorize_factorial #3.5s
#@timer # 2.5s
@counter
def factorial(n):
    if n==0 or n == 1:
        return 1
    else:
        return factorial(n-1) * n


#@timer
@counter
def tail_factorial(n, p=1):
    if n<=1:
        return p
    else:
        return tail_factorial(n-1, n*p)


res = factorial(12)
print("factorial =",res)
res2 = tail_factorial(12)
print("tail factorial =",res2)


        