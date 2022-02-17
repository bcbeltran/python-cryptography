import argon2

password = b'not a number'

argon = argon2.PasswordHasher(time_cost=20, memory_cost=100, parallelism=1, hash_len=16, encoding='utf-8', type=argon2.Type.D)
key = argon.hash(password='not a number')
print(key)

print(argon.verify(key, 'not a number'))
#Returns True
argon.verify(key, 'not a password')
#Raises a VerifyMismatchError