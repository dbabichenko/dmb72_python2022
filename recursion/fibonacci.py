def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]

    '''
    When you are not interested in some values returned by a function 
    we use underscore in place of variable name. 
    Basically it means you are not interested in how many times the 
    loop is run till now just that it should run some specific 
    number of times overall.
    '''
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print(fib(1))  # [1]
print(fib(2))  # [1, 1]
print(fib(3))  # [1, 1, 2]
print(fib(10)) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
