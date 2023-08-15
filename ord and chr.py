#ord gives ascii value of a character
print(ord('A'))#ord is short for ordinal
print(ord('a'))
print(ord('0'))
print(ord(' '))
print(chr(65))
print(chr(67))

for i in range(10000):
    print(chr(i),end=",")