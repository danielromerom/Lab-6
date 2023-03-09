# Daniel Romero

def encode(phrase):
    pass


def decode(phrase):
    pass


def main():
    # looping meny
    option = "1"
    phrase = ""
    while option != "0":
        # print menu
        print("0. Exit")
        print("1. Enter a new phrase")
        print("2. Print encoded phrase")
        print("3. Print decoded phrase")
        option = input ("ender an option: ")

        if option == "1":
            phrase = input("Enter your phrase: ")
        elif option == "2":
            print("Encoded phrase is", encode(phrase))
        elif option == "3":
            print("Decoded phrase is", decode(phrase))