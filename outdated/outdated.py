import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        prompt = input("Date: ")
        if bool(re.match("^[\s]*[0-9]+['/']+.*$", prompt)):
            a, b, c = prompt.strip().split("/")
            m = str(a).zfill(2)            
            d = str(b).zfill(2)
            y = int(c)
            if int(d) < 32 and int(m) < 13:
                print(f'{y}-{m}-{d}')
                break
            else:
                continue
        elif bool(re.match("^[a-zA-Z]+[\s][0-9]+[,][\s][0-9]+$", prompt)):
            x = prompt.replace(",", "")
            a, b, c = x.split(" ")
            m = str(months.index(a)+1).zfill(2)            
            d = str(b).zfill(2)
            y = int(c)
            if int(d) < 32 and int(m) < 13:
                print(f'{y}-{m}-{d}')
                break
            else:
                continue
    except EOFError:
        break