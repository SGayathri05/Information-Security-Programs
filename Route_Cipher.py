def route_cipher(message, rows, cols):
  message+= ' ' * (rows * cols- len(message))
  grid = [[' ' for _ in range(cols)] for _ in range(rows)]

  for r in range(rows):
    for c in range(cols):
      grid[r][c] = message[r*cols+c]

  ciphertext = ''
  for c in range(cols):
    for r in range(rows):
      ciphertext += grid[r][c]
  
  return ciphertext

def route_cipher_decrypt(ciphertext, rows, cols):
  grid = [[' ' for _ in range(cols)] for _ in range(rows)]

  for r in range(rows):
    for c in range(cols):
      grid[r][c] = ''

  i=0
  for c in range(cols):
    for r in range(rows):
      grid[r][c] = ciphertext[i]
      i = i+1

  plaintext = ''
  for r in range(rows):
    for c in range(cols):
      plaintext += grid[r][c]

  return plaintext.strip()  
  
message = input("Enter the message: ")
ciphertext = route_cipher(message, 3, 4)
print("Cipher text is: ", ciphertext)
print("Plain text is: ", route_cipher_decrypt(ciphertext,3,4))
