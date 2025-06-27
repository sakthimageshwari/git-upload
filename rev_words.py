# Reversing sentence 

p = """
hii  i am sakthi.
i am a good girl.
i love to read books.
"""
a = p.strip().split('\n')

for i in a:
    words = i.strip().split()
    ac=words[::-1]
    bc=' '.join(ac)
    print(bc)    
