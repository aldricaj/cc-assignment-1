import bcrypt
import repo

def check_user(username, clear_password):
    user = repo.get_user_by_username(username)
    if bcrypt.checkpw(clear_password.encode('utf8'), user.password_hash):
        return user
    else:
        return False

def hash_password(clear_password):
    return bcrypt.hashpw(clear_password.encode('utf8'), bcrypt.gensalt())

