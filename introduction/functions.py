# def displayMyName(name):
	# print(name)

# displayMyName(input('Enter your name: '))


##Fibonacci Number
# def fib(n):
    # a, b = 0, 1
    # result = []
    # while a < n:
        # result.append(a)
        # a, b = b, a+b
    # return result
        
# fibonacciNumbers = fib(10000000000000000000000000000000000000000000000000000000000000000)

# print(fibonacciNumbers)


##Ask if ok
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
    # while True:
        # ok = input(prompt)
        # if ok in ('y', 'ye', 'yes'):
            # return True
        # if ok in ('n', 'no', 'nop', 'nope'):
            # return False
        # retries = retries - 1
        # if retries < 0:
            # raise ValueError('invalid user response')
        # print(reminder)
        
# ask_ok('Will you marry me: ')

##Functions summary
#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):