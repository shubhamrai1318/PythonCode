def f(current, limit, a):
    if (current > limit):
        return
    for i in range(limit + 1):
        if i in a[:current]:
            continue
        a[current] = i
        if current == limit:

            print(a)
        else:
            f(current + 1, limit, a)

