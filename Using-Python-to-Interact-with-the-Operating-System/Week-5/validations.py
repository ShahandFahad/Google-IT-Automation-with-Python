##!/usr/bin/env python3

def validate_user(username, minlength):
    # Check conditionals
    assert type(username) == str, "username must be a string"
    # Raise type of error
    if minlength < 1:
        raise ValueError("minlength must be at least 1")
    if len(username) < 1:
        return False
    if not username.isalnum():
        return False
    return True
