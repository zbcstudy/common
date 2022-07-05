def fib(n: int):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b


fib(2000)
print(fib(0))


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print(fib2(20000))
