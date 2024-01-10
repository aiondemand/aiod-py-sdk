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

class Geo(object):
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
        'latitude': 'object',
        'longitude': 'object',
        'elevation_millimeters': 'object'
    }

    attribute_map = {
        'latitude': 'latitude',
        'longitude': 'longitude',
        'elevation_millimeters': 'elevation_millimeters'
    }

    def __init__(self, latitude=None, longitude=None, elevation_millimeters=None):  # noqa: E501
        """Geo - a model defined in Swagger"""  # noqa: E501
        self._latitude = None
        self._longitude = None
        self._elevation_millimeters = None
        self.discriminator = None
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if elevation_millimeters is not None:
            self.elevation_millimeters = elevation_millimeters

    @property
    def latitude(self):
        """Gets the latitude of this Geo.  # noqa: E501

        The latitude of a location in degrees (WGS84)  # noqa: E501

        :return: The latitude of this Geo.  # noqa: E501
        :rtype: object
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Geo.

        The latitude of a location in degrees (WGS84)  # noqa: E501

        :param latitude: The latitude of this Geo.  # noqa: E501
        :type: object
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Geo.  # noqa: E501

        The longitude of a location in degrees (WGS84)  # noqa: E501

        :return: The longitude of this Geo.  # noqa: E501
        :rtype: object
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Geo.

        The longitude of a location in degrees (WGS84)  # noqa: E501

        :param longitude: The longitude of this Geo.  # noqa: E501
        :type: object
        """

        self._longitude = longitude

    @property
    def elevation_millimeters(self):
        """Gets the elevation_millimeters of this Geo.  # noqa: E501

        The elevation in millimeters with tespect to the WGS84 ellipsoid  # noqa: E501

        :return: The elevation_millimeters of this Geo.  # noqa: E501
        :rtype: object
        """
        return self._elevation_millimeters

    @elevation_millimeters.setter
    def elevation_millimeters(self, elevation_millimeters):
        """Sets the elevation_millimeters of this Geo.

        The elevation in millimeters with tespect to the WGS84 ellipsoid  # noqa: E501

        :param elevation_millimeters: The elevation_millimeters of this Geo.  # noqa: E501
        :type: object
        """

        self._elevation_millimeters = elevation_millimeters

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
        if issubclass(Geo, dict):
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
        if not isinstance(other, Geo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
