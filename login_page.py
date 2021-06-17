import tkinter

class LoginPage(tkinter.Frame):

    def __init__(self, parent, App):
        self.application = App
        self.config = App.config
        super().__init__(parent)
        self.configure(bg="cyan")

        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.title_frame = tkinter.Frame(self, relief=tkinter.RIDGE, bg="cyan")
        self.title_frame.place(x=0, y=0, width=729, height=100)

        self.title_label = tkinter.Label(self.title_frame, text="Login Form",bd=5, relief=tkinter.RIDGE, bg="cyan", fg="black", font=("roboto sans-serif", 24), pady=17)
        self.title_label.pack(side=tkinter.TOP, fill=tkinter.X)

        self.form_frame = tkinter.Frame(self, bd=5, relief=tkinter.RIDGE, bg="cyan")
        self.form_frame.place(x=0, y=75, width=729, height=425)

        self.space = tkinter.Label(self.form_frame, text="", bg="cyan", padx=20, pady=8)
        self.space.grid(row=3, column=3, sticky=tkinter.W)

        #Username
        self.username_text = tkinter.StringVar()
        self.username_label = tkinter.Label(self.form_frame, text="Username  : ", font=("roboto sans-serif", 18), bg="cyan", fg="black", padx=63, pady=40)
        self.username_label.grid(row=3, column=3, sticky=tkinter.W)
        self.username_entry = tkinter.Entry(self.form_frame, textvariable=self.username_text, width=32, bd=6, font=("roboto sans-serif", 18))
        self.username_entry.grid(row=3, column=4)

        #Password
        self.password_text = tkinter.StringVar()
        self.password_label = tkinter.Label(self.form_frame, text="Password  : ", font=("roboto sans-serif", 18),
                                            bg="cyan", fg="black", padx=63, pady=30)
        self.password_label.grid(row=4, column=3, sticky=tkinter.W)
        self.password_entry = tkinter.Entry(self.form_frame, textvariable=self.password_text, width=32, bd=6,
                                            font=("roboto sans-serif", 18))
        self.password_entry.grid(row=4, column=4)

        #Buttons Frame
        self.button_frame = tkinter.Frame(self.form_frame, bd=2, relief=tkinter.RIDGE, bg="cyan")
        self.button_frame.place(x=120, y=240, width=500, height=110)

        self.space_label = tkinter.Label(self.button_frame, text="", bg="cyan", padx=18)
        self.space_label.grid(row=2, column=0)

        #Buttons
        self.login_button = tkinter.Button(self.button_frame, text="Login Now", width=15, height=2, bd=3,relief=tkinter.FLAT, bg="white", fg="black", font=("roboto sans-serif",12, "bold"), command=lambda:self.application.check_login())
        self.login_button.grid(row=2, column=1, padx=26, pady=26)

        self.register_button = tkinter.Button(self.button_frame, text="Register Now", width=15, height=2, bd=3, relief=tkinter.FLAT, bg="white", fg="black", font=("roboto sans-serif", 12, "bold"), command=lambda:self.application.register())
        self.register_button.grid(row=2, column=2)

