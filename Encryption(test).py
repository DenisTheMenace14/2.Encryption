import rsa


def init_keys():
    (pub, priv) = rsa.newkeys(256)
    with open("pub.pem", "wb") as file:
        file.write(pub.save_pkcs1())
    with open("priv.pem", "wb") as file:
        file.write(priv.save_pkcs1())

def encode():
    with open("pub.pem", "rb") as file:
        public = file.read()
    pubkey = rsa.PublicKey.load_pkcs1(public)
    message = 'Hello world!'.encode('utf-8')
    crypto = rsa.encrypt(message, pubkey)
    return crypto

def decode(crypto):
    with open("priv.pem", "rb") as file:
        private = file.read()
    privkey = rsa.PrivateKey.load_pkcs1(private)
    message = rsa.decrypt(crypto, privkey).decode('utf8')
    return message

def start():
    init_keys()
    crypto = encode()
    print(crypto)
    decoded_message=decode(crypto)
    print(decoded_message)

if __name__ == "__main__":
    start()