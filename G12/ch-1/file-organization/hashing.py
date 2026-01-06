import hashlib

# Original data
text = "Hello World"

# Encode as UTF-8 then generate hash with SHA256
hash_object = hashlib.sha256(text.encode())

# Print Hash as hex format
hash_hex = hash_object.hexdigest()

print("---------------------------------------------------------------------------------------------------")
print("Original text :", text)
print("SHA256 Hash    :", hash_hex)
print("---------------------------------------------------------------------------------------------------")


print("--------------------------------------Different Hash Algorithms------------------------------------")
print("---------------------------------------------------------------------------------------------------")

print(hashlib.md5(text.encode()).hexdigest())        # MD5 (128 bit)
print(hashlib.sha1(text.encode()).hexdigest())       # SHA-1 (160 bit)
print(hashlib.sha256(text.encode()).hexdigest())     # SHA-256 (256 bit)
print(hashlib.sha512(text.encode()).hexdigest())     # SHA-512 (512 bit)

print("---------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------")