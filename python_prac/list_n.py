#prints list n times sorted

#l={'e','f','g','h'}

l=[3,6,9,4]
l.sort()
for i in l:
#for i in range(4):

    print(*l, sep="\n")
    print("----------")
