#!/usr/bin/env python3

# a function that verifies wether a chosen username is valid
def validate_user(username, minLen):
    assert type(username) == str, "username must be a string"

    if minLen<1:
        raise ValueError("minLen must be at least 1")
    
    if not username.isalnum():
        return False
    return True