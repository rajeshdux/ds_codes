#take username and password and do login validation ..after 3 attempts user account should be blocked..'''
import pickle
#Registration
print("----------------------")
print("--* REGISTRATION *---")
print("----------------------")
username=input("enter the UserName for registration : ")
password=input("enter the desired password: ")

#Login
print("-----------------------")
print("-----* LOGIN *---------")
print("-----------------------")
c=0
while(True):
    uname=input("enter the username: ")
    pw=input("enter the password: ")
    if(uname==username and pw==password):
        print("Login success")
        break
    else:
        c+=1
        if(c==3):
            print("Login Failed : User Account Blocked...")
            break
        else:
            print("Wrong try..:","\nUserName:",uname,"\nPassword:",pw,"\n please try again only",3-c,"try left")


