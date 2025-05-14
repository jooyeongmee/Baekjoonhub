n = int(input())


def fibonacci(value):
    if value == 0 or value == 1:
        return value
    else:
        return fibonacci(value - 1) + fibonacci(value - 2)


print(fibonacci(n))

