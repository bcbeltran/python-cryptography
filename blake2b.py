from hashlib import blake2b

data = b'Message for transmission'

blake = blake2b(data, digest_size=32)
print('Printing blake digest: ')
print(blake.digest())
print('Printing blake hexadecimal digest: ')
print(blake.hexdigest())