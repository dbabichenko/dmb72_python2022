def add_numbers(a, b, c=0, d=0):
    add = a + b + c + d
    subtract = a-b-c-d
    mult = a*b*c*d
    
    return add, subtract, mult


print(add_numbers(44, 45))

print(add_numbers(44, 45, 100))


print(add_numbers(44, 45, 100, 200))

print(add_numbers(44, 45, d=100, c=200))

a, s, d = add_numbers(44, 45, d=100, c=200)
print(a)
print(s)
print(d)