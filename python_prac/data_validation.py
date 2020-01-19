l1=[]
l2=[]

with open ("E:\PythonProjects\datafiles\dfile.txt", 'r') as f:
    c=f.readlines()

    for i in c:
        if i[0]=='D':
            l1.append(i)
        else:
            l2.append(i)

c=0
s=0
for i in l1:
    e= i.split("|")
    for i in e:
        f=i.strip('\n')
    s=s+int(f)
    c+=1

l3=l2[0].split('|')
if(l3[1]==str(c) and l3[2]==str(s)):
    print("The Data is Valid...")
else:
    print("Invalid Data...")

print("End....")