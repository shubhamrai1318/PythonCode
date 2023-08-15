def f(x):
    return x
words="Python uses whitespace indentation, rather than curly brackets or keywords, to delimit blocks. An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block.[76] Thus, the program's visual structure accurately represents the program's semantic structure.[77] This feature is sometimes termed the off-side rule, which some other languages share, but in most languages indentation does not have any semantic meaning. The recommended indent size is four spaces.[78]"
print(words)
wordlist = words.split(sep=" ")
print(wordlist)
dict = dict.fromkeys(wordlist)
print(dict)
for word in wordlist:
    if dict[word]==None:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
l=list(dict.items())
print(l)
l.sort(key=lambda x:x[1],reverse=True)
print(l)
maxlist=l[:5]
print(maxlist)