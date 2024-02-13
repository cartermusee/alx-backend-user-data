#!/usr/bin/env python3
"""module for auth class"""
from flask import request
from typing import List, TypeVar


class Auth():
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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method for request auth method
        Keyword arguments:
        request: request for current_user
        Return: false path
        """
        return None
