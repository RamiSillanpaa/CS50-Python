def main():
    answer = input("Greeting: ")
    print(value(answer))


def value(greeting):
    if greeting.lower() == "hello":
        return 0
    elif greeting[0].lower() == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()