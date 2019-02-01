num = input("Enter numbers: ")
#num = numb.split(',')
odd = []
for x in num.split(','):
    b=int(x)
    if(b%2!=0):
        odd.append(str(b*b))
print(','.join(odd))    



