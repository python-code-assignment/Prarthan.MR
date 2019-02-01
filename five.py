import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 ):
        print("Minimum length of transaction password: 6")
        break
    elif (len(p)>12):
        print(" Maximum length of transaction password: 12")
        break
    elif not re.search("[a-z]",p):
        print("At least 1 letter between [a-z]")
        break
    elif not re.search("[0-9]",p):
        print("At least 1 number between [0-9]")
        break
    elif not re.search("[A-Z]",p):
        print("At least 1 letter between [A-Z]")
        break
    elif not re.search("[$#@]",p):
        print(" At least 1 character from [$#@]")
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")


