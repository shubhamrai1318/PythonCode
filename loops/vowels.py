s=" a b v f o h y k g e g u s".lower()
vowels="aeiou"
const="bcdfghjklmnpqrstvwxyz"
vowelcount=0
constcount=0
for ch in s:
    if ch in vowels:
        vowelcount+=1
    if ch in const:
        constcount+=1
print(vowelcount,constcount)
