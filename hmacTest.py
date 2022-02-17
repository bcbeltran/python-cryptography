import hmac, hashlib

data = b'Message for HMAC'
key = b'keyed-version'

hmac_code = hmac.new(key=key, msg=data, digestmod=hashlib.sha3_256)
hmac_digest = hmac_code.digest()
hmac_hexdigest = hmac_code.hexdigest()

print('HMAC digest: ', hmac_digest)
print('HMAC hexdigest: ', hmac_hexdigest)