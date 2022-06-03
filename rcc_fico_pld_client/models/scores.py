# coding: utf-8




import pprint
import re  # noqa: F401

import six

from rcc_fico_pld_client.configuration import Configuration


class Scores(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'scores': 'list[Score]'
    }

    attribute_map = {
        'scores': 'scores'
    }

    def __init__(self, scores=None, _configuration=None):  # noqa: E501
        """Scores - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._scores = None
        self.discriminator = None

        if scores is not None:
            self.scores = scores

    @property
    def scores(self):
        """Gets the scores of this Scores.  # noqa: E501


        :return: The scores of this Scores.  # noqa: E501
        :rtype: list[Score]
        """
        return self._scores

    @scores.setter
    def scores(self, scores):
        """Sets the scores of this Scores.


        :param scores: The scores of this Scores.  # noqa: E501
        :type: list[Score]
        """

        self._scores = scores

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
        if issubclass(Scores, dict):
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
        if not isinstance(other, Scores):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Scores):
            return True

        return self.to_dict() != other.to_dict()
