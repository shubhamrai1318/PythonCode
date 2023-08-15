l=[1,2,5,10,20]
# n=int(input("Amount= "))
n=25
for i in range(5):
    if l[i]==n:
        print(l[i])
    else:
        d=n%10
        n=n//10
        if d==l[i] and n==l[i]:
            print(d,n)
