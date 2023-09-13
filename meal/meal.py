def main():
    prompt = input("What's the time? ")
    if 7.00 <= convert(prompt) <= 8.00:
        print("breakfast time")
    elif 12.00 <= convert(prompt) <= 13.00:
        print("lunch time")
    elif 18.00 <= convert(prompt) <= 19.00:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    answer = hours + minutes
    return answer

if __name__ == "__main__":
    main()