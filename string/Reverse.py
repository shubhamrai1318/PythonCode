s="i.like.this.program.very.much"
s=s.split(".")
print(s)
l=len(s)
print(l)
s.reverse()
for i in range(l):
    print(s[i],end="")
    if i!=l-1:
        print(end=".")
