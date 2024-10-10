                                ## In this section we will practise the __call__ magic function ##
from typing import Any


class FormValidator:
    def __init__(self) -> None:
        self.error=[]
    
    def __call__(self, data:Any) -> Any:
        self.error.clear()                              ##It will clear all the elemets presented in the list
        if not data.get("username"):
            self.error.append("Username is not presented")
        if not data.get("password"):
            self.error.append("Password is not presented over there")
        if "@" not in data.get("email",""):
            self.error.append("Invalid email error format")
        return len(self.error) == 0
    
##Object or instance created here
validator = FormValidator()

form_data = {
    "username": "john_doe",
    "password": "hackerzone",
    "email": "john@example.com"
}
if validator(form_data):
    print("Your form is valid")
else:
    print("Your form is not valid")
        