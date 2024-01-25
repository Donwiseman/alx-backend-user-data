#!/usr/bin/env python3
""" The authentication class for the model."""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(passwd: str) -> bytes:
    """Hashes a given password."""
    salt = gensalt()
    encoded_pw = passwd.encode('utf-8')
    return hashpw(encoded_pw, salt)


def _generate_uuid() -> str:
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user and returns it. """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except InvalidRequestError or NoResultFound:
            hashed_passwd = _hash_password(password)
            return self._db.add_user(email, hashed_passwd)

    def valid_login(self,  email: str, password: str) -> bool:
        """Validates a password login."""
        try:
            user = self._db.find_user_by(email=email)
            pw_bytes = password.encode('utf-8')
            return checkpw(pw_bytes, user.hashed_password)
        except InvalidRequestError or NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Creates a session for the user."""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except InvalidRequestError or NoResultFound or ValueError:
            return None
