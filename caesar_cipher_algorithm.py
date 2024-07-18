alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(plain_text,shift_key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            position = alphabets.index(char)
            new_position = ( position + shift_key ) % 26
            new_char = alphabets[new_position]
            if is_upper:
                new_char = new_char.upper()
            cipher_text += new_char
        else :
            cipher_text += char
    return cipher_text


def decryption(cipher_text,shift_key):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            position = alphabets.index(char)
            new_position = (position - shift_key ) % 26
            new_char = alphabets[new_position] 
            if is_upper:
                new_char = new_char.upper()
            plain_text += new_char
        else :
            plain_text += char
    return plain_text


end_session = True
while end_session:

    ask_the_user = input("Type 'encrypt' for Encryption and 'decrypt' for Decryption\n").lower()

    if ask_the_user not in ["encrypt" , "decrypt"]:
        print("Invalid input!\n")
        continue

    text = input("Enter the message : ")
    
    while True:
        try:
            shift_value = int(input("Enter the shift value : "))
            break
        except ValueError:
            print("Invalid input! You must enter an integer number (better ranging from 0-25).\n")
    

    if ask_the_user == "encrypt":
        encrypted_message = encryption(text,shift_value)
        print(f"The encrypted message is : {encrypted_message}")
    elif ask_the_user == "decrypt":
        decrypted_message = decryption(text,shift_value)
        print(f"The decrypted message is : {decrypted_message}")

    while True:
        choose  = input("Type 'yes' to continue and 'no' to stop\n").lower()
        if choose in ['yes' or 'no']:
            break
        else :
            print("Invalid input! Please type 'yes' or 'no'.\n")

    if choose == 'no':
        end_session = False
        print("Thank you. Have a nice day!\n") 

#end of the code