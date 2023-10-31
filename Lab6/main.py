#encoder
def encode():
    stored_encode = input("Please enter your password to encode: ")
    stored_decode = []
    for i in stored_encode:
        if (int(i) + 3) > 9:
            stored_decode.append(int(i) + 3 - 10)
        else:
            stored_decode.append(int(i) + 3)
    print("Your password has been encoded and stored!\n\n")
    return stored_decode


def decode(encoded):

    return_str = ''

    for digit in range(0, len(encoded)):

        if encoded[digit] - 3 >= 0:
            return_str += str(encoded[digit] - 3)
        else:
            return_str += str(encoded[digit] - 3 + 10)

    return return_str



while True:
    menu_option = int(input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\n\nPlease enter an option: "))

    if menu_option == 1:
        stored_encode = encode()
    elif menu_option == 2:
        decoded = decode(stored_encode)
        temp_encode = ''
        for i in stored_encode:
            temp_encode += str(i)
        print(f'The encoded password is {temp_encode}, and the original password is {decoded}')
    elif menu_option == 3:
        quit()

