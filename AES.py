pip install pycryptodome

from Crypto.Cipher import AES
key = b'H@m)ghji&QWaT@fG'

cipher = AES.new(key, AES.MODE_EAX)
data = input("Enter the data: ").encode()
nonce = cipher.nonce

cipher_text = cipher.encrypt(data)
print("Cipher text = ", cipher_text)

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plain_text = cipher.decrypt(cipher_text)
print("Plain text= ", plain_text)
