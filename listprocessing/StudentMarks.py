P=[2,2,4,6]
C=[4,6,2,10]
M=[1,3,2]
p=[P[0]]
c=[C[0]]
m=[M[0]]
lenp=len(P)
lenc=len(C)
lenm=len(M)
# print(lenp)
for i in range(1,lenp):
    p=p+[P[i]+p[i-1]]
print("Phy =",p)
for i in range(1,lenc):
    c=c+[C[i]+c[i-1]]
print("Chem=",c)
for i in range(1,lenm):
    m=m+[M[i]+m[i-1]]
print("Math=",m)

p=set(p)
c=set(c)
m=set(m)
result = (p.intersection(c,m))
print(result)
r=list(result)
