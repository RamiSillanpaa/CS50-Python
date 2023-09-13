import re

camelCase = input("Give me a variable name in camel case: ")
snake_case = ""
for i in camelCase:
    if i.isupper():
        snake_case += "_" + i.lower()
    else:
        snake_case += i

print(snake_case)