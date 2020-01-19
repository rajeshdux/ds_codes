#create file with success,exception,error,failure,completed,... check list if value exist print success or failure


import os.path
with open("E:/PythonProjects/datafiles/s_file.txt",'w') as file:
    file_list=["success", "exception", "error", "failure", "completed"]
    file.writelines(["%s\n" % item for item in file_list])
    if os.path.exists('E:/datafiles/s_file.txt'):
        print("File created")

file=open("E:/PythonProjects/datafiles/s_file.txt", "r")
s_list=file.read().strip().split("\n")
print(s_list)

while True:
    s_string = input("enter the data to search: ")
    if s_string == "":
        continue
    if s_string in s_list:
        print("The searched data exists at location: ", s_list.index(s_string)+1)
        break
    else:
        print("The searched data doesn't exists")
        break
file.close()
