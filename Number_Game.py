n = 21
print("Welcome to the Game_World")
print("Guess a number")
trial = 1
while(trial<=9):
    n1 = int(input())

    if n1 == n:
        print("Congratulations you won the game!")
        break
    elif n1 > n:
        print("Oops! The number is greater, try again")

    elif n1 < n:
        print("Oops! The number is smaller, try again")

    print("Only", 9-trial,"trials are left")
    trial = trial + 1

    if trial>9:
        print("Game Over!")




