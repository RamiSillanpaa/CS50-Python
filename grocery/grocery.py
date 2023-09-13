order = {}
while True:
    try:
        prompt = input("").upper()
        if prompt in order:
            order[prompt] = order[prompt] + 1
        else:
            order[prompt] = 1
    except EOFError:
        orde = dict(sorted(order.items()))
        for i in orde:
            print(str(orde[i]) + " " + str(i))
        break