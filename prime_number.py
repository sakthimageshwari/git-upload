

def prime_no(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return "It is prime"
print(prime_no(13))    