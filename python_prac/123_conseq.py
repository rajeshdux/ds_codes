'''write a program to input a list'''

l1 = [1, 2, 4, 6, 3]
l2 = [2, 3, 1, 2, 3]
l3 = [2, 1, 1, 2, 3, 3]


# check whether the list has 1,2,3 consecutively


def convert(s=[]):
    i = ""
    for x in s:
        i += str(x)
    return i



def find_seq(l=[]):

    z = convert(l)

    if "123" in z:
        print("sequence exist")
    else:
        print("No sequence")

find_seq(l1)
find_seq(l2)
find_seq(l3)

