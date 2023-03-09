def menu_options():
    print("MENU")
    print("-------------")
    print("1.Encode")
    print("2.Decode")
    print("3.Quit")


def encode_password(password):

    encoded_pw = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3))
        encoded_pw += encoded_digit
    return encoded_pw


def decode_password(encoded_pw):
    decoded_pw = ""
    for digit in encoded_pw:
        decoded_digit = str((int(digit) - 3))
        decoded_pw += decoded_digit
    return decoded_pw


def main():
    encoded_pw = ""
    while True:
        menu_options()
        choice = int(input('Please enter an option: '))
        if choice == 1:
            password = input('Please enter your password to encode: ')
            encoded_pw = encode_password(password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            if not encoded_pw:
                print("You must encode a password first!")
            else:
                decoded_pw = decode_password(encoded_pw)
                print(f"The encoded password is {encoded_pw}, and the original password is {decoded_pw}.")
        elif choice == 3:
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
