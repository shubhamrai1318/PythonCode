s = ")("
count = 0
result = "matched"
for element in s:
    # print(element)
    if element == "(":
        count = count + 1
    elif element == ")":
        count = count - 1
        if count < 0:
            result = "unmatched"
            break

print(result)
