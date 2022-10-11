T = int(input())
table = {
  '@': lambda x: x * 3,
  '%': lambda x: x + 5,
  '#': lambda x: x - 7,
}
for _ in range(T):
  arr = input().split()
  answer = float(arr[0])
  for i in range(1, len(arr)):
    answer = table[arr[i]](answer)
  print('%.2f' % answer)
