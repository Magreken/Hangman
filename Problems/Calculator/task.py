# put your python code here

var1 = float(input())
var2 = float(input())

operator = input()

if operator == "+":
    print(var1 + var2)
elif operator == "-":
    print(var1 - var2)
elif operator == "*":
    print(var1 * var2)
elif operator == "pow":
    print(var1 ** var2)
elif var2 == 0:
    print("Division by 0!")
elif operator == "/":
    print(var1 / var2)
elif operator == "mod":
    print(var1 % var2)
elif operator == "div":
    print(var1 // var2)

