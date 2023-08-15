n = input("Enter the number: ")
l=[n]

while True:
    sum = 0
    i = 0
    for element in n:
        sq = int(element) * int(element)
        sum = sum + sq
        i = i + 1
    if sum==1:
        print("Happy Number")
        break
    if sum in l:
        l=l+[sum]
        print(l)
        print("Not Happy")
        break
    n = str(sum)
    l=l+[sum]
    print(l)
