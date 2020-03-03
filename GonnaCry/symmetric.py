import base64
import hashlib

import generate_keys

from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def _pad(self, s):
        s = s.decode('utf-8')
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
