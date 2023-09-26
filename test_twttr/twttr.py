import re

def main():
    prompt = input("Input: ")
    print(shorten(prompt))


def shorten(word):
    return re.sub("[aeiouAEIOU]", "", word)


if __name__ == "__main__":
    main()