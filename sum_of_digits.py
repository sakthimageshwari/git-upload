#sum of digits

number= 356

s = 0

while number > 0:         
    r=number %10          
    s=s+r                 
    number=number//10     


print(' result is ', s)