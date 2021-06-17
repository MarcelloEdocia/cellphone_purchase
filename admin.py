import tkinter
from tkinter import ttk

class Admin(tkinter.Frame):

    def __init__(self, parent, App):
        self.application = App
        self.config = App.config
        super().__init__(parent)
        self.configure(bg="cyan")

        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.users = self.config.load_user()

        #Label
        self.space = tkinter.Label(self, text="", font=("roboto sans-serif",25), bg="cyan", fg="white")
        self.space.grid(row=0, column=0)
        self.title = tkinter.Label(self, text="Admin Information", font=("roboto sans-serif", 25), bg="cyan", fg="black")
        self.title.grid(row=1, column=0)


        #Frame
        self.list_frame = tkinter.Frame(self, bd=0, relief=tkinter.RIDGE, bg="white", width=730, height=400)
        self.list_frame.grid(row=2, column=0)

        self.button_frame = tkinter.Button(self, relief=tkinter.RIDGE, bg="cyan", width=740, height=2, bd=0)
        self.button_frame.grid(row=3, column=0)

        self.grid_rowconfigure(2, weight=4)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Creating scrollbar
        self.tree_scroll = tkinter.Scrollbar(self.list_frame)
        self.tree_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        #List
        self.style = ttk.Style()
        self.style.configure("my_style.Treeview", hightlightthickness=0, bd=0)
        self.style.configure("my_style.Treeview.Heading", font=("roboto sans-serif", 10, "bold"), fg="black")

        self.admin_treeview = ttk.Treeview(self.list_frame, style="my_style.Treeview", yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.config(command=self.admin_treeview.yview)

        self.admin_treeview['columns'] = ("Username", "Phone Number")
        self.admin_treeview.column("#0", width=0, stretch=tkinter.NO)
        self.admin_treeview.column("Username", anchor=tkinter.CENTER, width=370)
        self.admin_treeview.column("Phone Number", anchor=tkinter.CENTER, width=370)

        #Creating Headings
        self.admin_treeview.heading("#0", text="", anchor=tkinter.W)
        self.admin_treeview.heading("Username",text="Username", anchor=tkinter.CENTER)
        self.admin_treeview.heading("Phone Number",text="Phone Number",anchor=tkinter.CENTER)

        users = self.users
        count = 0
        for user in users:
            #print(users[user]["email"])
            username = user
            phone_number = f"{users[user]['phone']}"
            self.admin_treeview.insert(parent="", index="end", iid=count, text="", values=(username, phone_number))
            count += 1
        self.admin_treeview.pack(expand=True)
       # self.admin_treeview.bind("<Double-1>", self.doubleclick)

        #Buttons
        self.view_information_button = tkinter.Button(self.button_frame, text="View Information", width=15, height=2, bd=2, relief=tkinter.FLAT, bg="white", fg="black", font=("roboto sans-serif", 10, "bold"), command=self.information_popup)
        self.view_information_button.pack(expand=True, pady=7)

        self.return_button = tkinter.Button(self.button_frame, text="Back to Menu", width=15, height=2, bd=2, relief=tkinter.FLAT, bg="white", fg="black", font=("roboto sans-serif", 10, "bold"), command=lambda:self.application.gotomenu())
        self.return_button.pack(expand=True)

    def information_popup(self):
        try:
            selected = self.admin_treeview.focus()
            values = self.admin_treeview.item(selected, "values")
            admin_username = values[0]
            # print(self.users[admin_username])

            new_window = tkinter.Toplevel(self)
            new_window.title("Admin Information")
            new_window.geometry("470x350+700+300")
            new_window.config(bg="cyan")

            new_window.grid_rowconfigure(1, weight=4)
            new_window.grid_rowconfigure(2, weight=1)
            new_window.grid_columnconfigure(1, weight=1)

            information_frame = tkinter.Frame(new_window, height=287, width=468, bg="cyan", bd=4, relief=tkinter.RIDGE)
            information_frame.grid(row=1, column=1)

            username = tkinter.Label(information_frame, text=f"Username: {admin_username}", font=("roboto sans-serif", 13), padx=20, pady=5, bg="cyan")
            username.pack(expand=True)

            front_name = tkinter.Label(information_frame, text=f"Front Name: {self.users[admin_username]['first_name']}", font=("roboto sans-serif", 13), padx=20, pady=7, bg="cyan")
            front_name.pack(expand=True)

            last_name = tkinter.Label(information_frame, text=f"Last Name: {self.users[admin_username]['last_name']}", font=("roboto sans-serif", 13), padx=20, pady=7, bg="cyan")
            last_name.pack(expand=True)

            phone_number = tkinter.Label(information_frame, text=f"Phone Number: {self.users[admin_username]['phone']}", font=("roboto sans-serif", 13), padx=20, pady=7, bg="cyan")
            phone_number.pack(expand=True)

            email = tkinter.Label(information_frame, text=f"Email: {self.users[admin_username]['email']}", font=("roboto sans-serif", 13), padx=20, pady=7, bg="cyan")
            email.pack(expand=True)

            button_frame = tkinter.Frame(new_window, height=70, width=468, bg="cyan", bd=0, relief=tkinter.RIDGE)
            button_frame.grid(row=2, column=1)

            return_button = tkinter.Button(button_frame, height=1, width=5, bg="white", fg="black", font=("roboto sans-serif", 12, "bold"), text="Return", command=new_window.destroy)
            return_button.pack(expand=True, padx=20, pady=20)
        except:
            print("You have to choose one of the admins before you can view the information!")











