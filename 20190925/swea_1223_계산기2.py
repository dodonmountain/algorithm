import sys; sys.stdin = open('1223.txt')

for t_case in range(10):
    length = int(input())
    nums = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    S = []
    N = []
    cal = input()
  
    for char in cal:
        if char == "*":
            if S[-1] == "*":
                N.append(char)
            else:
                S.append(char)
        elif char == "+":
            if S[-1] == "*":
                N.append("*")
                S[-1] = "+"
            else:
                S.append(char)
        else:
            N.append(int(char))
  
    for f in N:
        if f in ("+", "*"):
            b = S.pop()
            a = S.pop()
            if f == "+":
                S.append(a + b)
            elif f == "*":
                S.append(a * b)
        else:
            S.append(f)
  
    print("#{} {}".format(t_case+1, S.pop()))