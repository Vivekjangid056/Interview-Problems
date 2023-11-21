# fibonacci series

n = int(input("enter number: "))

first, second = 0, 1

for i in range(n):
    if i <=1:
        result = i
    else:   
        result = first + second
        first = second
        second = result
    print(result)

# using recursion
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print("hello")

for i in range(n):
    print(fib(i))

