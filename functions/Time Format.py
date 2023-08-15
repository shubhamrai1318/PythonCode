hh = int(input("Enter Time in hr: "))
mm = int(input("Enter Time in min: "))
def time(hh,mm):
    if hh>12 and hh<24:
        if mm>60:
            h=hh-12
            mm=mm-60
            h+=1
            print(h,":",mm,"Pm")
        else:
            h=hh-12
            print(h, ":", mm, "Pm")
    elif hh==12:
        print(hh,":",mm,"Pm")
    elif hh<12:
        if mm>60:
            mm=mm-60
            hh+=1
            print(hh,":",mm,"Am")
        else:
            print(hh, ":", mm, "Am")
    elif hh>24:
        print("Invalid Time")


time(hh,mm)
