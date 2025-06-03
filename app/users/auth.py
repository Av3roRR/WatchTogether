from argon2 import PasswordHasher

pwd_context = PasswordHasher()

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(hashed_password: str, plain_password: str) -> bool:
    return pwd_context.verify(hashed_password, plain_password)