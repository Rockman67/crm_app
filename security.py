import bcrypt

def hash_password(password):
    """
    Хеширование пароля.
    
    Args:
        password (str): Пароль пользователя.
        
    Returns:
        str: Хешированный пароль.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    """
    Проверка пароля.
    
    Args:
        password (str): Пароль пользователя.
        hashed (str): Хешированный пароль.
        
    Returns:
        bool: True, если пароль правильный, иначе False.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
