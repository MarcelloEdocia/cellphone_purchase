import tkinter

class MenuPage(tkinter.Frame):

    def __init__(self, parent, App):
        self.application = App
        self.config = App.config
        super().__init__(parent)
        self.configure(bg="grey")

        self.grid(row=0, column=0, stick="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        #Frame
        self.text_frame = tkinter.Frame(self, bd=4, relief=tkinter.RIDGE, bg="cyan")
        self.text_frame.place(x=0, y=0, width=735, height=510)

        #Button Frames
        self.button_frame = tkinter.Frame(self, bd=4, relief=tkinter.RIDGE, bg="cyan")
        self.button_frame.place(x=130, y=68, width=490, height=350)

        #Admins
        self.see_admin_button = tkinter.Button(self.button_frame, text="Admin Informations", width=45, height=3, bd=2, relief=tkinter.FLAT, bg="white", fg="black", font=("roboto sans-serif", 11, "bold"), command=lambda:self.application.gotoadmin())
        self.see_admin_button.grid(row=1, column=5, pady=35, padx=33)

        #View all the purchases
        self.see_purchase_button = tkinter.Button(self.button_frame, text="Purchases List", width=45, height=3, bd=2, relief=tkinter.FLAT, bg="white", fg="black", font=("roboto sans-serif", 11, "bold"), command=lambda:self.application.gotopurchase())
        self.see_purchase_button.grid(row=2, column=5)

        #Exit Button
        self.exit_button = tkinter.Button(self.button_frame, text="Exit System", width=45, height=3, bd=2, relief=tkinter.FLAT, bg="white", fg="black", font=("roboto sans-serif", 11, "bold"), command=lambda:self.application.exit_popup())
        self.exit_button.grid(row=3, column=5, pady=35, padx=33)

