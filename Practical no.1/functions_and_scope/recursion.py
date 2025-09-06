'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))'''

'''def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return(n * factorial(n-1))
print(factorial(3))'''
a = "turvk"
b = "turvk"
c = a
d = "turk"
'''print(id(a))
print(id(b))
print(id(c))
print(id(d))'''
def func(a):
    print(a)
    a += 10
    
num = 5
print(num)
func(num)
print(func(num))