import hashlib

value = input("Enter the message to be hashed: ")

result1 = hashlib.md5(value.encode())
result2 = hashlib.md5(value.encode())

print("Binary equivalent:", end=" ")
print(result1.digest())

print("Hex equivalent:", end=" ")
print(result2.hexdigest())
