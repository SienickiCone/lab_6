# This lab file belongs to Quang Anh Pham
encode_password = None


def encode(password):
    empty_list = []
    for i in range(0, len(password)):
        empty_list.append(str(int(password[i]) + 3)[-1])
    return ''.join(empty_list)
    # Warning, if you are using this function, the value return is a string, not an integer.


def menu():
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')


def main():
    user_selection = '0'
    while user_selection != '3':
        global encode_password
        menu()
        user_selection = input("Please enter an option: ")
        if user_selection == '1':
            password = input("Please enter your password to encode: ")
            encode_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif user_selection == '2':
            print(f'The encoded password is {encode_password}, and the original password is {decode(encode_password)}\n')
        elif user_selection == '3':
            continue


if __name__ == "__main__":
    main()
