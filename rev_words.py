# Reversing sentence 

p = input("enter the sentence:")
a = p.strip().split('\n')

for i in a:
    words = i.strip().split()
    ac=words[::-1]
    bc=' '.join(ac)
    print(bc)    
