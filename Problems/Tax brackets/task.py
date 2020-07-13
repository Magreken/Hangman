dollar = int(input())
tax = 0
percent = 0
if dollar <= 15527:
    tax = 0
elif dollar <= 42707:
    tax = dollar * 0.15
    percent = 15
elif dollar <= 132406:
    tax = dollar * 0.25
    percent = 25
else:
    tax = dollar * 0.28
    percent = 28

print(f"The tax for {dollar} is {percent}%. That is {tax:.0f} dollars!")
