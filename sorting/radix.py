def digits(n,pos):
    if pos==1:
        d = n%10
        return d
    if pos == 2:
        n=n//10
        d=n%10
        return d
    if pos == 3:
        n=n//100
        d=n%10
        return d

n=digits(325,2)
print(n)