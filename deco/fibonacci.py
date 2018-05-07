from clock_deco2 import clock

@clock
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    fibonacci(6)
