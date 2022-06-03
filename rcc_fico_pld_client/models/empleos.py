# coding: utf-8


import pprint
import re  # noqa: F401

import six

from rcc_fico_pld_client.configuration import Configuration


class Empleos(object):
  

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'empleos': 'list[Empleo]'
    }

    attribute_map = {
        'empleos': 'empleos'
    }

    def __init__(self, empleos=None, _configuration=None):  # noqa: E501
        """Empleos - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._empleos = None
        self.discriminator = None

        if empleos is not None:
            self.empleos = empleos

    @property
    def empleos(self):
        """Gets the empleos of this Empleos.  # noqa: E501


        :return: The empleos of this Empleos.  # noqa: E501
        :rtype: list[Empleo]
        """
        return self._empleos

    @empleos.setter
    def empleos(self, empleos):
        """Sets the empleos of this Empleos.


        :param empleos: The empleos of this Empleos.  # noqa: E501
        :type: list[Empleo]
        """

        self._empleos = empleos

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
        if issubclass(Empleos, dict):
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
        if not isinstance(other, Empleos):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Empleos):
            return True

        return self.to_dict() != other.to_dict()
