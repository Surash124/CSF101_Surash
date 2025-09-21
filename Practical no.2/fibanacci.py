def fibonacci(n):
    if n<0:
        return 0
    elif n == 1:
        return 1
    elif fibonacci(n-1) + fibonacci(n-2) < 0:
        return
return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))