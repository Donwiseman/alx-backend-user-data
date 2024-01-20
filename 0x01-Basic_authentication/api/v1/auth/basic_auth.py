#!/usr/bin/env python3
"""
Basic Authentication class for the API
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """Implements the basic authentication system for api."""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts the Base64 enconding string for basic authy."""
        if not authorization_header or type(authorization_header) is not str:
            return None
        if authorization_header.startswith("Basic "):
            return authorization_header.split()[1]
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Decodes a base64 encoded dtring. """
        if not base64_authorization_header or type(base64_authorization_header
                                                   ) is not str:
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Returns the extracted username and password from decoded string."""
        if not decoded_base64_authorization_header or\
                type(decoded_base64_authorization_header) is not str or\
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        return decoded_base64_authorization_header.split(':')

    def user_object_from_credentials(self, user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """Returns the user object matching the credentials."""
        from models.user import User
        if not user_email or not user_pwd:
            return None
        if type(user_email) is not str or type(user_pwd) is not str:
            return None
        search_results = User.search({'email': user_email})
        if not search_results:
            return None
        for obj in search_results:
            if obj.is_valid_password(user_pwd):
                return obj
        return None
