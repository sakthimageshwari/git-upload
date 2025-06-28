#finding the count for vowels,consonants and spaces in the given  sentence

p=input("enter the sentence:")
b="aeiouAEIOU"
count_v=0
count_c=0
count_s=0
for char in p:
    if char.isalpha():
        if char in b:
            count_v+=1
        else:
            count_c+=1
    if char==' ': 
        count_s+=1     

print("vowels:",count_v,' ',"consonats:",count_c,' ',"spaces:",count_s)        
