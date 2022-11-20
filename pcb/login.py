from pymongo import MongoClient

class Login():
    
    def __init__(self):
        
        
        self.connect()
        user = str(input("Welcome! Please type your username:\n_"))
        self.user = user
        password = str(input("And now type your password:\n_"))
        self.password = password
        self.run()

    def connect(self):
        client = MongoClient("mongodb://localhost:27017/")
        mydb = client["operationalsystemsdb"]
        self.mydb = mydb
        dblist = client.list_database_names()
        if "operationalsystemsdb" in dblist:
            print("The database exists.")
        else:
            print("Not found")
        

    def run(self):
        counter = 0
        while self.check() is False:
            print("\nINCORRECT USERNAME OR PASSWORD!\nPLEASE RETRY", "--TRIALS:", counter)
            counter += 1
            if counter > 5:
                print("OUT OF TRIALS! CLOSING FOR YOUR SAFETY")
                break 
            self.user = str(input("\nPlease type your username:\n_"))
            self.password = str(input("And now type your password:\n_")) 
        print("\n------------------------------\nWelcome back!\n------------------------------\n")

    def check(self):
        my_col = self.mydb["logins"]
        
        user = {"username" : self.user}
        password = {"password" : self.password}
        key_user = bool(my_col.find_one(user))
        key_password = bool(my_col.find_one(password))

        if  key_user is True and \
            key_password is True:
            return True
        else:
            return False

l = Login()