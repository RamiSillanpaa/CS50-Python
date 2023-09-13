from pyfiglet import Figlet
import sys
import random
import re

figlet = Figlet()
l = figlet.getFonts()
#print(sys.argv[1]+sys.argv[2])
if len(sys.argv) < 2:
    figlet.setFont(font=random.choice(l))
    prompt = input("Input: ")
    print(figlet.renderText(prompt))
elif len(sys.argv) == 3:
    if bool(re.match("-f|--font", sys.argv[1])) and sys.argv[2] in l:
        figlet.setFont(font=sys.argv[2])
        prompt = input("Input: ")
        print(figlet.renderText(prompt))
    else:
        sys.exit("Invalid usage.")
else:
        sys.exit("Invalid usage.")