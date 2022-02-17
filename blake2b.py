from hashlib import blake2b

# data = b'Message for transmission'

# blake = blake2b(data, digest_size=32)
# print('Printing blake digest: ')
# print(blake.digest())
# print('Printing blake hexadecimal digest: ')
# print(blake.hexdigest())

blake = blake2b(key=b'keys', digest_size=60)
blake.update(b'Blake message')
blake_digest = blake.digest()
blake_hexdigest = blake.hexdigest()

print('Blake digest: ', blake_digest)
print('Blake hexdigest: ', blake_hexdigest)