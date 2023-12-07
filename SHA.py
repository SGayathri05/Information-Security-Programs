import hashlib

str = input("Enter the value: ")

result = hashlib.sha256(str.encode())
print("Sha 256 ", result.hexdigest())

result = hashlib.sha512(str.encode())
print("Sha 512 ", result.hexdigest())

result = hashlib.sha384(str.encode())
print("Sha 384 ", result.hexdigest())

result = hashlib.sha224(str.encode())
print("Sha 224 ", result.hexdigest())
