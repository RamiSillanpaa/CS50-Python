import random

a = True

while a:
    level = input("Level: ")
    try:
        if int(level) >= 1 and level.isdigit():
            answer = random.randrange(1, int(level))
            guess = 0
            while guess != answer:
                guess = int(input("Guess: "))
                if guess < answer and 1 <= guess <= int(level):
                    print("Too small!")
                elif guess > answer and 1 <= guess <= int(level):
                    print("Too large!")
                elif guess == answer and 1 <= guess <= int(level):
                    print("Just right!")
                    a = False
                else:
                    continue
        elif level.isalpha():
            continue
        else:
            continue
    except ValueError:
        continue