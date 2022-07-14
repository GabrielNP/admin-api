import  bcrypt

def check_hash(raw_pwd: bytes, hashed_pwd: bytes):
    return bcrypt.checkpw(raw_pwd, hashed_pwd)
