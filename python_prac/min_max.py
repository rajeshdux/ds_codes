'''#Assignment
find min and max value without inbuilt min and max function'''

l1=[10, 20, -500,-40, 80]

def min_max(l=[]):
    min=l[0]
    max=l[0]
    for i in range(0,len(l),1):

        if(l[i] > max):
            max = l[i]

        if(l[i] < min):
            min = l[i]

    print("Maximum element = ", max)
    print("Minimum element = ", min)

min_max(l1)
