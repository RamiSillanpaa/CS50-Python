import re
from string import punctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #“All vanity plates must start with at least two letters.”
    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    #“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
    #The first number used cannot be a ‘0’.”
    #“No periods, spaces, or punctuation marks are allowed.”
    if bool(re.match("^[A-Z][A-Z]+[\d]*$", s)) and bool(re.match("^[\w]{2,6}$", s)):
        if bool(re.match("^[A-Z]*[1-9]+[0-9]*$", s)) or bool(re.match("^[A-Z]*$", s)):
            return True
        else:
            return False
    else:
        return False

main()