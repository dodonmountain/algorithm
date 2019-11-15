import random
Man1 = ["가위","바위","보"]
Man2 = ["가위","바위","보"]
a = random.choice(Man1)
b = random.choice(Man2)
if a == "가위":
    if b == "가위":
        print("Result : Draw")
    elif b == "바위":
        print("Result : Man2 Win!")
    else:
        print("Result : Man1 Win!")
if a == "바위":
    if b == "가위":
        print("Result : Man1 Win!")
    elif b == "바위":
        print("Result : Draw")
    else:
        print("Result : Man2 Win!")
if a == "보":
    if b == "가위":
        print("Result : Man2 Win!")
    elif b == "바위":
        print("Result : Man1 Win!")
    else:
        print("Result : Draw")