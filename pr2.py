# Write a program in Python to check whether an integer is Armstrong number or not.

n = int(input("enter the number: "))

def armstrong(n):
    power = len(str(n))
    temp = n
    sum = 0
    while temp>0:
        digit = temp % 10
        sum += digit**power
        temp = temp//10
    if sum == n:
        return f"number {n} is armstrong"
    else:
        return f"number {n} not armstrong"

print(armstrong(n))