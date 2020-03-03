#!/bin/bash/env python
# coding=UTF-8
import os
from os import chmod
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

class assymetric():
    # Constructor
    def __init__(self):
        self.private_key_path = ""
        self.public_key_path = ""
        self.bit_len = 2048
        self.private_key_PEM = None
        self.public_key_PEM = None
        self.key = None


    def generate_keys(self):
        self.key = RSA.generate(self.bit_len)
        self.private_key_PEM = self.key.exportKey('OpenSSH')
        self.public_key_PEM = self.key.publickey().exportKey('OpenSSH')
