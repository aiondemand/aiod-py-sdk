# coding: utf-8

"""
    FastAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ProjectsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def count_of_projects_counts_projects_v1_get(self, **kwargs):  # noqa: E501
        """Count Of Projects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_of_projects_counts_projects_v1_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.count_of_projects_counts_projects_v1_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.count_of_projects_counts_projects_v1_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def count_of_projects_counts_projects_v1_get_with_http_info(self, **kwargs):  # noqa: E501
        """Count Of Projects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_of_projects_counts_projects_v1_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method count_of_projects_counts_projects_v1_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/counts/projects/v1', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_projects_platforms_platform_projects_v1_get(self, platform, **kwargs):  # noqa: E501
        """List Projects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_projects_platforms_platform_projects_v1_get(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object platform: (required)
        :param object schema:
        :param object offset:
        :param object limit:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_projects_platforms_platform_projects_v1_get_with_http_info(platform, **kwargs)  # noqa: E501
        else:
            (data) = self.list_projects_platforms_platform_projects_v1_get_with_http_info(platform, **kwargs)  # noqa: E501
            return data

    def list_projects_platforms_platform_projects_v1_get_with_http_info(self, platform, **kwargs):  # noqa: E501
        """List Projects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_projects_platforms_platform_projects_v1_get_with_http_info(platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object platform: (required)
        :param object schema:
        :param object offset:
        :param object limit:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['platform', 'schema', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_projects_platforms_platform_projects_v1_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'platform' is set
        if ('platform' not in params or
                params['platform'] is None):
            raise ValueError("Missing the required parameter `platform` when calling `list_projects_platforms_platform_projects_v1_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'platform' in params:
            path_params['platform'] = params['platform']  # noqa: E501

        query_params = []
        if 'schema' in params:
            query_params.append(('schema', params['schema']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/platforms/{platform}/projects/v1', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_projects_projects_v1_get(self, **kwargs):  # noqa: E501
        """List Projects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_projects_projects_v1_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object schema:
        :param object offset:
        :param object limit:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_projects_projects_v1_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_projects_projects_v1_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_projects_projects_v1_get_with_http_info(self, **kwargs):  # noqa: E501
        """List Projects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_projects_projects_v1_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object schema:
        :param object offset:
        :param object limit:
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['schema', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_projects_projects_v1_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'schema' in params:
            query_params.append(('schema', params['schema']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/v1', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def project_platforms_platform_projects_v1_identifier_get(self, identifier, platform, **kwargs):  # noqa: E501
        """Project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_platforms_platform_projects_v1_identifier_get(identifier, platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object identifier: (required)
        :param object platform: (required)
        :param object schema:
        :return: ProjectRead
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.project_platforms_platform_projects_v1_identifier_get_with_http_info(identifier, platform, **kwargs)  # noqa: E501
        else:
            (data) = self.project_platforms_platform_projects_v1_identifier_get_with_http_info(identifier, platform, **kwargs)  # noqa: E501
            return data

    def project_platforms_platform_projects_v1_identifier_get_with_http_info(self, identifier, platform, **kwargs):  # noqa: E501
        """Project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_platforms_platform_projects_v1_identifier_get_with_http_info(identifier, platform, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object identifier: (required)
        :param object platform: (required)
        :param object schema:
        :return: ProjectRead
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'platform', 'schema']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method project_platforms_platform_projects_v1_identifier_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `project_platforms_platform_projects_v1_identifier_get`")  # noqa: E501
        # verify the required parameter 'platform' is set
        if ('platform' not in params or
                params['platform'] is None):
            raise ValueError("Missing the required parameter `platform` when calling `project_platforms_platform_projects_v1_identifier_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'platform' in params:
            path_params['platform'] = params['platform']  # noqa: E501

        query_params = []
        if 'schema' in params:
            query_params.append(('schema', params['schema']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/platforms/{platform}/projects/v1/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectRead',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def project_projects_v1_identifier_delete(self, identifier, **kwargs):  # noqa: E501
        """Project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_projects_v1_identifier_delete(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object identifier: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.project_projects_v1_identifier_delete_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.project_projects_v1_identifier_delete_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def project_projects_v1_identifier_delete_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_projects_v1_identifier_delete_with_http_info(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object identifier: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method project_projects_v1_identifier_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `project_projects_v1_identifier_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OpenIdConnect']  # noqa: E501

        return self.api_client.call_api(
            '/projects/v1/{identifier}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def project_projects_v1_identifier_get(self, identifier, **kwargs):  # noqa: E501
        """Project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_projects_v1_identifier_get(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object identifier: (required)
        :param object schema:
        :return: ProjectRead
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.project_projects_v1_identifier_get_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.project_projects_v1_identifier_get_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def project_projects_v1_identifier_get_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_projects_v1_identifier_get_with_http_info(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object identifier: (required)
        :param object schema:
        :return: ProjectRead
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'schema']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method project_projects_v1_identifier_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `project_projects_v1_identifier_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'schema' in params:
            query_params.append(('schema', params['schema']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/v1/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectRead',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def project_projects_v1_identifier_put(self, body, identifier, **kwargs):  # noqa: E501
        """Project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_projects_v1_identifier_put(body, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectCreate body: (required)
        :param object identifier: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.project_projects_v1_identifier_put_with_http_info(body, identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.project_projects_v1_identifier_put_with_http_info(body, identifier, **kwargs)  # noqa: E501
            return data

    def project_projects_v1_identifier_put_with_http_info(self, body, identifier, **kwargs):  # noqa: E501
        """Project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_projects_v1_identifier_put_with_http_info(body, identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectCreate body: (required)
        :param object identifier: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method project_projects_v1_identifier_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `project_projects_v1_identifier_put`")  # noqa: E501
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `project_projects_v1_identifier_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OpenIdConnect']  # noqa: E501

        return self.api_client.call_api(
            '/projects/v1/{identifier}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def project_projects_v1_post(self, body, **kwargs):  # noqa: E501
        """Project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_projects_v1_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectCreate body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.project_projects_v1_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.project_projects_v1_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def project_projects_v1_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.project_projects_v1_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectCreate body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method project_projects_v1_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `project_projects_v1_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OpenIdConnect']  # noqa: E501

        return self.api_client.call_api(
            '/projects/v1', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
