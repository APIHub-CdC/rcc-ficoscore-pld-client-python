# coding: utf-8

from __future__ import absolute_import

import codecs
import logging
import os

from OpenSSL import crypto
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.x509 import load_pem_x509_certificate


class KeyHandler(object):

    def __init__(self, key_pair_route=None, cdc_cert_route=None, password=None):
        # set logger
        logging.basicConfig(level=logging.NOTSET)
        self.logger = logging.getLogger('KeyHandler')
        # parsing password to bytes
        self.password = bytes(password, encoding='utf8') if password is not None else None
        # set default paths for keys
        self.key_pair_file = os.getcwd()+"/keypair.p12"
        self.cert_file = os.getcwd()+"/cdc_cert.pem"

        self.logger.debug("self.key_pair_file -->"+self.key_pair_file)
        self.logger.debug("self.cert_file -->"+self.cert_file)

        if key_pair_route is not None and cdc_cert_route is not None:
            self.key_pair_file = key_pair_route
            self.cert_file = cdc_cert_route
        self.logger.debug("Key_pair file is at -->"+self.key_pair_file)
        self.logger.debug("CDC_cert file is at -->"+self.cert_file)
        self.private_key = self.__read_pkcs12_private_key()

        if self.private_key is None:
            self.logger.error("Could not load private key")
            raise Exception
        self.certificate = self.__read_certificate()
        if self.certificate is None:
            self.logger.error("Could not load certificate")
            raise Exception

    def __read_pkcs12_private_key(self):
        loaded_pri_key, bytes_pkcs12 = None, None
        with open(self.key_pair_file, "rb") as filepointer:
            bytes_pkcs12 = filepointer.read()
            filepointer.close()
        pkcs12 = crypto.load_pkcs12(bytes_pkcs12, self.password)
        encoded = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())
        loaded_pri_key = serialization.load_pem_private_key(encoded, password=None, backend=default_backend())
        self.logger.info("private key loaded")
        return loaded_pri_key

    def __read_certificate(self):
        loaded_pub_key = None
        with open(self.cert_file, "r") as file_pointer:
            lines = file_pointer.readlines()
            max_lines = len(lines)
            serialized_certificate = ''.join(lines[0:max_lines])
            cert = load_pem_x509_certificate(str.encode(serialized_certificate), default_backend())
            loaded_pub_key = cert.public_key()
        self.logger.info("certificate loaded")
        return loaded_pub_key

    def get_signature_from_private_key(self, to_sign):
        signature_text, payload_bytes = None, None
        if to_sign is None:
            self.logger.error("The parameter to_sign is mandatory")
            raise Exception
        else:
            payload_bytes = bytes(to_sign, encoding='utf8')
        try:
            chosen_hash = hashes.SHA256()
            hasher = hashes.Hash(chosen_hash, default_backend())
            hasher.update(payload_bytes)
            digest = hasher.finalize()
            signature = self.private_key.sign(digest, ec.ECDSA(utils.Prehashed(chosen_hash)))
            signature_text = codecs.encode(signature, 'hex').decode()
            self.logger.info("The signature is: "+signature_text)
        except Exception as error:
            self.logger.error(error)
        return signature_text

    def get_verification_from_public_key(self, to_verify, signature):
        payload_bytes, signature_bytes = None, None
        if to_verify is None:
            self.logger.error("The parameter to_verify is mandatory")
            raise Exception
        else:
            payload_bytes = bytes(to_verify, encoding='utf8')
        if signature is None:
            self.logger.error("The parameter signature is mandatory")
            raise Exception
        else:
            signature_bytes = codecs.decode(signature, 'hex')
        is_verified = None
        try:
            chosen_hash = hashes.SHA256()
            hash = hashes.Hash(chosen_hash, default_backend())
            hash.update(payload_bytes)
            digest = hash.finalize()
            self.certificate.verify(signature_bytes, digest, ec.ECDSA(utils.Prehashed(chosen_hash)))
            is_verified = True
        except Exception as error:
            print(error)
            is_verified = False
        return is_verified
