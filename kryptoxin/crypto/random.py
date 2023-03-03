"""
kryptoxin crypto random module.
This module is dedicated to random cryptographic functions.
"""
import secrets


def gen_rand_bytes(len):
    return secrets.token_bytes(len)
