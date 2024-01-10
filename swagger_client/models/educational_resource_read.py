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

class EducationalResourceRead(object):
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
        'date_published': 'object',
        'same_as': 'object',
        'time_required': 'object',
        'access_mode': 'object',
        'ai_resource_identifier': 'object',
        'aiod_entry': 'AIoDEntryRead',
        'alternate_name': 'object',
        'application_area': 'object',
        'contact': 'object',
        'content': 'Text',
        'creator': 'object',
        'description': 'Text',
        'educational_level': 'object',
        'has_part': 'object',
        'in_language': 'object',
        'industrial_sector': 'object',
        'is_part_of': 'object',
        'keyword': 'object',
        'location': 'object',
        'media': 'object',
        'note': 'object',
        'pace': 'object',
        'prerequisite': 'object',
        'relevant_link': 'object',
        'relevant_resource': 'object',
        'relevant_to': 'object',
        'research_area': 'object',
        'scientific_domain': 'object',
        'target_audience': 'object',
        'type': 'object',
        'identifier': 'object'
    }

    attribute_map = {
        'platform': 'platform',
        'platform_resource_identifier': 'platform_resource_identifier',
        'name': 'name',
        'date_published': 'date_published',
        'same_as': 'same_as',
        'time_required': 'time_required',
        'access_mode': 'access_mode',
        'ai_resource_identifier': 'ai_resource_identifier',
        'aiod_entry': 'aiod_entry',
        'alternate_name': 'alternate_name',
        'application_area': 'application_area',
        'contact': 'contact',
        'content': 'content',
        'creator': 'creator',
        'description': 'description',
        'educational_level': 'educational_level',
        'has_part': 'has_part',
        'in_language': 'in_language',
        'industrial_sector': 'industrial_sector',
        'is_part_of': 'is_part_of',
        'keyword': 'keyword',
        'location': 'location',
        'media': 'media',
        'note': 'note',
        'pace': 'pace',
        'prerequisite': 'prerequisite',
        'relevant_link': 'relevant_link',
        'relevant_resource': 'relevant_resource',
        'relevant_to': 'relevant_to',
        'research_area': 'research_area',
        'scientific_domain': 'scientific_domain',
        'target_audience': 'target_audience',
        'type': 'type',
        'identifier': 'identifier'
    }

    def __init__(self, platform=None, platform_resource_identifier=None, name=None, date_published=None, same_as=None, time_required=None, access_mode=None, ai_resource_identifier=None, aiod_entry=None, alternate_name=None, application_area=None, contact=None, content=None, creator=None, description=None, educational_level=None, has_part=None, in_language=None, industrial_sector=None, is_part_of=None, keyword=None, location=None, media=None, note=None, pace=None, prerequisite=None, relevant_link=None, relevant_resource=None, relevant_to=None, research_area=None, scientific_domain=None, target_audience=None, type=None, identifier=None):  # noqa: E501
        """EducationalResourceRead - a model defined in Swagger"""  # noqa: E501
        self._platform = None
        self._platform_resource_identifier = None
        self._name = None
        self._date_published = None
        self._same_as = None
        self._time_required = None
        self._access_mode = None
        self._ai_resource_identifier = None
        self._aiod_entry = None
        self._alternate_name = None
        self._application_area = None
        self._contact = None
        self._content = None
        self._creator = None
        self._description = None
        self._educational_level = None
        self._has_part = None
        self._in_language = None
        self._industrial_sector = None
        self._is_part_of = None
        self._keyword = None
        self._location = None
        self._media = None
        self._note = None
        self._pace = None
        self._prerequisite = None
        self._relevant_link = None
        self._relevant_resource = None
        self._relevant_to = None
        self._research_area = None
        self._scientific_domain = None
        self._target_audience = None
        self._type = None
        self._identifier = None
        self.discriminator = None
        if platform is not None:
            self.platform = platform
        if platform_resource_identifier is not None:
            self.platform_resource_identifier = platform_resource_identifier
        self.name = name
        if date_published is not None:
            self.date_published = date_published
        if same_as is not None:
            self.same_as = same_as
        if time_required is not None:
            self.time_required = time_required
        if access_mode is not None:
            self.access_mode = access_mode
        if ai_resource_identifier is not None:
            self.ai_resource_identifier = ai_resource_identifier
        if aiod_entry is not None:
            self.aiod_entry = aiod_entry
        if alternate_name is not None:
            self.alternate_name = alternate_name
        if application_area is not None:
            self.application_area = application_area
        if contact is not None:
            self.contact = contact
        if content is not None:
            self.content = content
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if educational_level is not None:
            self.educational_level = educational_level
        if has_part is not None:
            self.has_part = has_part
        if in_language is not None:
            self.in_language = in_language
        if industrial_sector is not None:
            self.industrial_sector = industrial_sector
        if is_part_of is not None:
            self.is_part_of = is_part_of
        if keyword is not None:
            self.keyword = keyword
        if location is not None:
            self.location = location
        if media is not None:
            self.media = media
        if note is not None:
            self.note = note
        if pace is not None:
            self.pace = pace
        if prerequisite is not None:
            self.prerequisite = prerequisite
        if relevant_link is not None:
            self.relevant_link = relevant_link
        if relevant_resource is not None:
            self.relevant_resource = relevant_resource
        if relevant_to is not None:
            self.relevant_to = relevant_to
        if research_area is not None:
            self.research_area = research_area
        if scientific_domain is not None:
            self.scientific_domain = scientific_domain
        if target_audience is not None:
            self.target_audience = target_audience
        if type is not None:
            self.type = type
        self.identifier = identifier

    @property
    def platform(self):
        """Gets the platform of this EducationalResourceRead.  # noqa: E501

        The external platform from which this resource originates. Leave empty if this item originates from AIoD. If platform is not None, the platform_resource_identifier should be set as well.  # noqa: E501

        :return: The platform of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this EducationalResourceRead.

        The external platform from which this resource originates. Leave empty if this item originates from AIoD. If platform is not None, the platform_resource_identifier should be set as well.  # noqa: E501

        :param platform: The platform of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._platform = platform

    @property
    def platform_resource_identifier(self):
        """Gets the platform_resource_identifier of this EducationalResourceRead.  # noqa: E501

        A unique identifier issued by the external platform that's specified in 'platform'. Leave empty if this item is not part of an external platform.  # noqa: E501

        :return: The platform_resource_identifier of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._platform_resource_identifier

    @platform_resource_identifier.setter
    def platform_resource_identifier(self, platform_resource_identifier):
        """Sets the platform_resource_identifier of this EducationalResourceRead.

        A unique identifier issued by the external platform that's specified in 'platform'. Leave empty if this item is not part of an external platform.  # noqa: E501

        :param platform_resource_identifier: The platform_resource_identifier of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._platform_resource_identifier = platform_resource_identifier

    @property
    def name(self):
        """Gets the name of this EducationalResourceRead.  # noqa: E501


        :return: The name of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EducationalResourceRead.


        :param name: The name of this EducationalResourceRead.  # noqa: E501
        :type: object
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def date_published(self):
        """Gets the date_published of this EducationalResourceRead.  # noqa: E501

        The datetime (utc) on which this resource was first published on an external platform. Note the difference between `.aiod_entry.date_created` and `.date_published`: the former is automatically set to the datetime the resource was created on AIoD, while the latter can optionally be set to an earlier datetime that the resource was published on an external platform.  # noqa: E501

        :return: The date_published of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """Sets the date_published of this EducationalResourceRead.

        The datetime (utc) on which this resource was first published on an external platform. Note the difference between `.aiod_entry.date_created` and `.date_published`: the former is automatically set to the datetime the resource was created on AIoD, while the latter can optionally be set to an earlier datetime that the resource was published on an external platform.  # noqa: E501

        :param date_published: The date_published of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._date_published = date_published

    @property
    def same_as(self):
        """Gets the same_as of this EducationalResourceRead.  # noqa: E501

        Url of a reference Web page that unambiguously indicates this resource's identity.  # noqa: E501

        :return: The same_as of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._same_as

    @same_as.setter
    def same_as(self, same_as):
        """Sets the same_as of this EducationalResourceRead.

        Url of a reference Web page that unambiguously indicates this resource's identity.  # noqa: E501

        :param same_as: The same_as of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._same_as = same_as

    @property
    def time_required(self):
        """Gets the time_required of this EducationalResourceRead.  # noqa: E501

        An approximate or recommendation of the time required to use or complete the educational resource.  # noqa: E501

        :return: The time_required of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._time_required

    @time_required.setter
    def time_required(self, time_required):
        """Sets the time_required of this EducationalResourceRead.

        An approximate or recommendation of the time required to use or complete the educational resource.  # noqa: E501

        :param time_required: The time_required of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._time_required = time_required

    @property
    def access_mode(self):
        """Gets the access_mode of this EducationalResourceRead.  # noqa: E501

        The primary mode of accessing this educational resource.  # noqa: E501

        :return: The access_mode of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this EducationalResourceRead.

        The primary mode of accessing this educational resource.  # noqa: E501

        :param access_mode: The access_mode of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._access_mode = access_mode

    @property
    def ai_resource_identifier(self):
        """Gets the ai_resource_identifier of this EducationalResourceRead.  # noqa: E501

        This resource can be identified by its own identifier, but also by the resource_identifier.  # noqa: E501

        :return: The ai_resource_identifier of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._ai_resource_identifier

    @ai_resource_identifier.setter
    def ai_resource_identifier(self, ai_resource_identifier):
        """Sets the ai_resource_identifier of this EducationalResourceRead.

        This resource can be identified by its own identifier, but also by the resource_identifier.  # noqa: E501

        :param ai_resource_identifier: The ai_resource_identifier of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._ai_resource_identifier = ai_resource_identifier

    @property
    def aiod_entry(self):
        """Gets the aiod_entry of this EducationalResourceRead.  # noqa: E501


        :return: The aiod_entry of this EducationalResourceRead.  # noqa: E501
        :rtype: AIoDEntryRead
        """
        return self._aiod_entry

    @aiod_entry.setter
    def aiod_entry(self, aiod_entry):
        """Sets the aiod_entry of this EducationalResourceRead.


        :param aiod_entry: The aiod_entry of this EducationalResourceRead.  # noqa: E501
        :type: AIoDEntryRead
        """

        self._aiod_entry = aiod_entry

    @property
    def alternate_name(self):
        """Gets the alternate_name of this EducationalResourceRead.  # noqa: E501

        An alias for the item, commonly used for the resource instead of the name.  # noqa: E501

        :return: The alternate_name of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._alternate_name

    @alternate_name.setter
    def alternate_name(self, alternate_name):
        """Sets the alternate_name of this EducationalResourceRead.

        An alias for the item, commonly used for the resource instead of the name.  # noqa: E501

        :param alternate_name: The alternate_name of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._alternate_name = alternate_name

    @property
    def application_area(self):
        """Gets the application_area of this EducationalResourceRead.  # noqa: E501

        The objective of this AI resource.  # noqa: E501

        :return: The application_area of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._application_area

    @application_area.setter
    def application_area(self, application_area):
        """Sets the application_area of this EducationalResourceRead.

        The objective of this AI resource.  # noqa: E501

        :param application_area: The application_area of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._application_area = application_area

    @property
    def contact(self):
        """Gets the contact of this EducationalResourceRead.  # noqa: E501

        Contact information of persons/organisations that can be contacted about this resource.  # noqa: E501

        :return: The contact of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this EducationalResourceRead.

        Contact information of persons/organisations that can be contacted about this resource.  # noqa: E501

        :param contact: The contact of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._contact = contact

    @property
    def content(self):
        """Gets the content of this EducationalResourceRead.  # noqa: E501


        :return: The content of this EducationalResourceRead.  # noqa: E501
        :rtype: Text
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this EducationalResourceRead.


        :param content: The content of this EducationalResourceRead.  # noqa: E501
        :type: Text
        """

        self._content = content

    @property
    def creator(self):
        """Gets the creator of this EducationalResourceRead.  # noqa: E501

        Contact information of persons/organisations that created this resource.  # noqa: E501

        :return: The creator of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this EducationalResourceRead.

        Contact information of persons/organisations that created this resource.  # noqa: E501

        :param creator: The creator of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this EducationalResourceRead.  # noqa: E501


        :return: The description of this EducationalResourceRead.  # noqa: E501
        :rtype: Text
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EducationalResourceRead.


        :param description: The description of this EducationalResourceRead.  # noqa: E501
        :type: Text
        """

        self._description = description

    @property
    def educational_level(self):
        """Gets the educational_level of this EducationalResourceRead.  # noqa: E501

        The level or levels of education for which this resource is intended.  # noqa: E501

        :return: The educational_level of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._educational_level

    @educational_level.setter
    def educational_level(self, educational_level):
        """Sets the educational_level of this EducationalResourceRead.

        The level or levels of education for which this resource is intended.  # noqa: E501

        :param educational_level: The educational_level of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._educational_level = educational_level

    @property
    def has_part(self):
        """Gets the has_part of this EducationalResourceRead.  # noqa: E501


        :return: The has_part of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._has_part

    @has_part.setter
    def has_part(self, has_part):
        """Sets the has_part of this EducationalResourceRead.


        :param has_part: The has_part of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._has_part = has_part

    @property
    def in_language(self):
        """Gets the in_language of this EducationalResourceRead.  # noqa: E501

        The language(s) of the educational resource, in ISO639-3.  # noqa: E501

        :return: The in_language of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._in_language

    @in_language.setter
    def in_language(self, in_language):
        """Sets the in_language of this EducationalResourceRead.

        The language(s) of the educational resource, in ISO639-3.  # noqa: E501

        :param in_language: The in_language of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._in_language = in_language

    @property
    def industrial_sector(self):
        """Gets the industrial_sector of this EducationalResourceRead.  # noqa: E501

        A business domain where a resource is or can be used.  # noqa: E501

        :return: The industrial_sector of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._industrial_sector

    @industrial_sector.setter
    def industrial_sector(self, industrial_sector):
        """Sets the industrial_sector of this EducationalResourceRead.

        A business domain where a resource is or can be used.  # noqa: E501

        :param industrial_sector: The industrial_sector of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._industrial_sector = industrial_sector

    @property
    def is_part_of(self):
        """Gets the is_part_of of this EducationalResourceRead.  # noqa: E501


        :return: The is_part_of of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._is_part_of

    @is_part_of.setter
    def is_part_of(self, is_part_of):
        """Sets the is_part_of of this EducationalResourceRead.


        :param is_part_of: The is_part_of of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._is_part_of = is_part_of

    @property
    def keyword(self):
        """Gets the keyword of this EducationalResourceRead.  # noqa: E501

        Keywords or tags used to describe this resource, providing additional context.  # noqa: E501

        :return: The keyword of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this EducationalResourceRead.

        Keywords or tags used to describe this resource, providing additional context.  # noqa: E501

        :param keyword: The keyword of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._keyword = keyword

    @property
    def location(self):
        """Gets the location of this EducationalResourceRead.  # noqa: E501


        :return: The location of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EducationalResourceRead.


        :param location: The location of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._location = location

    @property
    def media(self):
        """Gets the media of this EducationalResourceRead.  # noqa: E501

        Images or videos depicting the resource or associated with it.   # noqa: E501

        :return: The media of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this EducationalResourceRead.

        Images or videos depicting the resource or associated with it.   # noqa: E501

        :param media: The media of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._media = media

    @property
    def note(self):
        """Gets the note of this EducationalResourceRead.  # noqa: E501

        Notes on this AI resource.  # noqa: E501

        :return: The note of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this EducationalResourceRead.

        Notes on this AI resource.  # noqa: E501

        :param note: The note of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._note = note

    @property
    def pace(self):
        """Gets the pace of this EducationalResourceRead.  # noqa: E501

        The high-level study schedule available for this educational resource. \"self-paced\" is mostly used for MOOCS, Tutorials and short courses without interactive elements; \"scheduled\" is used for scheduled courses with interactive elements that is not a full-time engagement; \"full-time\" is used for programmes or intensive courses that require a full-time engagement from the student.  # noqa: E501

        :return: The pace of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._pace

    @pace.setter
    def pace(self, pace):
        """Sets the pace of this EducationalResourceRead.

        The high-level study schedule available for this educational resource. \"self-paced\" is mostly used for MOOCS, Tutorials and short courses without interactive elements; \"scheduled\" is used for scheduled courses with interactive elements that is not a full-time engagement; \"full-time\" is used for programmes or intensive courses that require a full-time engagement from the student.  # noqa: E501

        :param pace: The pace of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._pace = pace

    @property
    def prerequisite(self):
        """Gets the prerequisite of this EducationalResourceRead.  # noqa: E501

        Minimum or recommended requirements to make use of this educational resource.  # noqa: E501

        :return: The prerequisite of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._prerequisite

    @prerequisite.setter
    def prerequisite(self, prerequisite):
        """Sets the prerequisite of this EducationalResourceRead.

        Minimum or recommended requirements to make use of this educational resource.  # noqa: E501

        :param prerequisite: The prerequisite of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._prerequisite = prerequisite

    @property
    def relevant_link(self):
        """Gets the relevant_link of this EducationalResourceRead.  # noqa: E501

        URLs of relevant resources. These resources should not be part of AIoD (use relevant_resource otherwise). This field should only be used if there is no more specific field.  # noqa: E501

        :return: The relevant_link of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._relevant_link

    @relevant_link.setter
    def relevant_link(self, relevant_link):
        """Sets the relevant_link of this EducationalResourceRead.

        URLs of relevant resources. These resources should not be part of AIoD (use relevant_resource otherwise). This field should only be used if there is no more specific field.  # noqa: E501

        :param relevant_link: The relevant_link of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._relevant_link = relevant_link

    @property
    def relevant_resource(self):
        """Gets the relevant_resource of this EducationalResourceRead.  # noqa: E501


        :return: The relevant_resource of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._relevant_resource

    @relevant_resource.setter
    def relevant_resource(self, relevant_resource):
        """Sets the relevant_resource of this EducationalResourceRead.


        :param relevant_resource: The relevant_resource of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._relevant_resource = relevant_resource

    @property
    def relevant_to(self):
        """Gets the relevant_to of this EducationalResourceRead.  # noqa: E501


        :return: The relevant_to of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._relevant_to

    @relevant_to.setter
    def relevant_to(self, relevant_to):
        """Sets the relevant_to of this EducationalResourceRead.


        :param relevant_to: The relevant_to of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._relevant_to = relevant_to

    @property
    def research_area(self):
        """Gets the research_area of this EducationalResourceRead.  # noqa: E501

        The research area is similar to the scientific_domain, but more high-level.  # noqa: E501

        :return: The research_area of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._research_area

    @research_area.setter
    def research_area(self, research_area):
        """Sets the research_area of this EducationalResourceRead.

        The research area is similar to the scientific_domain, but more high-level.  # noqa: E501

        :param research_area: The research_area of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._research_area = research_area

    @property
    def scientific_domain(self):
        """Gets the scientific_domain of this EducationalResourceRead.  # noqa: E501

        The scientific domain is related to the methods with which an objective is reached.  # noqa: E501

        :return: The scientific_domain of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._scientific_domain

    @scientific_domain.setter
    def scientific_domain(self, scientific_domain):
        """Sets the scientific_domain of this EducationalResourceRead.

        The scientific domain is related to the methods with which an objective is reached.  # noqa: E501

        :param scientific_domain: The scientific_domain of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._scientific_domain = scientific_domain

    @property
    def target_audience(self):
        """Gets the target_audience of this EducationalResourceRead.  # noqa: E501

        The intended users of this educational resource.  # noqa: E501

        :return: The target_audience of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """Sets the target_audience of this EducationalResourceRead.

        The intended users of this educational resource.  # noqa: E501

        :param target_audience: The target_audience of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._target_audience = target_audience

    @property
    def type(self):
        """Gets the type of this EducationalResourceRead.  # noqa: E501

        The type of educational resource.  # noqa: E501

        :return: The type of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EducationalResourceRead.

        The type of educational resource.  # noqa: E501

        :param type: The type of this EducationalResourceRead.  # noqa: E501
        :type: object
        """

        self._type = type

    @property
    def identifier(self):
        """Gets the identifier of this EducationalResourceRead.  # noqa: E501


        :return: The identifier of this EducationalResourceRead.  # noqa: E501
        :rtype: object
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this EducationalResourceRead.


        :param identifier: The identifier of this EducationalResourceRead.  # noqa: E501
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
        if issubclass(EducationalResourceRead, dict):
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
        if not isinstance(other, EducationalResourceRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
