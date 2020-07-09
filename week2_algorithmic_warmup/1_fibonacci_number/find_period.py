from fibonacci import calc_fib


n = 20
m_min = 2
m_max = 10

for m in range(m_min, m_max):
    print('m = ', m)
    for i in range(n):
        print(calc_fib(i) % m)
