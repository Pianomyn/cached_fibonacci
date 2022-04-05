import sys
import redis
r = redis.Redis()

def fib_decorator(fib_fn):
    def wrapper_func(n):
        intermediate_result = r.hget("results", n)
        if intermediate_result:
            intermediate_result = int(intermediate_result)
            return intermediate_result 

        result = fib_fn(n)
        if result > 1:
            r.hset("results", n, result)
        return result
    return wrapper_func

num = sys.argv[1]

@fib_decorator
def fibonacci_redis(n):
    if n <= 1:
        return n
    result = fibonacci_redis(n-1) + fibonacci_redis(n-2)
    return result

print(fibonacci_redis(int(num)))
r.delete("results")
