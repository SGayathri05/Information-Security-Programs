alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z']

def polyalphabetic():

  message = input("Msg: ")
  password = input("password: ")
  password = password*len(message)
  cipher_text = ''
  count = 0
  for i in message:
    shift = alphabet.index(password[count])
    letter_index = alphabet.index(i)
    cipher_letter = alphabet[(letter_index + shift)%26]
    cipher_text = cipher_letter + cipher_text
    count = count+1

  return print(f"The encryption is: {cipher_text} \nThe decryption is: ", message)

polyalphabetic()
