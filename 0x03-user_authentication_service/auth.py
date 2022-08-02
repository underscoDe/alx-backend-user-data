#!/usr/bin/env python3
""" Authentication helper
"""

import bcrypt


def _hash_password(password: str) -> str:
    """takes in a password string
    argument and returns a bytes"""

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
