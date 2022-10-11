T = int(input())
answers = []
for _ in range(T):
  a, b, c = map(int, input().split())

  if (a == b == c):
      answers.append(10000 + (a * 1000))
  elif (a == b or a == c):
      answers.append(1000 + (a * 100))
  elif (b == c):
      answers.append(1000 + (b * 100))
  else:
      answers.append(max(a, b, c) * 100)

print(max(answers))