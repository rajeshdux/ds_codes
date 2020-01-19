# Phone number to words

phone= input("enter phone number: ")
mapping={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}

output=""
for i in phone:
    output += mapping.get(i,"!") + " " # for other values or zero prints exclamation mark
print(output)
