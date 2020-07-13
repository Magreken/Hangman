# Write your code here
import random as rd

words = ["python", "java", "kotlin", "javascript"]

print("H A N G M A N")
game = ""

val = rd.randint(0, 3)
word = words[val]
helping = ""
taken = ""
for i in range(len(word)):
    helping += "-"

i = 0
while game != "exit":
    game = input("""Type "play" to play the game, "exit" to quit: """)
    print()
    if game == "exit" or game != "play":
        continue
    while i < 8:
        print(helping)
        if not ("-" in helping):
            break

        s = input("Input a letter: ")
        tmp = ""
        if len(s) != 1:
            print("You should input a single letter")
            tmp = helping
        elif not s.isascii() or s.upper() == s:
            print("It is not an ASCII lowercase letter")
            tmp = helping
        elif s in taken:
            print("You already typed this letter")
            tmp = helping
        elif s in word:
            taken += s
            for j in range(len(word)):
                if word[j] == s:
                    tmp += s
                else:
                    tmp += helping[j]
        else:
            print("No such letter in the word")
            taken += s
            tmp = helping
            i += 1
            if i == 8:
                break

        helping = tmp
        print()

    if i == 8:
        print("You are hanged!")
        print()
    else:
        print(f"You guessed the word {helping}!")
        print("You survived!")
        print()
