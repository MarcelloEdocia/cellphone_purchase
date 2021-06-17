import tkinter
from json import dump

class AddPurchase(tkinter.Frame):

    def __init__(self, parent, App):
        self.application = App
        self.config = App.config
        super().__init__(parent)
        self.configure(bg="cyan")

        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.purchases = self.config.load_purchase()

        self.title_frame = tkinter.Frame(self, relief=tkinter.RIDGE, bg="cyan")
        self.title_frame.place(x=0, y=0, width=729, height=100)

        self.title_label = tkinter.Label(self.title_frame, text="Add New Purchase", bd=5, relief=tkinter.RIDGE, bg="cyan",
                                         fg="black", font=("roboto sans-serif", 24), pady=17)
        self.title_label.pack(side=tkinter.TOP, fill=tkinter.X)

        self.form_frame = tkinter.Frame(self, bd=5, relief=tkinter.RIDGE, bg="cyan")
        self.form_frame.place(x=0, y=75, width=729, height=425)

        self.customer_name_text = tkinter.StringVar()
        self.customer_name_label = tkinter.Label(self.form_frame, text="Customer       :", font=("roboto sans-serif", 14),
                                             bg="cyan", fg="black", padx=7, pady=30)
        self.customer_name_label.grid(row=3, column=3, sticky=tkinter.W)
        self.customer_entry = tkinter.Entry(self.form_frame, textvariable=self.customer_name_text, width=20, bd=5,
                                             font=("roboto sans-serif", 14))
        self.customer_entry.grid(row=3, column=4)

        self.product_name_text = tkinter.StringVar()
        self.product_name_label = tkinter.Label(self.form_frame, text="Product       :", font=("roboto sans-serif", 14),
                                            bg="cyan", fg="black", padx=5, pady=30)
        self.product_name_label.grid(row=3, column=5, sticky=tkinter.W)
        self.product_entry = tkinter.Entry(self.form_frame, textvariable=self.product_name_text, width=18, bd=5,
                                            font=("roboto sans-serif", 14))
        self.product_entry.grid(row=3, column=6)

        self.amount_text = tkinter.StringVar()
        self.amount_label = tkinter.Label(self.form_frame, text="Amount           : ", font=("roboto sans-serif", 14),
                                            bg="cyan", fg="black", padx=7, pady=30)
        self.amount_label.grid(row=4, column=3, sticky=tkinter.W)
        self.amount_entry = tkinter.Entry(self.form_frame, textvariable=self.amount_text, width=20, bd=5,
                                            font=("roboto sans-serif", 14))
        self.amount_entry.grid(row=4, column=4)

        self.address_text = tkinter.StringVar()
        self.address_label = tkinter.Label(self.form_frame, text="Address      : ", font=("roboto sans-serif", 14),
                                         bg="cyan", fg="black", padx=5, pady=30)
        self.address_label.grid(row=4, column=5, sticky=tkinter.W)
        self.address_entry = tkinter.Entry(self.form_frame, textvariable=self.address_text, width=18, bd=5,
                                         font=("roboto sans-serif", 14))
        self.address_entry.grid(row=4, column=6)

        self.date_text = tkinter.StringVar()
        self.date_label = tkinter.Label(self.form_frame, text="Transact Date : ", font=("roboto sans-serif", 14),
                                            bg="cyan", fg="black", padx=5, pady=30)
        self.date_label.grid(row=5, column=3, sticky=tkinter.W)
        self.date_entry = tkinter.Entry(self.form_frame, textvariable=self.date_text, width=20, bd=5,
                                            font=("roboto sans-serif", 14))
        self.date_entry.grid(row=5, column=4)

        self.price_text = tkinter.StringVar()
        self.price_label = tkinter.Label(self.form_frame, text="Price           : ", font=("roboto sans-serif", 14),
                                        bg="cyan", fg="black", padx=5, pady=30)
        self.price_label.grid(row=5, column=5, sticky=tkinter.W)
        self.price_entry = tkinter.Entry(self.form_frame, textvariable=self.price_text, width=18, bd=5,
                                        font=("roboto sans-serif", 14))
        self.price_entry.grid(row=5, column=6)

        self.retailer_text = tkinter.StringVar()
        self.retailer_label = tkinter.Label(self.form_frame, text="Retailer           :", font=("roboto sans-serif", 14), bg="cyan", fg="black", padx=5, pady=30)
        self.retailer_label.grid(row=6, column=3, sticky=tkinter.W)
        self.retailer_entry = tkinter.Entry(self.form_frame, textvariable=self.retailer_text, width=20, bd=5, font=("roboto sans-serif", 14))
        self.retailer_entry.grid(row=6, column=4)


        self.button_frame = tkinter.Frame(self.form_frame, bd=0, relief=tkinter.RIDGE, bg="cyan")
        self.button_frame.place(x=0, y=340, width=720, height=170)

        self.space = tkinter.Label(self.button_frame, text="                       ", font=("roboto sans-serif", 14),
                                   fg="white", bg="cyan")
        self.space.grid(row=2, column=3)

        self.add_purchase_button = tkinter.Button(self.button_frame, text="Submit", width=15, height=1, bd=2,
                                              relief=tkinter.FLAT, font=("roboto sans-serif", 12, "bold"), command=lambda:self.application.add_purchase())
        self.add_purchase_button.grid(row=2, column=4, padx=60, pady=34)
        self.cancel_button = tkinter.Button(self.button_frame, text="Cancel", width=15, height=1, bd=2,
                                            relief=tkinter.FLAT, font=("roboto sans-serif", 12, "bold"),
                                            command=lambda:self.application.gotopurchase())
        self.cancel_button.grid(row=2, column=5, pady=34, padx=15)