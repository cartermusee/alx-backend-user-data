#!/usr/bin/env python3
"""method that takes in a
password string arguments and returns bytes.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """method to paasw hash
    args:
        password(str): password to hash
    Returns: bytes"""
    salt = bcrypt.gensalt()
    pass_bytes = bcrypt.hashpw(password.encode('utf-8'), salt)
    return pass_bytes


def _generate_uuid() -> str:
    """generate uuid"""
    new_uid = uuid.uuid4()
    return str(new_uid)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """hould take mandatory email
        and password string arguments
        and return a User object."""
        try:
            if self._db.find_user_by(email=email):
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            passw = _hash_password(password)
            return self._db.add_user(email, passw)

    def valid_login(self, email: str, password: str) -> bool:
        """check pass if iss hashhed while logining"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                if bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password):
                    return True
        except Exception:
            return False
        return False

    def create_session(self, email: str) -> str:
        """creating a session
        Returns: a string"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            user.session_id = _generate_uuid()
            return user.session_id

    def get_user_from_session_id(self, session_id: str):
        """find user by session id"""
        if session_id is None:
            return None
        user = self._db._session.query(User)\
            .filter_by(session_id=session_id).first()
        if user:
            return user
        else:
            return None

    def destroy_session(self, user_id: str) -> None:
        """a method thatdestroy session
        args:
            user_id: users id to get user"""
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None
        else:
            user.session_id = None
            return None

    def get_reset_password_token(self, email: str) -> str:
        """generate reset password"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                user.reset_token = _generate_uuid()
                return user.reset_token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """update password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            user.hashed_password = hashed_password
            user.reset_token = None
        except Exception:
            raise ValueError
