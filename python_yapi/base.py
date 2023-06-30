import logging
from json import JSONDecodeError
from typing import Union

import requests

from .exceptions import ResponseNotJSONError
from .utils import log

DEFAULT_TIMEOUT = 60


class ApiBase(object):
    """Base class for YApi Http API"""

    def __init__(self, base_url: str = 'http://localhost:3000'):
        """
        :param base_url: The base URL of YApi(dafault as http://localhost:3000)
        """
        self.base_url = base_url.rstrip('/')
        self._session = requests.Session()
        self._session.timeout = DEFAULT_TIMEOUT

    def request(self, method, url, **kwargs) -> Union[dict, list, str]:
        """
        Send general http request
        :param method: The HTTP method, eg: GET, POST, PUT, DELETE, ...
        :param url: The URL of the request, can be relative api path to the base_url
        :param kwargs: keyword arguments that requests.request() supports
                eg: params, headers, data, json, files, auth, ...
                additional keyword argument: check_errcode (default as True)
        :return: JSON format response body as dictionary
        :raise: TimeoutError if request timeout to get response
        :raise: JSONDecodeError if response body is not a JSON
        :raise: AssertionError if check_errcode(deafault as True) and errcode of response body not equals 0
        """
        if not url.startswith('http'):
            url = f'{self.base_url}/{url.lstrip("/")}'
        response = self._session.request(method, url, **kwargs)
        if not response.ok:
            logging.warning(f'Response Error: [{response.status_code}] {response.text}')
        try:
            response_body = response.json()
        except JSONDecodeError:
            raise ResponseNotJSONError(f"Response body is not a JSON: {response.text}")

        check_errcode = kwargs.pop('check_errcode', True)
        if check_errcode:
            assert response_body['errcode'] == 0, f'response error: {response_body}'
        return response_body['data']

    @log
    def get(self, url, **kwargs) -> Union[dict, list, str]:
        """
        Send http get request
        :param url: The URL of the request, can be relative api path to the base_url
        :param kwargs: keyword arguments that requests.request() supports
                eg: params, headers, data, json, files, auth, ...
                additional keyword argument: check_errcode (default as True)
        :raise: TimeoutError if request timeout to get response
        :raise: JSONDecodeError if response body is not a JSON
        :raise: AssertionError if check_errcode(deafault as True) and errcode of response body not equals 0
        :return: JSON format response body as dictionary
        """
        return self.request('GET', url, **kwargs)

    @log
    def post(self, url, **kwargs) -> Union[dict, list, str]:
        """
        Send http POST request
        :param url: The URL of the request, can be relative api path to the base_url
        :param kwargs: keyword arguments that requests.request() supports
                eg: params, headers, data, json, files, auth, ...
                additional keyword argument: check_errcode (default as True)
        :raise: TimeoutError if request timeout to get response
        :raise: JSONDecodeError if response body is not a JSON
        :raise: AssertionError if check_errcode(deafault as True) and errcode of response body not equals 0
        :return: JSON format response body as dictionary
        """
        return self.request('POST', url, **kwargs)
