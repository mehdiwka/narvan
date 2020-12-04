from time import time


def timeit(method):
    def timed(*args, **kw):
        global elapsed
        ts = time()
        result = method(*args, **kw)
        te = time()
        elapsed = (te - ts) * 1000
        print('timer:{} r:{}'.format(elapsed, result))
        return result
    return timed
@timeit
def fibonacci(n):
    if not isinstance(n, int):
        raise Exception("number not set or is not valid")
    if n < 0:
        raise Exception("number must be positive")
    elif n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3))
