#!/usr/bin/env python3
"""
Session Authentication class for the API
"""

from api.v1.auth.auth import Auth
from typing import TypeVar


class SessionAuth(Auth):
    """ Session Management class for the API. """
