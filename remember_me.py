from pathlib import Path
import json

def get_stored_user_inform(path):
    if path.exists():
        contents=path.read_text()
        user_inform=json.loads(contents)
        return user_inform 
    else:
        return None

def greet_user():
    path=Path("user_name.json")
    user_inform=get_stored_user_inform(path)
    if user_inform:
        print(f"Welcome back!We remember you.")
        for key,value in user_inform.items():
            print(f"Your {key} is {value}.")
    else:
        user_name=input("What's your name?")
        user_phone=input("What's your telephone number?")
        user_birthday=input("What's your birthday?")
        user_inform={}
        user_inform["name"]=user_name
        user_inform["phone"]=user_phone
        user_inform["birthday"]=user_birthday
        contents=json.dumps(user_inform)
        path.write_text(contents)
        print("We will remember your information")

greet_user()    
    