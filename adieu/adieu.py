import inflect

p = inflect.engine()
answer = "Adieu, adieu, to "
names = []
mylist = []

while True:
    try:
        prompt = input()
        names.append(prompt)
        print(names)
    except EOFError:
        mylist = p.join((names))
        print(answer + mylist)
        break