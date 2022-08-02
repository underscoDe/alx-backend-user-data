#!/usr/bin/env python3
""" Authentication helper
"""

import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User
import bcrypt
from uuid import uuid4


def _hash_password(password: str) -> str:
    """takes in a password string
    argument and returns a bytes"""

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
