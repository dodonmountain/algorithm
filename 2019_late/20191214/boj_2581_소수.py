M = int(input())
N = int(input())

a = [False,False] + [True]*(N-1)
primes=[]
answer_sum = 0
for i in range(2,N+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, N+1, i):
        a[j] = False
answer_min = None
for prime in primes:
    if prime >= M:
        if not answer_min:
            answer_min = prime
        answer_sum += prime
if answer_min:
    print(answer_sum)
    print(answer_min)
else:
    print(-1)