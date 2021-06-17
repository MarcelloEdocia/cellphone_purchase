import json

class Config:

    def __init__(self):
        self.app_title = "CellPhone Purchases Management System"
        self.screen = "730x500+500+200"
        self.users_path = "./data/users.json"
        self.purchase_path = "./data/purchases.json"

    def load_user(self):
        with open(self.users_path, "r") as json_data:
            data = json.load(json_data)
        return data

    def load_purchase(self):
        with open(self.purchase_path,"r") as json_data:
            data = json.load(json_data)
        return data

    def login(self, username, password):
        users = self.load_user()
        if username in users:
            if password == users[username]["password"]:
                return True
        else:
            return False


