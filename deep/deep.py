answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if answer.replace(" ", "") == "42":
    print("Yes")
elif answer.lower() == "forty-two":
    print("Yes")
elif answer.lower() == "forty two":
    print("Yes")
else:
    print("No")