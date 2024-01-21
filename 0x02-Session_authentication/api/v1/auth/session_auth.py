#!/usr/bin/env python3
"""
Session Authentication class for the API
"""

from api.v1.auth.auth import Auth
from typing import TypeVar
import uuid


class SessionAuth(Auth):
    """ Session Management class for the API. """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if not user_id or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
