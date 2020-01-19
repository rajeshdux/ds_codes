# Do task based on User input.. 1-3,9 ..other input will loop back'''

list=[1,2,3,4,5,6,7]
middle=int(len(list)/2)

while(True):
    print("To print the First element of the list enter 1:")
    print("To print the Middle element of the list enter 2:")
    print("To print the Last element of the list enter 3:")
    print("To quit enter 9:")
    ch = int(input("enter the choice: \n"))

    if(ch==1):
        print("The first element is :",list[0])
        break
    elif(ch==2):
        print("The Middle element is :",list[middle])
        break
    elif(ch==3):
        print("The Last element is :",list[-1])
        break
    elif(ch==9):
        break

    else:
        print("Not a valid choice...try again...")
        continue

print("The Task is Done....")

