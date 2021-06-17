import tkinter

class Register(tkinter.Frame):

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

        self.title_label = tkinter.Label(self.title_frame, text="Register Form", bd=5, relief=tkinter.RIDGE, bg="cyan",
                                         fg="black", font=("roboto sans-serif", 24), pady=17)
        self.title_label.pack(side=tkinter.TOP, fill=tkinter.X)

        self.form_frame = tkinter.Frame(self, bd=5, relief=tkinter.RIDGE, bg="cyan")
        self.form_frame.place(x=0, y=75, width=729, height=425)

        self.first_name_text = tkinter.StringVar()
        self.firstname_label = tkinter.Label(self.form_frame, text="First Name: ", font=("roboto sans-serif", 14), bg="cyan", fg="black", padx=7, pady=30)
        self.firstname_label.grid(row=3, column=3, sticky=tkinter.W)
        self.firstname_entry = tkinter.Entry(self.form_frame, textvariable=self.first_name_text, width=20, bd=5, font=("roboto sans-serif", 14))
        self.firstname_entry.grid(row=3, column=4)

        self.last_name_text = tkinter.StringVar()
        self.lastname_label = tkinter.Label(self.form_frame, text="Last Name: ", font=("roboto sans-serif", 14),
                                             bg="cyan", fg="black", padx=5, pady=30)
        self.lastname_label.grid(row=3, column=5, sticky=tkinter.W)
        self.lastname_entry = tkinter.Entry(self.form_frame, textvariable=self.last_name_text, width=20, bd=5,
                                             font=("roboto sans-serif", 14))
        self.lastname_entry.grid(row=3, column=6)

        self.username_text = tkinter.StringVar()
        self.username_label = tkinter.Label(self.form_frame, text="Username: ", font=("roboto sans-serif", 14), bg="cyan", fg="black", padx=7, pady=30)
        self.username_label.grid(row=4, column=3, sticky=tkinter.W)
        self.username_entry = tkinter.Entry(self.form_frame, textvariable=self.username_text, width=20, bd=5, font=("roboto sans-serif", 14))
        self.username_entry.grid(row=4, column=4)

        self.email_text = tkinter.StringVar()
        self.email_label = tkinter.Label(self.form_frame, text="        Email : ", font=("roboto sans-serif", 14), bg="cyan", fg="black", padx=5, pady=30)
        self.email_label.grid(row=4, column=5, sticky=tkinter.W)
        self.email_entry = tkinter.Entry(self.form_frame, textvariable=self.email_text, width=20, bd=5, font=("roboto sans-serif", 14))
        self.email_entry.grid(row=4, column=6)

        self.password_text = tkinter.StringVar()
        self.password_label = tkinter.Label(self.form_frame, text="Password: ", font=("roboto sans-serif", 14), bg="cyan", fg="black", padx=5, pady=30)
        self.password_label.grid(row=5, column=3, sticky=tkinter.W)
        self.password_entry = tkinter.Entry(self.form_frame, textvariable=self.password_text, width=20, bd=5, font=("roboto sans-serif", 14))
        self.password_entry.grid(row=5, column=4)

        self.phone_text = tkinter.StringVar()
        self.phone_label = tkinter.Label(self.form_frame, text="Phone num : ", font=("roboto sans-serif", 14), bg="cyan", fg="black", padx=5, pady=30)
        self.phone_label.grid(row=5, column=5, sticky=tkinter.W)
        self.phone_entry = tkinter.Entry(self.form_frame, textvariable=self.phone_text, width=20, bd=5, font=("roboto sans-serif", 14))
        self.phone_entry.grid(row=5, column=6)

        self.button_frame = tkinter.Frame(self.form_frame, bd=0, relief=tkinter.RIDGE, bg="cyan")
        self.button_frame.place(x=0, y=280, width=720, height=170)

        self.space = tkinter.Label(self.button_frame, text="                       ", font=("roboto sans-serif", 14), fg="white", bg="cyan")
        self.space.grid(row=2, column=3)

        self.register_button = tkinter.Button(self.button_frame, text="Submit", width=15, height=2, bd=2, relief=tkinter.FLAT, font=("roboto sans-serif", 12, "bold"), command=lambda:self.application.save_user())
        self.register_button.grid(row=2, column=4, padx=60, pady=34)

        self.cancel_button = tkinter.Button(self.button_frame, text="Cancel", width=15, height=2, bd=2, relief=tkinter.FLAT, font=("roboto sans-serif", 12, "bold"), command=lambda:self.application.gotologin())
        self.cancel_button.grid(row=2, column=5, pady=34, padx=15)