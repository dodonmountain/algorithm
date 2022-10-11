T = int(input())

score_a = 0
score_b = 0

for _ in range(T):
  for _ in range(9):
      a, b = map(int, input().split())
      score_a += a
      score_b += b

  print('Yonsei' if score_a > score_b else 'Korea' if score_a < score_b else 'Draw')