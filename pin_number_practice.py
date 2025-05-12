userpin=input('enter the pin: ')
i=1

while i<=3 and userpin!='1234':
    print("try again the pin")
    userpin=input('enter the pin: ')
    i+=1

if userpin=='1234':
    print("pin is correct")
else:
    print("the pin is incorrect")