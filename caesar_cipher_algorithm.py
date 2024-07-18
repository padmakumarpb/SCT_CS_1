alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(plain_text,shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = ( position + shift_key ) % 26
            cipher_text = cipher_text + alphabets[new_position]
        else :
            cipher_text += char
    return cipher_text


def decryption(cipher_text,shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - shift_key ) % 26
            plain_text = plain_text + alphabets[new_position] 
        else :
            plain_text += char
    return plain_text


end_session = True
while end_session:
    ask_the_user = input("Type 'encrypt' for Encryption and 'decrypt' for Decryption\n").lower()

    text = input("Enter the message : ").lower()

    shift_value = int(input("Enter the shift value : "))

    if ask_the_user == "encrypt":
        encrypted_message = encryption(text,shift_value)
        print(f"The encrypted message is : {encrypted_message}")
    elif ask_the_user == "decrypt":
        decrypted_message = decryption(text,shift_value)
        print(f"The decrypted message is : {decrypted_message}")

    choose  = input("Type 'yes' to continue and 'no' to stop\n").lower()
    if choose == 'no':
        end_session = False
        print("Thank you. Have a nice day!\n")

