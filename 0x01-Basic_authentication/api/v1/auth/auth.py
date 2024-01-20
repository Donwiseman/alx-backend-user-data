#!/usr/bin/env python3
"""
Authentication class for the API
"""

from flask import request
from typing import TypeVar, List


class Auth():
    """
    Base class definition for the API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check i the path requires authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """Check if the authorization object is present."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user who sent the request."""
        return None
