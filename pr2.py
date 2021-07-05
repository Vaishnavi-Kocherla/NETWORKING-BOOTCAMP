import hashlib

string_data = input("Enter string data: ")

result_1 = hashlib.md5(string_data.encode())
result_2 = hashlib.sha224(string_data.encode())
result_3 = hashlib.sha1(string_data.encode())

print("the hashes for 3 algorithms are ")

print(result_1.hexdigest())
print(result_2.hexdigest())
print(result_3.hexdigest())


