#!/usr/bin/env python3
"""module for bcrypt"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash password with haspwd"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """check if is valid"""
    valid = bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    return valid
