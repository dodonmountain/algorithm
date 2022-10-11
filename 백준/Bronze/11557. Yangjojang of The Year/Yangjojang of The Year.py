T = int(input())

for _ in range(T):
    N = int(input())
    leaderboard = []
    for _ in range(N):
      school, score = map(str, input().split())
      score = int(score)
      leaderboard.append([school, score])
    print(sorted(leaderboard, key=lambda x: x[1], reverse=True)[0][0])
