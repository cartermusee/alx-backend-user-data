#!/usr/bin/env python3
"""method that takes in a
password string arguments and returns bytes.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> str:
    """method to paasw hash
    args:
        password(str): password to hash
    Returns: bytes"""
    salt = bcrypt.gensalt()
    pass_bytes = bcrypt.hashpw(password.encode('utf-8'), salt)
    return pass_bytes


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email, password):
        """hould take mandatory email
        and password string arguments
        and return a User object."""
        try:
            if self._db.find_user_by(email=email):
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            passw = _hash_password(password)
            return self._db.add_user(email, passw)
            