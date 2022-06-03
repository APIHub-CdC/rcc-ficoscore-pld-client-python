# coding: utf-8



import pprint
import re  # noqa: F401

import six

from rcc_fico_pld_client.configuration import Configuration


class Respuesta(object):
   

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'folio_consulta': 'str',
        'folio_consulta_otorgante': 'str',
        'clave_otorgante': 'str',
        'declaraciones_consumidor': 'str',
        'persona': 'PersonaRespuesta',
        'consultas': 'list[Consulta]',
        'creditos': 'list[Credito]',
        'domicilios': 'list[DomicilioRespuesta]',
        'empleos': 'list[Empleo]',
        'scores': 'list[Score]',
        'mensajes': 'list[Mensaje]'
    }

    attribute_map = {
        'folio_consulta': 'folioConsulta',
        'folio_consulta_otorgante': 'folioConsultaOtorgante',
        'clave_otorgante': 'claveOtorgante',
        'declaraciones_consumidor': 'declaracionesConsumidor',
        'persona': 'persona',
        'consultas': 'consultas',
        'creditos': 'creditos',
        'domicilios': 'domicilios',
        'empleos': 'empleos',
        'scores': 'scores',
        'mensajes': 'mensajes'
    }

    def __init__(self, folio_consulta=None, folio_consulta_otorgante=None, clave_otorgante=None, declaraciones_consumidor=None, persona=None, consultas=None, creditos=None, domicilios=None, empleos=None, scores=None, mensajes=None, _configuration=None):  # noqa: E501
        """Respuesta - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._folio_consulta = None
        self._folio_consulta_otorgante = None
        self._clave_otorgante = None
        self._declaraciones_consumidor = None
        self._persona = None
        self._consultas = None
        self._creditos = None
        self._domicilios = None
        self._empleos = None
        self._scores = None
        self._mensajes = None
        self.discriminator = None

        if folio_consulta is not None:
            self.folio_consulta = folio_consulta
        if folio_consulta_otorgante is not None:
            self.folio_consulta_otorgante = folio_consulta_otorgante
        if clave_otorgante is not None:
            self.clave_otorgante = clave_otorgante
        if declaraciones_consumidor is not None:
            self.declaraciones_consumidor = declaraciones_consumidor
        if persona is not None:
            self.persona = persona
        if consultas is not None:
            self.consultas = consultas
        if creditos is not None:
            self.creditos = creditos
        if domicilios is not None:
            self.domicilios = domicilios
        if empleos is not None:
            self.empleos = empleos
        if scores is not None:
            self.scores = scores
        if mensajes is not None:
            self.mensajes = mensajes

    @property
    def folio_consulta(self):
        """Gets the folio_consulta of this Respuesta.  # noqa: E501

        Folio de la consulta  # noqa: E501

        :return: The folio_consulta of this Respuesta.  # noqa: E501
        :rtype: str
        """
        return self._folio_consulta

    @folio_consulta.setter
    def folio_consulta(self, folio_consulta):
        """Sets the folio_consulta of this Respuesta.

        Folio de la consulta  # noqa: E501

        :param folio_consulta: The folio_consulta of this Respuesta.  # noqa: E501
        :type: str
        """

        self._folio_consulta = folio_consulta

    @property
    def folio_consulta_otorgante(self):
        """Gets the folio_consulta_otorgante of this Respuesta.  # noqa: E501

        Folio de la consulta con relación al otorgante  # noqa: E501

        :return: The folio_consulta_otorgante of this Respuesta.  # noqa: E501
        :rtype: str
        """
        return self._folio_consulta_otorgante

    @folio_consulta_otorgante.setter
    def folio_consulta_otorgante(self, folio_consulta_otorgante):
        """Sets the folio_consulta_otorgante of this Respuesta.

        Folio de la consulta con relación al otorgante  # noqa: E501

        :param folio_consulta_otorgante: The folio_consulta_otorgante of this Respuesta.  # noqa: E501
        :type: str
        """

        self._folio_consulta_otorgante = folio_consulta_otorgante

    @property
    def clave_otorgante(self):
        """Gets the clave_otorgante of this Respuesta.  # noqa: E501

        Clave del otorgante  # noqa: E501

        :return: The clave_otorgante of this Respuesta.  # noqa: E501
        :rtype: str
        """
        return self._clave_otorgante

    @clave_otorgante.setter
    def clave_otorgante(self, clave_otorgante):
        """Sets the clave_otorgante of this Respuesta.

        Clave del otorgante  # noqa: E501

        :param clave_otorgante: The clave_otorgante of this Respuesta.  # noqa: E501
        :type: str
        """

        self._clave_otorgante = clave_otorgante

    @property
    def declaraciones_consumidor(self):
        """Gets the declaraciones_consumidor of this Respuesta.  # noqa: E501


        :return: The declaraciones_consumidor of this Respuesta.  # noqa: E501
        :rtype: str
        """
        return self._declaraciones_consumidor

    @declaraciones_consumidor.setter
    def declaraciones_consumidor(self, declaraciones_consumidor):
        """Sets the declaraciones_consumidor of this Respuesta.


        :param declaraciones_consumidor: The declaraciones_consumidor of this Respuesta.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                declaraciones_consumidor is not None and len(declaraciones_consumidor) > 100):
            raise ValueError("Invalid value for `declaraciones_consumidor`, length must be less than or equal to `100`")  # noqa: E501

        self._declaraciones_consumidor = declaraciones_consumidor

    @property
    def persona(self):
        """Gets the persona of this Respuesta.  # noqa: E501


        :return: The persona of this Respuesta.  # noqa: E501
        :rtype: PersonaRespuesta
        """
        return self._persona

    @persona.setter
    def persona(self, persona):
        """Sets the persona of this Respuesta.


        :param persona: The persona of this Respuesta.  # noqa: E501
        :type: PersonaRespuesta
        """

        self._persona = persona

    @property
    def consultas(self):
        """Gets the consultas of this Respuesta.  # noqa: E501


        :return: The consultas of this Respuesta.  # noqa: E501
        :rtype: list[Consulta]
        """
        return self._consultas

    @consultas.setter
    def consultas(self, consultas):
        """Sets the consultas of this Respuesta.


        :param consultas: The consultas of this Respuesta.  # noqa: E501
        :type: list[Consulta]
        """

        self._consultas = consultas

    @property
    def creditos(self):
        """Gets the creditos of this Respuesta.  # noqa: E501


        :return: The creditos of this Respuesta.  # noqa: E501
        :rtype: list[Credito]
        """
        return self._creditos

    @creditos.setter
    def creditos(self, creditos):
        """Sets the creditos of this Respuesta.


        :param creditos: The creditos of this Respuesta.  # noqa: E501
        :type: list[Credito]
        """

        self._creditos = creditos

    @property
    def domicilios(self):
        """Gets the domicilios of this Respuesta.  # noqa: E501


        :return: The domicilios of this Respuesta.  # noqa: E501
        :rtype: list[DomicilioRespuesta]
        """
        return self._domicilios

    @domicilios.setter
    def domicilios(self, domicilios):
        """Sets the domicilios of this Respuesta.


        :param domicilios: The domicilios of this Respuesta.  # noqa: E501
        :type: list[DomicilioRespuesta]
        """

        self._domicilios = domicilios

    @property
    def empleos(self):
        """Gets the empleos of this Respuesta.  # noqa: E501


        :return: The empleos of this Respuesta.  # noqa: E501
        :rtype: list[Empleo]
        """
        return self._empleos

    @empleos.setter
    def empleos(self, empleos):
        """Sets the empleos of this Respuesta.


        :param empleos: The empleos of this Respuesta.  # noqa: E501
        :type: list[Empleo]
        """

        self._empleos = empleos

    @property
    def scores(self):
        """Gets the scores of this Respuesta.  # noqa: E501


        :return: The scores of this Respuesta.  # noqa: E501
        :rtype: list[Score]
        """
        return self._scores

    @scores.setter
    def scores(self, scores):
        """Sets the scores of this Respuesta.


        :param scores: The scores of this Respuesta.  # noqa: E501
        :type: list[Score]
        """

        self._scores = scores

    @property
    def mensajes(self):
        """Gets the mensajes of this Respuesta.  # noqa: E501


        :return: The mensajes of this Respuesta.  # noqa: E501
        :rtype: list[Mensaje]
        """
        return self._mensajes

    @mensajes.setter
    def mensajes(self, mensajes):
        """Sets the mensajes of this Respuesta.


        :param mensajes: The mensajes of this Respuesta.  # noqa: E501
        :type: list[Mensaje]
        """

        self._mensajes = mensajes

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
        if issubclass(Respuesta, dict):
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
        if not isinstance(other, Respuesta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Respuesta):
            return True

        return self.to_dict() != other.to_dict()
