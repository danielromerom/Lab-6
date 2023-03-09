# Daniel Romero

def encode(password):
    phrase = str(password)
    encoded_password = ""
    for i in password:
        encoded_password += str(int(i) + 3)
    return encoded_password


def decode(password):
    pass


def main():
    # looping menu
    option = "1"
    phrase = ""
    while option != "3":
        # print menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif option == "2":
            print(f"The encoded password is {password}, and the original password is {decode(password)}.")
            print()


if __name__ == "__main__":
    main()

