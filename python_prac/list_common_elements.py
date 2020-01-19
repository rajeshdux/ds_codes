#Assignment
l=[2,3,6,4,1,3]
l2=[2,6,4,8,1,7]
#print common elements
def list_common(l1=[],l2=[]):
    print(set(l2).intersection(set(l1)))


list_common(l,l2)