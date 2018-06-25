import hashlib
import os

def gen_validkey():
    random = os.urandom(16)
    md5 = hashlib.md5()
    md5.update(random)
    return md5.hexdigest()

