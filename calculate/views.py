from django.http import JsonResponse
from rest_framework.decorators import api_view
from time import time


def timed(opr, n=None, m=None):
    ts = time()
    if opr == "factorial" or opr == "fibonacci":
        result = eval(opr)(n)
    else:
        result = eval(opr)(m, n)
    te = time()
    elapsed = (te - ts) * 1000
    print('timer:{} r:{}'.format(elapsed, result))
    return result, elapsed


def error(message=None):
    return JsonResponse({'status': False, 'message': message}, status=400)


def success(result, message=None, elapsed=None):
    return JsonResponse({'status': True, 'result': result, 'message': message, 'elapsed time': elapsed}, status=200)


def factorial(n):
    if not isinstance(n, int):
        raise Exception("number not set or is not valid")
    if n < 0:
        raise Exception("number must be positive")
    if n > 1000:
        raise Exception("number must be less than 20")
    if n == 1 or n == 0:
        return 1
    else:
        result = n * factorial(n - 1)
        return result


def fibonacci(n):
    if not isinstance(n, int):
        raise Exception("number not set or is not valid")
    if n < 0:
        raise Exception("number must be positive")
    elif n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def ackermann(m, n):
    if not isinstance(n, int) and not isinstance(m, int):
        raise Exception("number not set or is not valid")
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


@api_view(['POST'])
def calculate(request):
    operators = {"factorial", "fibonacci", "ackermann"}
    try:
        opr = request.data['opr']
        n = int(request.data['n']) if request.data['n'] else None
        m = int(request.data['m']) if request.data['m'] else None
        if opr in operators:
            result, elapsed = timed(opr, n, m)
            return success(result, "Done", elapsed)
        else:
            raise Exception("operator not found!")
    except Exception as e:
        return error(e.__str__())
