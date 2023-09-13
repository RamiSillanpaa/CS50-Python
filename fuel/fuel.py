import math

def main():
    try:
        x = "0"
        y = "0"
        while not x.isdigit() or not y.isdigit() or int(x) > int(y) or int(y)==0:
            prompt = input("Input fraction in X/Y format: ")
            x, y = prompt.split("/")

        x = int(x)
        y = int(y)
        a = int(round((x / y * 100),0))


        if a <= 1:
            print("E")
        elif a >= 99:
            print("F")
        else:
            print(f'{a}%')
    except (ValueError, ZeroDivisionError):
        main()
main()