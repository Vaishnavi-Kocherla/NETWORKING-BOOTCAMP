import hashlib

string_data = input("Enter string data: ")
result = hashlib.md5(string_data.encode())
print("The hash is ")
print("hash in byte foramt")
print(result.digest())
print("hash in hexadecimal format")
print(result.hexdigest())

print(hashlib.algorithms_available)