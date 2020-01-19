'''
#Reverse the list without using reverse function..
'''

def reverse(l=[]):
    s=[]
    for i in range(1,len(l)+1):
        s += l[-i]
    return s
