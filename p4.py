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

