exp=100
monster=[(101,100,1),(100,1,2),(101,100,3)]
print("Monster:",monster)
monster.sort()
l=len(monster)
for i in monster:
    if exp>=i[0]:
        print(exp,"vs",i[0],"\t\tbonus=",i[1])
        exp=exp+i[1]
        print(exp,"\t\t\tMonster",i[2] ,"Loose" )
        
