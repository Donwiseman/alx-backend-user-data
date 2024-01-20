#!/usr/bin/env python3
"""
Basic Authentication class for the API
"""

from api.v1.auth.auth import Auth


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
