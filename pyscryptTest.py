import hashlib, secrets

passwrd = b'not a number'
salt = secrets.token_bytes(32)

scrypt_key = hashlib.scrypt(password=passwrd, salt=salt, n=16384, r=8, p=1, dklen=32)
print('Salt: ', salt)
print('Key: ', scrypt_key)