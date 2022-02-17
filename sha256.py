from hashlib import sha256
from secrets import compare_digest

sha256_digest_1 = sha256(b'sha256 hashed message')
digest_1 = sha256_digest_1.digest()
hexdigest_1 = sha256_digest_1.hexdigest()

sha256_digest_2 = sha256()
sha256_digest_2.update(b'sha256') 
sha256_digest_2.update(b' hashed') 
sha256_digest_2.update(b' message')
digest_2 = sha256_digest_2.digest()
hexdigest_2 = sha256_digest_2.hexdigest()

print(compare_digest(digest_1, digest_2))
print(compare_digest(hexdigest_1, hexdigest_2))