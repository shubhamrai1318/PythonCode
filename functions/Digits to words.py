# conversion of digits into words upto 100 Crore:
def unit(n):
    digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return digits[n]


def eleven(e):
    ele = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    return ele[e]


def tens(t):
    ten = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    return ten[t]


def upto99(n):
    if n <= 9:
        return unit(n)
    if n >= 11 and n <= 19:
        return eleven(n - 11)
    if n % 10 == 0:
        return tens(n // 10)
    t = n // 10
    u = n % 10
    return tens(t) + " " + unit(u)


def upto999(n):
    if n <= 99:
        return upto99(n)
    h = n // 100
    if n % 100 == 0:
        return unit(h) + " hundred"
    d = n % 100
    return unit(h) + " hundred " + upto99(d)


def upto9999(n):
    if n < 999:
        return upto999(n)
    t = n // 1000
    if n % 1000 == 0:
        return unit(t) + " Thousand"
    d = n % 1000
    return unit(t) + " Thousand " + upto999(d)


def upto99999(n):
    if n < 9999:
        return upto9999(n)
    t = n // 10000
    if n % 10000 == 0:
        return tens(t) + " Thousand "
    d = n % 10000
    return tens(t) + " " + upto9999(d)


def upto999999(n):
    if n < 99999:
        return upto99999(n)
    t = n // 100000
    if n % 100000 == 0:
        return unit(t) + " Lakh "
    d = n % 100000
    return unit(t) + " Lakh " + upto99999(d)


def upto9999999(n):
    if n < 999999:
        return upto999999(n)
    t = n // 1000000
    if n % 1000000 == 0:
        return tens(t) + " Lakh"
    d = n % 1000000
    return tens(t) + " " + upto999999(d)


def upto99999999(n):
    if n < 9999999:
        return upto9999999(n)
    t = n // 10000000
    if n % 10000000 == 0:
        return unit(t) + " Crore"
    d = n % 10000000
    return unit(t) + " Crore " + upto9999999(d)


def upto999999999(n):
    if n < 99999999:
        return upto99999999(n)
    t = n // 100000000
    if n % 100000000 == 0:
        return tens(t) + " Crore"
    d = n % 100000000
    return tens(t) + " " + upto99999999(d)


n = int(input("Enter any number= "))
if n > 999999999:
    print("Enter Number Less than 100 Crore")
else:
    print(n, "in Word : ", upto999999999(n))
