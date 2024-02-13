#!/usr/bin/env python3
"""module for basic auth class"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """that returns the decoded value of a Base64
        string base64_authorization_header:
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            dec = base64.b64decode(base64_authorization_header)
            dc_utf = dec.decode('utf-8')
            return dc_utf
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """method returns the
        user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        else:
            email, password = decoded_base64_authorization_header.split(":")
            return email, password
