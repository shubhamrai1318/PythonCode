exp = " (a*(b+c)*(d-e) "
stack = []
n = len(exp)
for i in range(n):

    ch = exp[i]
    if ch == '(':
        stack.append(i)
        # print(stack)
    if ch == ')':
        l = len(stack)
        if l == 0:
            print("Invalid Exp")
            break
        else:
            prev = stack.pop()
            bracketedexp = exp[prev:i + 1]
            print(bracketedexp)
