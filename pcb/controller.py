from login import Login
from view import View


class Controller():
    
    def __init__(self):
        
        self.login = Login(self)
        self.view = View(self)