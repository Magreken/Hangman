var = int(input())

if (var % 400 == 0) or ((var % 4 == 0) and (var % 100 != 0)):
    print("Leap")
else:
    print("Ordinary")

