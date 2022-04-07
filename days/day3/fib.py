def fib1 (limit):
    a, b = 0, 1
    while a < limit:
        print(a)
        a, b = b, a+b
        """ a = b
        b = (a+b) """
