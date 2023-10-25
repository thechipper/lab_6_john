#encoder
def decode(x):
    num_string = x
    num_list = []
    for i in num_string:
        num_list.append(str(int(i) + 3))
    num_string = ''.join(num_list)
    return num_string

while True:
    menu_option = int(input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\n\nPlease enter an option: "))

    if menu_option == 1:
        stored_encode = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!\n\n")
    elif menu_option == 2:
        decode_value = decode(stored_encode)
        print(f"The encoded password is {decode_value} and the original password is {stored_encode}\n\n")
    elif menu_option == 3:
        quit()