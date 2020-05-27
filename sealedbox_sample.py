# -*- coding: utf-8 -*-
"""PyNaCl SealedBox encrypt/decrypt sample code."""

from nacl.public import PrivateKey
from nacl.public import SealedBox
from nacl.encoding import Base64Encoder


prikey = PrivateKey.generate()
pubkey = prikey.public_key

message = 'abcdefg1234'
encoding = 'utf-8'

print('-'*100)
print('KEY and MESSAGE')
print('-'*100)
print('PRIKEY:', prikey)
print('PRIKEY(BASE64):', prikey.encode(Base64Encoder).decode(encoding))
print('PUBKEY:', pubkey)
print('PUBKEY(BASE64):', pubkey.encode(Base64Encoder).decode(encoding))
print('MESSAGE:', message)

print('-'*100)
print('ENCRYPT with public key')
print('-'*100)

box = SealedBox(pubkey)
encrypted = box.encrypt(message.encode(encoding=encoding))
print('ENCRYPTED MESSAGE:', encrypted)
print('ENCRYPTED MESSAGE(BASE64):', Base64Encoder.encode(encrypted).decode(encoding))

print('-'*100)
print('DECRYPT with private key')
print('-'*100)

box = SealedBox(prikey)
decrypted = box.decrypt(encrypted).decode(encoding=encoding)
print('DECRYPTED MESSAGE:', decrypted)
