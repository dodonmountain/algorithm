while True:
    n = int(input())
    if n == -1:
        break
    divisors = []
    for i in range(1, n):
        if not (n % i):
            divisors.append(i)
    if sum(divisors) == n:
        print(n, '=', ' + '.join(map(str, divisors)))
    else:
        print(n, 'is NOT perfect.')
    