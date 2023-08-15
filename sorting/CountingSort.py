a = [2,4,9,6,1,7,5,2,1,2]
f = [0 for x in range(10)]
print("List: ",a,"\nF = ",f)
for element in a:
    f[element] = f[element] + 1
print("Freq=",f)
for i in range(1,10):
    f[i]=f[i]+f[i-1]
print("C.F.=",f)
output = [0 for x in a]
n=len(a)
for i in reversed(range(n)):
    value=a[i]
    pos = f[value]-1
    output[pos] = value
    f[value]-=1
print("Output:",output)