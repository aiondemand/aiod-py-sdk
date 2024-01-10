# coding: utf-8

"""
    FastAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class VCardOrganisation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'object',
        'type': 'object',
        'vcardfn': 'object'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'vcardfn': 'vcard:fn'
    }

    def __init__(self, id=None, type=None, vcardfn=None):  # noqa: E501
        """VCardOrganisation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._vcardfn = None
        self.discriminator = None
        self.id = id
        if type is not None:
            self.type = type
        self.vcardfn = vcardfn

    @property
    def id(self):
        """Gets the id of this VCardOrganisation.  # noqa: E501


        :return: The id of this VCardOrganisation.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VCardOrganisation.


        :param id: The id of this VCardOrganisation.  # noqa: E501
        :type: object
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this VCardOrganisation.  # noqa: E501


        :return: The type of this VCardOrganisation.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VCardOrganisation.


        :param type: The type of this VCardOrganisation.  # noqa: E501
        :type: object
        """

        self._type = type

    @property
    def vcardfn(self):
        """Gets the vcardfn of this VCardOrganisation.  # noqa: E501

        The formatted text corresponding to the name of the object  # noqa: E501

        :return: The vcardfn of this VCardOrganisation.  # noqa: E501
        :rtype: object
        """
        return self._vcardfn

    @vcardfn.setter
    def vcardfn(self, vcardfn):
        """Sets the vcardfn of this VCardOrganisation.

        The formatted text corresponding to the name of the object  # noqa: E501

        :param vcardfn: The vcardfn of this VCardOrganisation.  # noqa: E501
        :type: object
        """
        if vcardfn is None:
            raise ValueError("Invalid value for `vcardfn`, must not be `None`")  # noqa: E501

        self._vcardfn = vcardfn

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
        if issubclass(VCardOrganisation, dict):
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
        if not isinstance(other, VCardOrganisation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
