def prime1(num):
    c=0
    for i in range(2,num):
        c=c+1
        if(num%i==0):
            return  c , "Not Prime"
    return c , "Prime"

def prime2(num):
    c=0
    limit=(num**0.5)+1
    for i in range(2,int(limit)+1):
        c+=1
        if(num%i==0):
            return c, "Not Prime"
    return c, "Prime"
def prime3(num):
    c=0
    limit=(num**0.5)+1
    if( num%2 == 0):
        return c,"Not Prime"
    for i in range(3,int(limit),2):
        c+=1
        if(num % i == 0):
            return c,"Not Prime"
    return c, "Prime"

num=67
p1=prime1(num)
p2=prime2(num)
p3=prime3(num)
print(p1)
print(p2)
print(p3)
sq=(num**0.5)
for i in range(2,int(sq)+1):
    print(i,end=",")
