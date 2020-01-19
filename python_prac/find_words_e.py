#create l=["escar", 'exception', 'svcon', "faol", "done","ena"] find and print word starting with e..

l=["escar", 'exception', 'svcon', "faol", "done","ena", "Exa","Emma"]

for i in range(0,len(l)):
    s = l[i].lower()
    if s[0]=="e":
        print(l[i])

