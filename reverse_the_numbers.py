num=1234
s=0
while num>0:
    r=num%10
    s=s+r
    if num>9:
        s=s*10
    num=num//10
print("The Reversed number:",s)        