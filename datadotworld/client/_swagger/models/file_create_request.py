# coding: utf-8

"""
    data.world Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FileCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, source=None):
        """
        FileCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'source': 'FileSourceCreateRequest'
        }

        self.attribute_map = {
            'name': 'name',
            'source': 'source'
        }

        self._name = name
        self._source = source

    @property
    def name(self):
        """
        Gets the name of this FileCreateRequest.

        :return: The name of this FileCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FileCreateRequest.

        :param name: The name of this FileCreateRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")
        if name is not None and not re.search('^[^/]+$', name):
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[^/]+$/`")

        self._name = name

    @property
    def source(self):
        """
        Gets the source of this FileCreateRequest.

        :return: The source of this FileCreateRequest.
        :rtype: FileSourceCreateRequest
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this FileCreateRequest.

        :param source: The source of this FileCreateRequest.
        :type: FileSourceCreateRequest
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, FileCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other