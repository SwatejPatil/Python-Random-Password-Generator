import string
import random

if __name__ == "__main__":
    charSet1 = string.ascii_lowercase
    charSet2 = string.ascii_uppercase
    charSet3 = string.digits
    charSet4 = string.punctuation
    charSet5 = string.hexdigits

    # passLen = int(input("Enter password length\n"))
    while True:
        try:
            passLen = int(input("Enter the password length \n"))
            break
        except ValueError :
            print("Please enter a number and try again...")
    password = []
    password.extend(list(charSet1))
    password.extend(list(charSet2))
    password.extend(list(charSet3))
    password.extend(list(charSet4))
    password.extend(list(charSet5))

    random.shuffle(password)

    print("".join(password[0:passLen]))
