#encoder
while True:
    menu_option = int(input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\n\nPlease enter an option: "))

    if menu_option == 1:
        stored_encode = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!\n\n")
    elif menu_option == 2:
        pass

    elif menu_option == 3:
        quit()

