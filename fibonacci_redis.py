import sys
import redis
r = redis.Redis()


def fib_decorator(fib_fn):
    def wrapper_func(n):
        intermediate_result = r.hget("results", n)
        if intermediate_result:
            return int(intermediate_result)

        result = fib_fn(n)
        if result > 1:
            r.hset("results", n, result)
        return result
    return wrapper_func


@fib_decorator
def fibonacci_redis(n):
    if n <= 1:
        return n
    return fibonacci_redis(n-1) + fibonacci_redis(n-2)


if __name__ == "__main__":
    num = sys.argv[1]
    print(fibonacci_redis(int(num)))
    r.delete("results")
