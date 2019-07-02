operators = {
    '*':lambda x, y:x * y,
    '+':lambda x, y:x + y,
    '-':lambda x, y:x - y,
    '/':lambda x, y:x / y,
}



def calculate(x, y, op):
    return operators[op](x, y)



print(calculate(3, 4, '+'))
print(calculate(3, 4, '-'))
print(calculate(3, 4, '*'))
print(calculate(3, 4, '/'))
