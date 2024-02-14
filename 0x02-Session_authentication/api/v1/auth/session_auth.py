#!/usr/bin/env python3
"""module for session auth class"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
import uuid
from models.user import User


class SessionAuth(Auth):
    """clas session auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """method that hat creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id.update({session_id: user_id})
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """method that returns a User ID based on a Session ID:"""
        if session_id is None or not isinstance(session_id, str):
            return None
        self.user_id_by_session_id.get(session_id)
