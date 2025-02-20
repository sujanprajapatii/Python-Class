#Fibonacii Series14
def fibonacci(n):
    a=0
    b=1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
fibonacci(n)