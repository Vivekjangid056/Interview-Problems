# number is prime or not

def prime(n):
    if n == 0 or n== 1:
        return "number is prime"
    else:
        for i in range(2, n):
            if n%i ==0:
                return "number is not prime"
        else:
            return "number is prime"
        

print(prime(11))