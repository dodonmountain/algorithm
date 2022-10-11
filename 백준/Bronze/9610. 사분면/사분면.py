T = int(input())

axis_map = {
  "Q1": 0,
  "Q2": 0,
  "Q3": 0,
  "Q4": 0,
  "AXIS": 0
}

for _ in range(T):
    x, y = map(int, input().split())
    if (x == 0) or (y == 0):
        axis_map["AXIS"] += 1
    elif (x > 0) and (y > 0):
        axis_map["Q1"] += 1
    elif (x < 0) and (y > 0):
        axis_map["Q2"] += 1
    elif (x < 0) and (y < 0):
        axis_map["Q3"] += 1
    elif (x > 0) and (y < 0):
        axis_map["Q4"] += 1

for (k, v) in axis_map.items():
    print(f"{k}: {v}")
