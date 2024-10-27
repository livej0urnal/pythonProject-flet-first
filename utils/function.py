import hashlib
import string
import random


#method create password hash
def hash_password(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

# generate random name for file
def p_link_generate(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters_and_digits) for i in range(length))
    return result_str