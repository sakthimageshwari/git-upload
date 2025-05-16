'''
INPUT="AGFT3BHHGTY4HBGV6HDG6K7HDV1"
OUTPUT SHOULD BE 3+4+6+6+7=?

'''
input_value=input("enter some string:")
a=0
for char in input_value:
    if '0'<=char<='9' and char!='1':
        a+=ord(char)-ord('0')
print(a)