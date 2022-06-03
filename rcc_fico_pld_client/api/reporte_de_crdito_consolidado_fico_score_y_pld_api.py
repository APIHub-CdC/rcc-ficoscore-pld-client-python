# coding: utf-8



from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rcc_fico_pld_client.api_client import ApiClient


class ReporteDeCrditoConsolidadoFICOScoreYPLDApi(object):


    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_consultas(self, folio_consulta,  x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene las consultas del reporte de crédito.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consultas(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: Consultas
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_consultas_with_http_info(folio_consulta,  x_api_key, username, password, **kwargs)  # noqa: E501
        else:
            (data) = self.get_consultas_with_http_info(folio_consulta,  x_api_key, username, password, **kwargs)  # noqa: E501
            return data

    def get_consultas_with_http_info(self, folio_consulta,  x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene las consultas del reporte de crédito.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_consultas_with_http_info(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: Consultas
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folio_consulta', 'x_api_key', 'username', 'password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_consultas" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folio_consulta' is set
        if self.api_client.client_side_validation and ('folio_consulta' not in params or
                                                       params['folio_consulta'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folio_consulta` when calling `get_consultas`")  # noqa: E501
        # verify the required parameter '' is set
        if self.api_client.client_side_validation and ('' not in params or
                                                       params[''] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `` when calling `get_consultas`")  # noqa: E501
        # verify the required parameter 'x_api_key' is set
        if self.api_client.client_side_validation and ('x_api_key' not in params or
                                                       params['x_api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `x_api_key` when calling `get_consultas`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_consultas`")  # noqa: E501
        # verify the required parameter 'password' is set
        if self.api_client.client_side_validation and ('password' not in params or
                                                       params['password'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `password` when calling `get_consultas`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folio_consulta' in params:
            path_params['folioConsulta'] = params['folio_consulta']  # noqa: E501

        query_params = []

        header_params = {}
        if '' in params:
            header_params['x-signature'] = params['']  # noqa: E501
        if 'x_api_key' in params:
            header_params['x-api-key'] = params['x_api_key']  # noqa: E501
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/rcc-ficoscore-pld/{folioConsulta}/consultas', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Consultas',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_creditos(self, folio_consulta,  x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene los créditos del reporte de crédito.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_creditos(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: Creditos
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_creditos_with_http_info(folio_consulta,  x_api_key, username, password, **kwargs)  # noqa: E501
        else:
            (data) = self.get_creditos_with_http_info(folio_consulta,  x_api_key, username, password, **kwargs)  # noqa: E501
            return data

    def get_creditos_with_http_info(self, folio_consulta,  x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene los créditos del reporte de crédito.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_creditos_with_http_info(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: Creditos
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folio_consulta',  'x_api_key', 'username', 'password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_creditos" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folio_consulta' is set
        if self.api_client.client_side_validation and ('folio_consulta' not in params or
                                                       params['folio_consulta'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folio_consulta` when calling `get_creditos`")  # noqa: E501
      
        # verify the required parameter 'x_api_key' is set
        if self.api_client.client_side_validation and ('x_api_key' not in params or
                                                       params['x_api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `x_api_key` when calling `get_creditos`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_creditos`")  # noqa: E501
        # verify the required parameter 'password' is set
        if self.api_client.client_side_validation and ('password' not in params or
                                                       params['password'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `password` when calling `get_creditos`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folio_consulta' in params:
            path_params['folioConsulta'] = params['folio_consulta']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_api_key' in params:
            header_params['x-api-key'] = params['x_api_key']  # noqa: E501
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/rcc-ficoscore-pld/{folioConsulta}/creditos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Creditos',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_domicilios(self, folio_consulta, x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene los domiclios del reporte de crédito.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_domicilios(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: DomiciliosRespuesta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_domicilios_with_http_info(folio_consulta,  x_api_key, username, password, **kwargs)  # noqa: E501
        else:
            (data) = self.get_domicilios_with_http_info(folio_consulta,  x_api_key, username, password, **kwargs)  # noqa: E501
            return data

    def get_domicilios_with_http_info(self, folio_consulta,  x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene los domiclios del reporte de crédito.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_domicilios_with_http_info(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: DomiciliosRespuesta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folio_consulta',  'x_api_key', 'username', 'password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_domicilios" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folio_consulta' is set
        if self.api_client.client_side_validation and ('folio_consulta' not in params or
                                                       params['folio_consulta'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folio_consulta` when calling `get_domicilios`")  # noqa: E501

        # verify the required parameter 'x_api_key' is set
        if self.api_client.client_side_validation and ('x_api_key' not in params or
                                                       params['x_api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `x_api_key` when calling `get_domicilios`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_domicilios`")  # noqa: E501
        # verify the required parameter 'password' is set
        if self.api_client.client_side_validation and ('password' not in params or
                                                       params['password'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `password` when calling `get_domicilios`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folio_consulta' in params:
            path_params['folioConsulta'] = params['folio_consulta']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_api_key' in params:
            header_params['x-api-key'] = params['x_api_key']  # noqa: E501
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/rcc-ficoscore-pld/{folioConsulta}/domicilios', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DomiciliosRespuesta',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_empleos(self, folio_consulta, x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene los empleos del reporte de crédito.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_empleos(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: Empleos
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_empleos_with_http_info(folio_consulta,  x_api_key, username, password, **kwargs)  # noqa: E501
        else:
            (data) = self.get_empleos_with_http_info(folio_consulta,  x_api_key, username, password, **kwargs)  # noqa: E501
            return data

    def get_empleos_with_http_info(self, folio_consulta,  x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene los empleos del reporte de crédito.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_empleos_with_http_info(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: Empleos
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folio_consulta',  'x_api_key', 'username', 'password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_empleos" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folio_consulta' is set
        if self.api_client.client_side_validation and ('folio_consulta' not in params or
                                                       params['folio_consulta'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folio_consulta` when calling `get_empleos`")  # noqa: E501
        # verify the required parameter 'x_api_key' is set
        if self.api_client.client_side_validation and ('x_api_key' not in params or
                                                       params['x_api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `x_api_key` when calling `get_empleos`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_empleos`")  # noqa: E501
        # verify the required parameter 'password' is set
        if self.api_client.client_side_validation and ('password' not in params or
                                                       params['password'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `password` when calling `get_empleos`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folio_consulta' in params:
            path_params['folioConsulta'] = params['folio_consulta']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_api_key' in params:
            header_params['x-api-key'] = params['x_api_key']  # noqa: E501
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/rcc-ficoscore-pld/{folioConsulta}/empleos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Empleos',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_mensajes(self, folio_consulta,  x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene los mensajes del reporte de crédito.  # noqa: E501

        El elemento de Mensaje contiene información acerca de los mensajes emitidos por Círculo de Crédito, este elemento se repite dependiendo del número de mensajes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mensajes(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: Mensajes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_mensajes_with_http_info(folio_consulta,  x_api_key, username, password, **kwargs)  # noqa: E501
        else:
            (data) = self.get_mensajes_with_http_info(folio_consulta,  x_api_key, username, password, **kwargs)  # noqa: E501
            return data

    def get_mensajes_with_http_info(self, folio_consulta,  x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene los mensajes del reporte de crédito.  # noqa: E501

        El elemento de Mensaje contiene información acerca de los mensajes emitidos por Círculo de Crédito, este elemento se repite dependiendo del número de mensajes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_mensajes_with_http_info(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: Mensajes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folio_consulta', 'x_api_key', 'username', 'password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mensajes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folio_consulta' is set
        if self.api_client.client_side_validation and ('folio_consulta' not in params or
                                                       params['folio_consulta'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folio_consulta` when calling `get_mensajes`")  # noqa: E501
    
        # verify the required parameter 'x_api_key' is set
        if self.api_client.client_side_validation and ('x_api_key' not in params or
                                                       params['x_api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `x_api_key` when calling `get_mensajes`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_mensajes`")  # noqa: E501
        # verify the required parameter 'password' is set
        if self.api_client.client_side_validation and ('password' not in params or
                                                       params['password'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `password` when calling `get_mensajes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folio_consulta' in params:
            path_params['folioConsulta'] = params['folio_consulta']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_api_key' in params:
            header_params['x-api-key'] = params['x_api_key']  # noqa: E501
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/rcc-ficoscore-pld/{folioConsulta}/mensajes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Mensajes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_reporte(self, x_api_key, username, password, request, **kwargs):  # noqa: E501
        """Obtiene el reporte de crédito.  # noqa: E501

        En caso de que el reporte se consuma de forma segmentada, éste retornará un header llamado **x-cache-remaining**, el cual indicará el tiempo restante en cache; formato en segundos.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reporte(, x_api_key, username, password, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :param PersonaPeticion request:  (required)
        :param str x_full_report: Indicador si se quiere obtener el reporte en una sola petición true; en caso de requerirse de manera segmentada será false
        :return: Respuesta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_reporte_with_http_info( x_api_key, username, password, request, **kwargs)  # noqa: E501
        else:
            (data) = self.get_reporte_with_http_info(x_api_key, username, password, request, **kwargs)  # noqa: E501
            return data

    def get_reporte_with_http_info(self,  x_api_key, username, password, request, **kwargs):  # noqa: E501
        """Obtiene el reporte de crédito.  # noqa: E501

        En caso de que el reporte se consuma de forma segmentada, éste retornará un header llamado **x-cache-remaining**, el cual indicará el tiempo restante en cache; formato en segundos.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reporte_with_http_info(, x_api_key, username, password, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :param PersonaPeticion request:  (required)
        :param str x_full_report: Indicador si se quiere obtener el reporte en una sola petición true; en caso de requerirse de manera segmentada será false
        :return: Respuesta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [ 'x_api_key', 'username', 'password', 'request', 'x_full_report']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_reporte" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_api_key' is set
        if self.api_client.client_side_validation and ('x_api_key' not in params or
                                                       params['x_api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `x_api_key` when calling `get_reporte`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_reporte`")  # noqa: E501
        # verify the required parameter 'password' is set
        if self.api_client.client_side_validation and ('password' not in params or
                                                       params['password'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `password` when calling `get_reporte`")  # noqa: E501
        # verify the required parameter 'request' is set
        if self.api_client.client_side_validation and ('request' not in params or
                                                       params['request'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `request` when calling `get_reporte`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_api_key' in params:
            header_params['x-api-key'] = params['x_api_key']  # noqa: E501
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501
        if 'x_full_report' in params:
            header_params['x-full-report'] = params['x_full_report']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/rcc-ficoscore-pld', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Respuesta',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scores(self, folio_consulta, x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene los scores del reporte de crédito.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scores(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: Scores
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scores_with_http_info(folio_consulta, x_api_key, username, password, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scores_with_http_info(folio_consulta,  x_api_key, username, password, **kwargs)  # noqa: E501
            return data

    def get_scores_with_http_info(self, folio_consulta,  x_api_key, username, password, **kwargs):  # noqa: E501
        """Obtiene los scores del reporte de crédito.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scores_with_http_info(folio_consulta, , x_api_key, username, password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folio_consulta:  (required)
        :param str : Firma generada con la llave privada (required)
        :param str x_api_key: ConsumerKey obtenido desde el portal de desarrolladores (required)
        :param str username: Usuario de Círculo de Crédito (required)
        :param str password: Contraseña de Círculo de Crédito (required)
        :return: Scores
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folio_consulta',  'x_api_key', 'username', 'password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scores" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folio_consulta' is set
        if self.api_client.client_side_validation and ('folio_consulta' not in params or
                                                       params['folio_consulta'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `folio_consulta` when calling `get_scores`")  # noqa: E501
     
        # verify the required parameter 'x_api_key' is set
        if self.api_client.client_side_validation and ('x_api_key' not in params or
                                                       params['x_api_key'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `x_api_key` when calling `get_scores`")  # noqa: E501
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and ('username' not in params or
                                                       params['username'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `username` when calling `get_scores`")  # noqa: E501
        # verify the required parameter 'password' is set
        if self.api_client.client_side_validation and ('password' not in params or
                                                       params['password'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `password` when calling `get_scores`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folio_consulta' in params:
            path_params['folioConsulta'] = params['folio_consulta']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_api_key' in params:
            header_params['x-api-key'] = params['x_api_key']  # noqa: E501
        if 'username' in params:
            header_params['username'] = params['username']  # noqa: E501
        if 'password' in params:
            header_params['password'] = params['password']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/rcc-ficoscore-pld/{folioConsulta}/scores', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Scores',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
