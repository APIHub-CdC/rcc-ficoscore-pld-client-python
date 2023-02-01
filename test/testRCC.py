# coding: utf-8

from __future__ import absolute_import

import unittest

import rcc_fico_pld_client
from rcc_fico_pld_client.interceptor.key_handler import KeyHandler
from rcc_fico_pld_client.api.reporte_de_crdito_consolidado_fico_score_y_pld_api import ReporteDeCrditoConsolidadoFICOScoreYPLDApi
from rcc_fico_pld_client.api_client import ApiClient
from rcc_fico_pld_client.configuration import Configuration
from rcc_fico_pld_client.models.can import CAN
from rcc_fico_pld_client.models.catalogo_tipo_asentamiento import CatalogoTipoAsentamiento
from rcc_fico_pld_client.models.catalogo_tipo_domicilio import CatalogoTipoDomicilio
from rcc_fico_pld_client.models.domicilio_peticion import DomicilioPeticion
from rcc_fico_pld_client.models.persona_peticion import PersonaPeticion  # noqa: E501
from rcc_fico_pld_client.rest import ApiException
import uuid

import configparser

class TestRCC(unittest.TestCase):
    
    x_api_key = ""
    host = ""
    username = ""
    password = ""


    def setUp(self):
        
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.host = self.key_password= config['API_CONFIG']['host']
        self.x_api_key = self.key_password= config['API_CONFIG']['x_api_key']
        self.username = self.key_password= config['API_CONFIG']['username']
        self.password = self.key_password= config['API_CONFIG']['password']
    
        configuration = Configuration(host=self.host)
        self.api = ReporteDeCrditoConsolidadoFICOScoreYPLDApi(ApiClient(configuration))  # noqa: E501

    def test_reporte(self):
        body = PersonaPeticion(
            apellido_paterno="APELLIDO_PATERNO",
            apellido_materno="APELLIDO_MATERNO",
            apellido_adicional=None,
            primer_nombre="PRIMER_NOMBRE",
            segundo_nombre=None,
            fecha_nacimiento="YYYY-MM-DD",
            rfc="RFC",
            curp=None,
            nacionalidad="mx",
            residencia=None,
            estado_civil=None,
            sexo=None,
            clave_elector_ife=None,
            numero_dependientes=None,
            fecha_defuncion=None,
            domicilio=DomicilioPeticion( 
                direccion="DIRECCION",
                colonia_poblacion="COLONIA", 
                delegacion_municipio="MUNICIPIO", 
                ciudad= "CIUDAD", 
                estado="ESTADO", 
                cp="CODIGO_POSTAL", 
                fecha_residencia="YYYY-MM-DD", 
                numero_telefono=None, 
                tipo_domicilio=None, 
                tipo_asentamiento=None)
        )
        try:
   
            api_response=self.api.get_reporte( x_api_key=self.x_api_key, username=self.username, password=self.password, request=body)
            print(api_response)
        except ApiException as e:
            print("Exception when calling TestRCC->test_reporte: %s\n" % e)


if __name__ == '__main__':
    unittest.main()
