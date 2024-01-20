#!/usr/bin/env python3
"""
Basic Authentication class for the API
"""

from api.v1.auth.auth import Auth
import base64


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
