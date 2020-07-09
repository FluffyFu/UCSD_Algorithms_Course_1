# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    else:
        temp = b
        b = a % b
        a = temp
        return gcd(a, b)

def lcm(a, b):
    common = gcd(a, b)
    return a * b / common

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

