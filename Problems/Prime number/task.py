num = int(input())

if num == 1:
    print("This number is not prime")
else:
    for i in range(2, num - 1, 1):
        if num % i == 0:
            print("This number is not prime")
            break
    else:
        print("This number is prime")
