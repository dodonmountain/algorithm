_ = input()
s = input()
print('A' if s.count('A') > s.count('B') else 'B' if s.count('A') < s.count('B') else 'Tie')