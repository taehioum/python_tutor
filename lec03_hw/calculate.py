def infix_prefix(exp):
    prec = {'(':0, '+':1, '-':1, '*':2, '/':2}
    operators = []
    operands = []
    tokens = list(exp)

    for t in tokens:
        if t == '(':
            operators.append(t)
        elif t == ')':
            while operators and operators[-1] != '(':
                r_oprnd = operands.pop()
                l_oprnd = operands.pop()
                op = operators.pop()
                operands.append((op, l_oprnd, r_oprnd))
            operators.pop()
        elif t not in prec: # this is an integer
            operands.append(int(t))
        else:
            while operators and prec[t] <= prec[operators[-1]]:
                r_oprnd = operands.pop()
                l_oprnd = operands.pop()
                op = operators.pop()
                operands.append((op, l_oprnd, r_oprnd))
            operators.append(t)
    while operators:
        r_oprnd = operands.pop()
        l_oprnd = operands.pop()
        op = operators.pop()
        operands.append((op, l_oprnd, r_oprnd))
    return operands[-1]

def calculate(prefix):
    #TODO: delete pass and FILL ME IN
    pass

exp = input()
# remove the # to try the examples
# exp = "3+4*2"
# exp = "3*4"
# exp = "3*4-2"
# exp = "3*(4-2)"

prefix_exp = infix_prefix(exp)

# remove the # to see the converted prefix notation.
# print(prefix)
print(calculate(prefix_exp))
