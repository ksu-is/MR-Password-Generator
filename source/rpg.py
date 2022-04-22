#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string
import random

def random_password_generator():
	# Add character strings to chars variable with the strings showing uppercase, lowercase, numbers, and special characters.
	# string.ascii_letters is a chain of the ascii_lowercase and ascii_uppercase 
    chars = string.ascii_letters + string.digits + string.punctuation
    length = 4
    return ''.join(random.choice(chars) for x in range(length, 20))

def random_password_generator_ico():
	random_password_generator_ico = """

	"""
	print(random_password_generator_ico)
