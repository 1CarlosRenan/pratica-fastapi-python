from datetime import datetime, timedelta
from jose import jwt

# CONFIG
SECRET_KEY = 'caa9c8f8620cbb30679026bb6427e11f'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000


def criar_acess_token(data: dict):
    return 'token23423423'


def verificar_acess_token(token: str):
    return '(86) 99945-9999'
