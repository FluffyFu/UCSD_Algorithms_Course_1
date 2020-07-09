# Uses python3

cache = dict()
def calc_fib(n):
    if (n <= 1):
        return n
    if n in cache:
        return cache[n]
    else:
        cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]

def calc_fib_naive(n):
    if (n <= 1):
        return n
    return calc_fib_naive(n-1) + calc_fib_naive(n-2)

if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
