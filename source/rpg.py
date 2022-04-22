#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string
import random

def random_password_generator():
	# Add character strings to chars variable with the strings showing uppercase, lowercase, numbers, and special characters.
	# string.ascii_letters is a chain of the ascii_lowercase and ascii_uppercase 
    chars = string.ascii_letters + string.digits + string.punctuation
    size = 4
    return ''.join(random.choice(chars) for x in range(size, 20))

def random_password_generator_ico():
	random_password_generator_ico = """
	#############################################################
	# PYTHON - Random Password Generetor (RPG) - GH0ST S0FTWARE #
	#############################################################
	#                         CONTACT                           #
	#############################################################
	#               DEVELOPER : İSMAİL TAŞDELEN                 #
	#          Mail Address : pentestdatabase@gmail.com         #
	#   LINKEDIN : https://www.linkedin.com/in/ismailtasdelen   #
	#              Whatsapp : + 90 534 295 94 31                #
	#############################################################
	"""
	print(random_password_generator_ico)
