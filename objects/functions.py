def add_two_numbers(n1, n2):
    return n1 + n2

def do_math(n1=1, n2=2, op="add"):
    if op == "add":
        return n1 + n2
    elif op == "sub":
        return n1 - n2
    elif op == "mult":
        return n1 * n2
    elif op == "div":
        if n2 != 0:
            return n1 / n2


print(do_math(5, 10))
print(do_math(5, 10, "div"))
print(do_math(n1=10, n2=50, op="sub"))
print(do_math(n2=50, op="sub", n1=10))
print(do_math(op="mult", n2=50, n1=10))


def do_math_mult(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2

a, s, m, d = do_math_mult(5, 10)
print(a, "; ", s, "; ", m, "; ", d)