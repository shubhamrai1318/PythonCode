def insertion(l):
    l = [7,2,4,9,6]
    n=len(l)
    print("Input Array\n",l)
    for i in range (n-1):
        if l[i]<=l[i+1]:
            continue
        t=l[i+1]
        j=i+1
        while j>=1 and l[j-1]>t:
            l[j]=l[j-1]
            j=j-1
        l[j]=t
    print("sorted Array\n",l)

a=insertion()