import json
from models import User

def login(role):
    """
    Logs in all users (employees and managers).
    """
    username = input("Username: ")
    password = input("Password: ")

    with open("database.json", "r") as f:
        db = json.load(f)

    users = db["users"][f"{role}s"]

    if username in users and users[username] == password:
        print("\nLogin successful!\n")
        return User(username, role)
    
    return None
