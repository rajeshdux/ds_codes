'''find ascending and descending without inbuilt functions'''

#list = [40,20,10,80,20]
list=['a','c','f','e','d','b']
for i in range (len(list)-1,0,-1):
    for j in range(i):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
print("Ascending Order: ",list)

for i in range (len(list)-1,0,-1):
    for j in range(i):
        if list[j] < list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
print("Descending Order: ",list)



