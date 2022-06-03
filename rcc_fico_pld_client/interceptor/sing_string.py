# coding: utf-8

from __future__ import absolute_import

from rcc_fico_pld_client.interceptor.key_handler import KeyHandler

import configparser

class SingString(object):

    key_password = ""
    pathKeypair = ""
    pathCertificateCdc = ""
    
    def sing(self,text):      
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.key_password= config['CERTIFICATEINFO']['key_password']
        self.pathKeypair= config['CERTIFICATEINFO']['pathKeypair']
        self.pathCertificateCdc= config['CERTIFICATEINFO']['pathCertificateCdc']


        print(config.items())
        key_handler = KeyHandler(self.pathKeypair,self.pathCertificateCdc,self.key_password)
        signature = key_handler.get_signature_from_private_key(text)
        return signature

    def veify(self,text,sing):        
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.key_password= config['CERTIFICATEINFO']['key_password']
        self.pathKeypair= config['CERTIFICATEINFO']['pathKeypair']
        self.pathCertificateCdc= config['CERTIFICATEINFO']['pathCertificateCdc']

        key_handler = KeyHandler(self.pathKeypair,self.pathCertificateCdc,self.key_password)
        try:
            validate = key_handler.get_verification_from_public_key(text, sing)
        except Exception as e:        
            validate = False
        return validate