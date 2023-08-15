n=int(input())
a = input()
s=a.split(" ")
# print(s,n)
sum=0
for element in s:
    sum=sum+int(element)
print(sum)
if sum%2==0 and sum%3==0 and sum%5==0:
    print("1")
else:
    print("0")