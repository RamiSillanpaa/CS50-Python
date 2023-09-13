x, y, z = input("Give me a math equation: ").split(" ")
if y == "+":
    print(format(int(x) + int(z),".1f"))
elif y == "-":
    print(format(int(x) - int(z),".1f"))
elif y == "*":
    print(format(int(x) * int(z),".1f"))
elif y == "/":
    print(format(int(x) / int(z),".1f"))