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

class ContactRead(object):
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
        'platform': 'object',
        'platform_resource_identifier': 'object',
        'name': 'object',
        'aiod_entry': 'AIoDEntryRead',
        'email': 'object',
        'location': 'object',
        'organisation': 'object',
        'person': 'object',
        'telephone': 'object',
        'identifier': 'object'
    }

    attribute_map = {
        'platform': 'platform',
        'platform_resource_identifier': 'platform_resource_identifier',
        'name': 'name',
        'aiod_entry': 'aiod_entry',
        'email': 'email',
        'location': 'location',
        'organisation': 'organisation',
        'person': 'person',
        'telephone': 'telephone',
        'identifier': 'identifier'
    }

    def __init__(self, platform=None, platform_resource_identifier=None, name=None, aiod_entry=None, email=None, location=None, organisation=None, person=None, telephone=None, identifier=None):  # noqa: E501
        """ContactRead - a model defined in Swagger"""  # noqa: E501
        self._platform = None
        self._platform_resource_identifier = None
        self._name = None
        self._aiod_entry = None
        self._email = None
        self._location = None
        self._organisation = None
        self._person = None
        self._telephone = None
        self._identifier = None
        self.discriminator = None
        if platform is not None:
            self.platform = platform
        if platform_resource_identifier is not None:
            self.platform_resource_identifier = platform_resource_identifier
        if name is not None:
            self.name = name
        if aiod_entry is not None:
            self.aiod_entry = aiod_entry
        if email is not None:
            self.email = email
        if location is not None:
            self.location = location
        if organisation is not None:
            self.organisation = organisation
        if person is not None:
            self.person = person
        if telephone is not None:
            self.telephone = telephone
        self.identifier = identifier

    @property
    def platform(self):
        """Gets the platform of this ContactRead.  # noqa: E501

        The external platform from which this resource originates. Leave empty if this item originates from AIoD. If platform is not None, the platform_resource_identifier should be set as well.  # noqa: E501

        :return: The platform of this ContactRead.  # noqa: E501
        :rtype: object
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ContactRead.

        The external platform from which this resource originates. Leave empty if this item originates from AIoD. If platform is not None, the platform_resource_identifier should be set as well.  # noqa: E501

        :param platform: The platform of this ContactRead.  # noqa: E501
        :type: object
        """

        self._platform = platform

    @property
    def platform_resource_identifier(self):
        """Gets the platform_resource_identifier of this ContactRead.  # noqa: E501

        A unique identifier issued by the external platform that's specified in 'platform'. Leave empty if this item is not part of an external platform.  # noqa: E501

        :return: The platform_resource_identifier of this ContactRead.  # noqa: E501
        :rtype: object
        """
        return self._platform_resource_identifier

    @platform_resource_identifier.setter
    def platform_resource_identifier(self, platform_resource_identifier):
        """Sets the platform_resource_identifier of this ContactRead.

        A unique identifier issued by the external platform that's specified in 'platform'. Leave empty if this item is not part of an external platform.  # noqa: E501

        :param platform_resource_identifier: The platform_resource_identifier of this ContactRead.  # noqa: E501
        :type: object
        """

        self._platform_resource_identifier = platform_resource_identifier

    @property
    def name(self):
        """Gets the name of this ContactRead.  # noqa: E501


        :return: The name of this ContactRead.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContactRead.


        :param name: The name of this ContactRead.  # noqa: E501
        :type: object
        """

        self._name = name

    @property
    def aiod_entry(self):
        """Gets the aiod_entry of this ContactRead.  # noqa: E501


        :return: The aiod_entry of this ContactRead.  # noqa: E501
        :rtype: AIoDEntryRead
        """
        return self._aiod_entry

    @aiod_entry.setter
    def aiod_entry(self, aiod_entry):
        """Sets the aiod_entry of this ContactRead.


        :param aiod_entry: The aiod_entry of this ContactRead.  # noqa: E501
        :type: AIoDEntryRead
        """

        self._aiod_entry = aiod_entry

    @property
    def email(self):
        """Gets the email of this ContactRead.  # noqa: E501

        An email address.  # noqa: E501

        :return: The email of this ContactRead.  # noqa: E501
        :rtype: object
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactRead.

        An email address.  # noqa: E501

        :param email: The email of this ContactRead.  # noqa: E501
        :type: object
        """

        self._email = email

    @property
    def location(self):
        """Gets the location of this ContactRead.  # noqa: E501


        :return: The location of this ContactRead.  # noqa: E501
        :rtype: object
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ContactRead.


        :param location: The location of this ContactRead.  # noqa: E501
        :type: object
        """

        self._location = location

    @property
    def organisation(self):
        """Gets the organisation of this ContactRead.  # noqa: E501


        :return: The organisation of this ContactRead.  # noqa: E501
        :rtype: object
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this ContactRead.


        :param organisation: The organisation of this ContactRead.  # noqa: E501
        :type: object
        """

        self._organisation = organisation

    @property
    def person(self):
        """Gets the person of this ContactRead.  # noqa: E501


        :return: The person of this ContactRead.  # noqa: E501
        :rtype: object
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this ContactRead.


        :param person: The person of this ContactRead.  # noqa: E501
        :type: object
        """

        self._person = person

    @property
    def telephone(self):
        """Gets the telephone of this ContactRead.  # noqa: E501

        A telephone number, including the land code.  # noqa: E501

        :return: The telephone of this ContactRead.  # noqa: E501
        :rtype: object
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this ContactRead.

        A telephone number, including the land code.  # noqa: E501

        :param telephone: The telephone of this ContactRead.  # noqa: E501
        :type: object
        """

        self._telephone = telephone

    @property
    def identifier(self):
        """Gets the identifier of this ContactRead.  # noqa: E501


        :return: The identifier of this ContactRead.  # noqa: E501
        :rtype: object
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ContactRead.


        :param identifier: The identifier of this ContactRead.  # noqa: E501
        :type: object
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

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
        if issubclass(ContactRead, dict):
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
        if not isinstance(other, ContactRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
