num=153
temp=num
s=0
while num>0:
    r=num%10
    s=s+r**3
    num=num//10
if s==temp:
    print('It is armstrong number') 
else:
    print("It is not an armstrong number")           