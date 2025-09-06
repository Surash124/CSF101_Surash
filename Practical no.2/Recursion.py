def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
#To print n terms
def printfib(n, i = 0):
    if i < n:
        print(fibonacci_recursive(i), end=" ") #end="" to print in same line
        printfib(n, i + 1)
printfib(10)  # Example: Print first 10 Fibonacci numbers