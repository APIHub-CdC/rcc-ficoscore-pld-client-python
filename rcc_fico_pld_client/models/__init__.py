# coding: utf-8

# flake8: noqa
"""
    Reporte de Crédito Consolidado, FICO® Score y PLD 

    <p>Esta API reporta: el historial crediticio; el cumplimiento de pago de los compromisos que la persona ha adquirido con entidades financieras, no financieras e instituciones comerciales que dan crédito o participan en actividades afines al crédito; y filtra contra listas de cumplimiento para Prevención de Lavado de Dinero. En esta versión se retornan los campos del Crédito Asociado a Nomina (CAN) en el nodo de créditos.<br/><img src='https://developer.circulodecredito.com.mx/sites/default/files/2020-10/circulo_de_credito-apihub.png' height='40' width='220'/></p><br/>  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: api@circulodecredito.com.mx
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from rcc_fico_pld_client.models.can import CAN
from rcc_fico_pld_client.models.catalogo_estado_civil import CatalogoEstadoCivil
from rcc_fico_pld_client.models.catalogo_estados import CatalogoEstados
from rcc_fico_pld_client.models.catalogo_frecuencia_pago import CatalogoFrecuenciaPago
from rcc_fico_pld_client.models.catalogo_moneda import CatalogoMoneda
from rcc_fico_pld_client.models.catalogo_nacionalidad import CatalogoNacionalidad
from rcc_fico_pld_client.models.catalogo_prevencion import CatalogoPrevencion
from rcc_fico_pld_client.models.catalogo_razones import CatalogoRazones
from rcc_fico_pld_client.models.catalogo_residencia import CatalogoResidencia
from rcc_fico_pld_client.models.catalogo_sexo import CatalogoSexo
from rcc_fico_pld_client.models.catalogo_tipo_asentamiento import CatalogoTipoAsentamiento
from rcc_fico_pld_client.models.catalogo_tipo_credito import CatalogoTipoCredito
from rcc_fico_pld_client.models.catalogo_tipo_cuenta import CatalogoTipoCuenta
from rcc_fico_pld_client.models.catalogo_tipo_domicilio import CatalogoTipoDomicilio
from rcc_fico_pld_client.models.catalogo_tipo_responsabilidad import CatalogoTipoResponsabilidad
from rcc_fico_pld_client.models.consulta import Consulta
from rcc_fico_pld_client.models.consultas import Consultas
from rcc_fico_pld_client.models.credito import Credito
from rcc_fico_pld_client.models.creditos import Creditos
from rcc_fico_pld_client.models.domicilio_peticion import DomicilioPeticion
from rcc_fico_pld_client.models.domicilio_respuesta import DomicilioRespuesta
from rcc_fico_pld_client.models.domicilios_respuesta import DomiciliosRespuesta
from rcc_fico_pld_client.models.empleo import Empleo
from rcc_fico_pld_client.models.empleos import Empleos
from rcc_fico_pld_client.models.error import Error
from rcc_fico_pld_client.models.errores import Errores
from rcc_fico_pld_client.models.mensaje import Mensaje
from rcc_fico_pld_client.models.mensajes import Mensajes
from rcc_fico_pld_client.models.persona_peticion import PersonaPeticion
from rcc_fico_pld_client.models.persona_respuesta import PersonaRespuesta
from rcc_fico_pld_client.models.respuesta import Respuesta
from rcc_fico_pld_client.models.score import Score
from rcc_fico_pld_client.models.scores import Scores
