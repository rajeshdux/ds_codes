d={'A':'0Q', 'a':'1@', 'B':'15', 'c':'db', 'o':'00', 'd':'4$', 'D':'5%', 'e':'4^',
   'l':'1#', 'i':'1*', '1':'3A', '2':'T0', '3':'Q0', 'b':'$1'
   }

message=''
user_input = input("Enter the Data to encrypt..: ")
for i in user_input:
    if i in d.keys():
        message=message+d[i]
    else:
        message=message+i

print(message)