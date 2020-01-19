'''Assignment:
li=['program started' , 'Error in line 1', 'line 2',
'line 3','exception occurred', 'process success']
Output
Error in line 1
exception occurred
process success
'''

li=['program started', "Error in line 1", 'line 2',"line 3", "exception occurred","process success"]
for i in range(0,len(li)):
    if (li[i]=="Error in line 1"):
        print(li[i])
    if(li[i]=="exception occurred"):
        print(li[i])
    if(li[i]=="process success"):
        print(li[i])

print("End")


