import rsa


(pubkey, privkey) = rsa.newkeys(512)
message = 'Keep calm and learn Python'.encode('utf8')
crypto = rsa.encrypt(message, pubkey)
print(crypto)
message = rsa.decrypt(crypto, privkey)
print(message.decode('utf8'))