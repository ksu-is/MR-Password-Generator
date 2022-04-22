#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string
import random
#from tkinter import IntVar, StringVar

def random_password_generator():
	# Add character strings to chars variable with the strings showing uppercase, lowercase, numbers, and special characters.
	# string.ascii_letters is a chain of the ascii_lowercase and ascii_uppercase 
    chars = string.ascii_letters + string.digits + string.punctuation
    length = 4
    return ''.join(random.choice(chars) for x in range(length, 20))

# pass_len = IntVar()
# pass_str = StringVar()
# def Generator():
#    password = ''
#    for x in range (0,4):
#        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
#    for y in range(pass_len.get()- 4):
#        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
#    pass_str.set(password)

def random_password_generator_ico():
	random_password_generator_ico = """

	"""
	print(random_password_generator_ico)
