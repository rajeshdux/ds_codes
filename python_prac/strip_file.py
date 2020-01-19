#Ram#2S#BTM
# sham#32#JPNagar etc..
# create unique file,duplicate and ascending and ddescending
from modules import file_io
with open("E:/PythonProjects/datafiles/strip.txt") as f:
    s=[]
    s=file_io.fread("strip.txt")
    # print(s)


a=[]
a.append(s[0].strip().split("\n"))
l=[]
for i in a[0]:
    l.append(i.strip().split("#"))
print(l)

l.sort(key=lambda x: x[0]) # x[1...n] based on sort key chosen
print(l)



# c=[]
# for i in l[0]:
#     if len(i) == 2:
#         c.append(i.split())
#
# print(c)
#
# d={
#     "a":[1,2,3]
# }
# print(d["a"])
