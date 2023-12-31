menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0.00

while True:
    try:
        prompt = input("Item: ").lower()
        total += round(menu[prompt.title()],2)
        print(f"${total:.2f}")
    except EOFError:
        print("")
        break
    except KeyError:
        print("Not such item in the menu.")
