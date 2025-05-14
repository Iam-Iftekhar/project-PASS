import os
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_password(password):
    with open("master.key", "w") as file:
        file.write(hash_password(password))

def verify():
    if not os.path.exists("master.key"):
        password = input("Set your master password: ")
        save_password(password)
        return True
    else:
        password = input("Enter your master password: ")
        with open("master.key", "r") as file:
            stored_hash = file.read()
        return stored_hash == hash_password(password)