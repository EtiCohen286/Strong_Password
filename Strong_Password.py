import re

def strong_password(password):
    if len(password) < 8:
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[0-9]', password):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    if len(set(password)) != len(password):
        for char in set(password):
            if password.count(char) > 2:
                return False
    
    sequences = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789']
    for seq in sequences:
        for i in range(len(seq) - 2):
            if seq[i:i+3] in password:
                return False 
                   
    return True

