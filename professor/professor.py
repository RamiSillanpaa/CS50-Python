import random
import sys

def main():
    while True:
        level = get_level()
        score = 0
        questions = 0
        eqs = []
        while questions < 10:
            value1 = generate_integer(level)
            value2 = generate_integer(level)
            sum = value1 + value2
            eq = f"{value1} + {value2} = "
            if eq not in eqs:
                eqs.append(eq)
                questions += 1
                for i in range(3):
                    prompt = int(input(eq))
                    if prompt == sum and i < 3:
                        score += 1
                        break
                    elif prompt != sum and i < 2:
                        print("EEE")
                    elif prompt != sum and i == 2:
                        print("EEE")                        
                        print(f'{value1} + {value2} = {sum}')
        print(f'Score: {score}')
        sys.exit(0)
        


def get_level():
    a = 0
    while not 0 < int(a) <= 3 or not str(a).isdigit():
        prompt = input("Level: ")
        if prompt.isdigit():
            a = int(prompt)
    return int(a)


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()