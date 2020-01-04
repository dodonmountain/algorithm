import time
start = time.time()


def solution(n):
    def ipr(num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        elif num % 2 == 0:
            return False
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True
    answer = len([x for x in list(range(3, n+1, 2)) if ipr(x)])+1
    return answer

print(solution(200000))
print("time :", (time.time() - start)*1000000)