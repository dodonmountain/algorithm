train = 0
maxnow = 0
for _ in range(4):
    a, b = map(int, input().split())
    train -= a
    train += b
    if maxnow < train:
        maxnow = train
print(maxnow)