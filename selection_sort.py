arr = [64, 25, 10, 22, 11]
n = len(arr)
# # 1st step [0, n - 1]
# minIdx = 0
# for j in range(1, n):
#     if arr[minIdx] > arr[j]:
#         minIdx = j

# arr[0], arr[minIdx] = arr[minIdx], arr[0]

# print(arr)

# # 2nd stop [1, n-1]

# minIdx = 1
# for j in range(2, n):
#     if arr[minIdx] > arr[j]:
#         minIdx = j

# arr[1], arr[minIdx] = arr[minIdx], arr[1]

# print(arr)

# # 3rd step [2, n-2]

# minIdx = 2
# for j in range(3, n):
#     if arr[minIdx] > arr[j]:
#         minIdx = j

# arr[2], arr[minIdx] = arr[minIdx], arr[2]

# print(arr)

# # 4th step [3, n-3]

# minIdx = 3
# for j in range(4, n):
#     if arr[minIdx] > arr[j]:
#         minIdx = j

# arr[3], arr[minIdx] = arr[minIdx], arr[3]

# print(arr)

for i in range(n-1):
    minIdx = i
    for j in range(i + 1, n):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)