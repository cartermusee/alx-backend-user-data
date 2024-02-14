#!/usr/bin/env python3
"""module for auth class"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """module for class auth"""
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """ public method for require auth method
        Keyword arguments:
        path: path
         excluded_paths: not included
        Return: false path
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for url in excluded_paths:
            if url.endswith('/'):
                if path.startswith(url):
                    return False
                else:
                    if path == url.rstrip('/'):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """ public method for request auth method
        Keyword arguments:
        request: request to send or post
        Return: none
        """
        if request is None:
            return None
        aut = request.headers.get('Authorization')
        if aut is None:
            return None
        else:
            return aut

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method for request auth method
        Keyword arguments:
        request: request for current_user
        Return: false path
        """
        return None

    def session_cookie(self, request=None):
        """method that returns a cookie value from a request"""
        if request is None:
            return None
        cookies = getenv('SESSION_NAME', '_my_session_id')
        rqc = request.cookies.get(cookies)
        return rqc
