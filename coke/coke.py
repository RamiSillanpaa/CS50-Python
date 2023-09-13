due = 50
print(f"Amount Due: {due}")
while due > 0:
    coin = input("Insert coin: ")
    if coin == "50":
        due -= 50
    elif coin == "25":
        due -= 25
    elif coin == "10":
        due -= 10
    elif coin == "5":
        due -= 5
    if due <= 0:
        print(f"Change Owed: {0 - due}")
    elif due > 0:
        print(f"Amount Due: {due}")