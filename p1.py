# Write a program to reverse an integer in Python.

n = int(input("enter number: "))

result = 0

while n!= 0:
    result = result*10 + n%10 
    n = n//10

print(result)