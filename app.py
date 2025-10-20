import json, os, hashlib, pwinput, logging


logging.basicConfig(
    filename='login.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    force=True
)

def Hashpassword(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed


