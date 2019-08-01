N = int(input())
if N % 5 == 0:
    print(N // 5)
elif (N % 5) % 3 == 0:
    print((N // 5) + ((N % 5) // 3))
elif N % 3 == 0:
    print(N // 3)
else:
    for i in range(1, N // 5):
        if (N - 5 * i) % 3 == 0:
            answer = i + ((N - 5 * i) // 3)
        else:
            answer = -1
    print(answer)
