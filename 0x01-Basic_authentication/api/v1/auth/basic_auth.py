#!/usr/bin/env python3
"""module for basic auth class"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """methods for basic auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """returns the Base64 part of the Authorization
        header for a Basic Authentication:
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        bas_auth = authorization_header.startswith('Basic')
        bas_auth_end = authorization_header.endswith(" ")

        if not bas_auth and not bas_auth_end:
            return None
        else:
            return authorization_header.split(' ')[1]
