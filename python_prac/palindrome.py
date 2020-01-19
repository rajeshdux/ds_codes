#palindrome or not
def check_palindrome(n=0):
    a=str(n)
    #l=input("enter the number: ")
    if(a[0]==a[-1]):
        print("Entered number is palindrome")
    else:
        palindrome = "Entered number is not palindrome"
        print("%s" % palindrome)

    print("end")


check_palindrome(232)


