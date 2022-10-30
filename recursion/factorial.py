def factorial (x):
    temp = 0
    if x > 1:
        temp = x * factorial(x-1)
    else:
        temp = 1
    
    print(temp)
    return temp

print(factorial(3))
