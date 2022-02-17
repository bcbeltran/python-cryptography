import hashlib
from binascii import hexlify

data = 'Sending encrypted'
data = data.encode('utf-8')

sha3_512 = hashlib.sha3_512(data)
sha3_512_digest = sha3_512.digest()
sha3_512_hex_digest = sha3_512.hexdigest()

print('Printing digest output: ')
print(sha3_512_digest)
print('Printing hexadecimal output: ')
print(sha3_512_hex_digest)
print('Printing binary hexadecimal output: ')
print(hexlify(sha3_512_digest))