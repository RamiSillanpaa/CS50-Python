import re

prompt = input("Input: ")
output = re.sub("[aeiouAEIOU]", "", prompt)
print(output)