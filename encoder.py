# Daniel Romero

# define encode function
def encode(password):
    password = str(password)
    encoded_password = ""
    for i in password:
        encoded_password += str(int(i) + 3)
    return encoded_password


# define decode function
def decode(password):
    password = str(password)
    decoded_password = ""
    for i in password:
        decoded_password += str(int(i) - 3)
    return decoded_password


# defines main function
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
        # asks user to pick an option
        option = input("Please enter an option: ")
        # encodes password provided by user
        if option == "1":
            # asks user to provide the password
            password = input("Enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        # decodes password and returns it to the user
        elif option == "2":
            print(f"The encoded password is {password}, and the original password is {decode(password)}.")
            print()


# runs the program
if __name__ == "__main__":
    main()

