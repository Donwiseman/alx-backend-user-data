#!/usr/bin/env python3
""" The authentication class for the model."""
from bcrypt import hashpw, gensalt


def _hash_password(passwd: str) -> bytes:
    """Hashes a given password."""
    salt = gensalt()
    encoded_pw = passwd.encode('utf-8')
    return hashpw(encoded_pw, salt)
