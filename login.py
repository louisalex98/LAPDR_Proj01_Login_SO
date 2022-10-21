class Login():
    def __init__(self):

        
        user = str(input("Welcome! Please type your username:\n_"))
        self.user = user
        password = str(input("And now type your password:\n_"))
        self.password = password
        self.run()
        

    def run(self):
        counter = 0
        while self.check() is False:
            print("\nINCORRECT USERNAME OR PASSWORD!\nPLEASE RETRY")
            counter += 1
            if counter > 5:
                print("OUT OF TRIALS! CLOSING FOR YOUR SAFETY") 
            self.user = str(input("\nPlease type your username:\n_"))
            self.password = str(input("And now type your password:\n_")) 
        print("\n------------------------------\nWelcome back!\n------------------------------\n")
        self.file_users.close()
        self.file_password.close()

    def check(self):
        self.file_users = open("users.txt", "r")
        self.file_password = open("passwords.txt", "r")
        keyUser = self.file_users.readlines()
        keyPassword = self.file_password.readlines()
        if self.user in keyUser and \
           self.password in keyPassword:
            return True
        else:
            return False
        
    def counter(self):
        counter = 0



login = Login()
