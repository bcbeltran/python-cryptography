from Crypto.Hash import Poly1305
from Crypto.Cipher import AES

key = b'The key size has to be 32 bytes!'
mac = Poly1305.new(key=key, cipher=AES)
mac.update(b'message to be delivered')
mac_nonce = mac.nonce
mac_hex_digest = mac.hexdigest()
print('Poly1305 nonce: ', mac_nonce)
print('Poly1305 hex_digest: ', mac_hex_digest)

mac_verify = Poly1305.new(key=key, nonce=mac_nonce, cipher=AES, data=b'mesage to be delivered')
try:
    mac_verify.hexverify(mac_hex_digest)
    print('The message is authentic')
except:
    print('The message cannot be authenticated')