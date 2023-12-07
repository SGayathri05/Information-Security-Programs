def combinations_cipher(message, key):
    message = message.lower()
    message = ''.join(c for c in message if c.isalpha())

    encrypted_message = ''
    for i in range(0, len(message), key):
        encrypted_message += message[i:i+key][::-1]
    return encrypted_message


def combinations_decipher(encrypted_message, key):
    decrypted_message = ''
    for i in range(0, len(encrypted_message), key):
        decrypted_message += encrypted_message[i:i+key][::-1]
    return decrypted_message

message = input("Enter the message: ")
key = int(input("Enter the key: "))

# Encrypt the message
encrypted_message = combinations_cipher(message, key)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = combinations_decipher(encrypted_message, key)
print("Decrypted message:", decrypted_message)
