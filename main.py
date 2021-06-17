import tkinter
import sys
import time
import json

from config import Config
from login_page import LoginPage
from menu import MenuPage
from register import Register
from admin import Admin
from purchases import Purchase
from add_purchase import AddPurchase

class Window(tkinter.Tk):

    def __init__(self, App):
        self.app = App
        self.config = App.config

        super().__init__()
        self.title(self.config.app_title)
        self.geometry(self.config.screen)
        self.resizable(False, False)
        self.create_container()


        self.pages = {}
        self.users = self.config.load_user()
        self.purchases = self.config.load_purchase()

        self.create_add_purchase()
        self.create_admin_page()
        self.create_purchase_page()
        self.create_register_page()
        self.create_menu_page()
        self.create_login_page()

    def create_container(self):
        self.container = tkinter.Frame(self, bg="grey")
        self.container.pack(fill="both", expand=True)

    def create_login_page(self):
        self.pages["LoginPage"] = LoginPage(self.container, self)

    def create_menu_page(self):
        self.pages["MenuPage"] = MenuPage(self.container, self)

    def create_register_page(self):
        self.pages["RegisterPage"] = Register(self.container, self)

    def create_admin_page(self):
        self.pages["AdminPage"] = Admin(self.container, self)

    def create_purchase_page(self):
        self.pages["PurchasePage"] = Purchase(self.container, self)

    def create_add_purchase(self):
        self.pages["AddPurchase"] = AddPurchase(self.container, self)


    def create_falselogin(self):
        self.pixelVirtual = tkinter.PhotoImage(width=2, height=1)
        self.button_width = 80
        self.button_height = 30
        pop = tkinter.Toplevel(self)
        pop.title("Warning")
        pop.geometry("250x150+700+300")
        pop.config(bg="cyan")
        # Text warning
        pop_warning = tkinter.Label(pop, text="Wrong username or password !", font=("roboto sans-serif", 12), bg="cyan")
        pop_warning.pack(pady=10)
        # Warning button
        pop_frame = tkinter.Frame(pop, bg="cyan")
        pop_frame.pack(pady=5)
        button1 = tkinter.Button(pop_frame, text="Okay", image=self.pixelVirtual, width=self.button_width,
                                 height=self.button_height, compound="c", command=pop.destroy)
        button1.pack(pady=15)

    def create_register_warning(self):
        self.pixelVirtual = tkinter.PhotoImage(width=2, height=1)
        self.button_width = 80
        self.button_height = 30
        pop = tkinter.Toplevel(self)
        pop.title("Warning")
        pop.geometry("250x150+700+300")
        pop.config(bg="cyan")
        # Text warning
        pop_warning = tkinter.Label(pop, text="Please include all field!", font=("roboto sans-serif", 12),
                                    bg="cyan")
        pop_warning.pack(pady=10)
        # Warning button
        pop_frame = tkinter.Frame(pop, bg="cyan")
        pop_frame.pack(pady=5)
        button1 = tkinter.Button(pop_frame, text="Okay", image=self.pixelVirtual, width=self.button_width,
                                 height=self.button_height, compound="c", command=pop.destroy)
        button1.pack(pady=15)

    def create_usernamewarning(self):
        self.buttonVirtual = tkinter.PhotoImage(width=3, height=1)
        button_width = 80
        button_height = 30
        userwarning = tkinter.Toplevel(self)
        userwarning.title("Warning")
        userwarning.geometry("250x190+700+300")
        userwarning.config(bg="cyan")
        used_warning = tkinter.Label(userwarning, text="This Username has already been used",
                                     font=("roboto sans-serif", 10, "bold"), bg="cyan")
        used_warning.pack(expand=True, pady=10)
        used_warning_button = tkinter.Button(userwarning, text="Return", font=("Arial", 17),
                                             image=self.buttonVirtual, compound="c", height=button_height,
                                             width=button_width, command=userwarning.destroy)
        used_warning_button.pack(expand=True, pady=10)


    def change_page(self, page):
        new_page = self.pages[page]
        new_page.tkraise()

    def exit_button(self):
        time.sleep(1)
        sys.exit()

    def check_login(self):
        username = self.pages["LoginPage"].username_text.get()
        password = self.pages["LoginPage"].password_text.get()

        granted = self.config.login(username, password)
        if granted:
            self.change_page("MenuPage")
        else:
            self.create_falselogin()

    def gotoadmin(self):
        self.change_page("AdminPage")

    def gotopurchase(self):
        self.change_page("PurchasePage")

    def gotologin(self):
        self.change_page("LoginPage")

    def register(self):
        self.change_page("RegisterPage")

    def gotomenu(self):
        self.change_page("MenuPage")

    def addpurchase(self):
        self.change_page("AddPurchase")

    def exit_popup(self):
        self.pixelVirtual = tkinter.PhotoImage(width=2, height=1)
        self.button_width = 80
        self.button_height = 30

        pop = tkinter.Toplevel(self)
        pop.title("Warning")
        pop.geometry("250x150+700+300")
        pop.config(bg="cyan")
        # Text warning
        pop_warning = tkinter.Label(pop, text="Are you sure to exit?", font=("roboto sans-serif", 14), bg="cyan")
        pop_warning.pack(pady=10)
        # Warning button
        pop_frame = tkinter.Frame(pop, bg="cyan")
        pop_frame.pack(pady=5)
        button1 = tkinter.Button(pop_frame, text="Yes", image=self.pixelVirtual, width=self.button_width,
                                 height=self.button_height, compound="c", command=self.exit_button)
        button1.pack(side="left", pady=10, padx=10)
        button2 = tkinter.Button(pop_frame, text="No", image=self.pixelVirtual, width=self.button_width,
                                 height=self.button_height, compound="c", command=pop.destroy)
        button2.pack(side="right", pady=10, padx=10)

    def save_user(self):
        first_name = self.pages["RegisterPage"].first_name_text.get()
        last_name = self.pages["RegisterPage"].last_name_text.get()
        new_username = self.pages["RegisterPage"].username_text.get()
        new_password = self.pages["RegisterPage"].password_text.get()
        phone_number = self.pages["RegisterPage"].phone_text.get()
        email = self.pages["RegisterPage"].email_text.get()
        if first_name != "" and last_name != "" and new_username != "" and new_password != "" and email != "" and phone_number != "":
            if new_username in self.users:
                self.create_usernamewarning()
            else:
                self.users[new_username] = {
                    "first_name": first_name,
                    "last_name" : last_name,
                    "password" : new_password,
                    "email": email,
                    "phone" : phone_number,
                    "level": "admin"
                }
                with open("./data/users.json", "w") as file:
                    json.dump(self.users, file)
                self.create_admin_page()
                self.change_page("LoginPage")
        else:
            self.create_register_warning()


    def add_purchase(self):
        customer = self.pages["AddPurchase"].customer_name_text.get()
        product = self.pages["AddPurchase"].product_name_text.get()
        amount = self.pages["AddPurchase"].amount_text.get()
        address = self.pages["AddPurchase"].address_text.get()
        date = self.pages["AddPurchase"].date_text.get()
        price = self.pages["AddPurchase"].price_text.get()
        retailer = self.pages["AddPurchase"].retailer_text.get()
        #print(customer)
        #print(len(self.purchases))
        new_purchase = f"purchase{len(self.purchases)+1}"
        #print(new_purchase)
        if customer != "" and product != "" and amount != "" and address != "" and date != "" and price != "" and retailer != "":
            self.purchases[new_purchase] = {
                "customer_name": customer,
                "product_name": product,
                "amount": amount,
                "address": address,
                "transact_date": date,
                "product_price": price,
                "retailer_name": retailer
            }
        with open("./data/purchases.json", "w") as file:
            json.dump(self.purchases, file)
        self.create_purchase_page()
        self.change_page("PurchasePage")

class App:

    def __init__(self):
        self.config = Config()
        self.window = Window(self)

    def run(self):
        self.window.mainloop()


def main():
    my_app = App()
    my_app.run()

if __name__ == "__main__":
    main()