from modules import file_io


def user_reg():
    # Registration
    try:
        print("----------------------")
        print("--* REGISTRATION *---")
        print("----------------------")
        while True:
            username = input("Enter the UserName for registration : ")
            a = username.isdigit()
            if a == True:
                raise Exception("Enter only Characters as UserName")
                continue
            else:
                break

        password = input("enter the desired password: ")

        l = []
        l.append(username)
        l.append(password)

        d={}
        d[username]=password
        print("dictionary: ",d)

        file_io.fappend("ulogs.txt", l)

    except Exception as ex:
        print(ex)


def user_login():
    # Login
    try:
        print("-----------------------")
        print("-----* LOGIN *---------")
        print("-----------------------")
        c = 0
        while (True):
            uname = input("enter the username: ")
            pw = input("enter the password: ")

            # with open('E:/PythonProjects/datafiles/ulogs.txt', 'rb') as handle:
            #     if os.path.exists('E:/PythonProjects/datafiles/uv_logs.pkl'):
            #         pass
            #     else:
            #         raise Exception("Problem reading data from uv_logs...")
            l = []
            l=file_io.fread("ulogs.txt")


            for i in range(0, len(l), 2):
                username=[]
                username.append(l[i])

            for i in range(1, len(l), 2):
                password=[]
                password.append(l[i])


            if (uname in username and pw in password):
                print("Login success")
                break
            else:
                c += 1
                if (c == 3):
                    print("Login Failed : User Account Blocked...")
                    break
                else:
                    print("Wrong try..:", "\nUserName:", uname, "\nPassword:", pw, "\n please try again only", 3 - c,
                          "try left")
    except Exception as ex:
        print(ex)
