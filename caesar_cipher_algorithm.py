alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryption(plain_text,shift_key):
    cipher_text = ""
    for char in plain_text:
        position = alphabets.index(char)
        new_position = ( position + shift_key ) % 26
        cipher_text = cipher_text + alphabets[new_position]
    print(f"The encrypted message is : {cipher_text}.")


def decryption(cipher_text,shift_key):
    plain_text = ""
    for char in cipher_text:
        position = alphabets.index(char)
        new_position = (position - shift_key ) % 26
        plain_text = plain_text + alphabets[new_position] 
    print(f"The decrypted message is : {plain_text}.")


ask_the_user = input("Type 'encrypt' for Encryption and 'decrypt' for Decryption\n")

text = input("Enter the message : ")

shift_value = int(input("Enter the shift value : "))


if ask_the_user == "encrypt":
    encryption(text,shift_value)
elif ask_the_user == "decrypt":
    decryption(text,shift_value)

