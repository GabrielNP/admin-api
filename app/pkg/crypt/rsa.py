from base64 import b64encode, b64decode

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

class Crypt(object):
    PRIVATE_KEY_FILE_PATH = 'private.pem'
    PUBLIC_KEY_FILE_PATH = 'public.pem'

    def __init__(self, message: str):
        self.message = message

    def __get_public_key(self) -> str:
        with open(self.PUBLIC_KEY_FILE_PATH, 'r') as _file:
            return _file.read()

    def __get_private_key(self) -> str:
        with open(self.PRIVATE_KEY_FILE_PATH, 'r') as _file:
            return _file.read()
    
    def __get_cipher(self, key_type: str):
        file = self.__get_private_key() if key_type == 'private' else self.__get_public_key()
        key = RSA.importKey(file)
        return PKCS1_v1_5.new(key)

    def encrypt(self):
        """Encrypt and Encode (base64) a raw message."""
        cipher = self.__get_cipher('public')
        encrypted_message = cipher.encrypt(self.message.encode('utf-8'))
        encoded_message = b64encode(encrypted_message).decode('ascii')
        return encoded_message

    def decrypt(self):
        """Decode and decrypt a encoded encrypted message."""
        cipher = self.__get_cipher('private')
        decoded_encrypted_message = b64decode(self.message)
        decrypted_message = cipher.decrypt(decoded_encrypted_message, b'decryption failed')
        return decrypted_message
