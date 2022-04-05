import sys

def fibonacci(n):
    if n <= 1:
        return n
    
    result = fibonacci(n-1) + fibonacci(n-2)
    return result

num = sys.argv[1]
print(fibonacci(int(num)))
