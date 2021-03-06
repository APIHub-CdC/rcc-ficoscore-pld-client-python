# coding: utf-8

"""
    Reporte de Crédito Consolidado, FICO® Score y PLD 

    <p>Esta API reporta: el historial crediticio; el cumplimiento de pago de los compromisos que la persona ha adquirido con entidades financieras, no financieras e instituciones comerciales que dan crédito o participan en actividades afines al crédito; y filtra contra listas de cumplimiento para Prevención de Lavado de Dinero. En esta versión se retornan los campos del Crédito Asociado a Nomina (CAN) en el nodo de créditos.<br/><img src='https://developer.circulodecredito.com.mx/sites/default/files/2020-10/circulo_de_credito-apihub.png' height='40' width='220'/></p><br/>  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: api@circulodecredito.com.mx
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rcc_fico_pld_client.configuration import Configuration


class CatalogoPrevencion(object):

    """
    allowed enum values
    """
    AD = "AD"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CL = "CL"
    CO = "CO"
    CV = "CV"
    FD = "FD"
    FN = "FN"
    FP = "FP"
    FR = "FR"
    GP = "GP"
    IA = "IA"
    IM = "IM"
    IS = "IS"
    LC = "LC"
    LG = "LG"
    LO = "LO"
    LS = "LS"
    NA = "NA"
    NV = "NV"
    PC = "PC"
    PD = "PD"
    PE = "PE"
    PI = "PI"
    PR = "PR"
    RA = "RA"
    RI = "RI"
    RF = "RF"
    RN = "RN"
    RV = "RV"
    SG = "SG"
    UP = "UP"
    VR = "VR"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self, _configuration=None):  # noqa: E501
        """CatalogoPrevencion - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CatalogoPrevencion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CatalogoPrevencion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogoPrevencion):
            return True

        return self.to_dict() != other.to_dict()
