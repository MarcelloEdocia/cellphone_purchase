import tkinter
from tkinter import ttk
from json import dump


class Purchase(tkinter.Frame):

    def __init__(self, parent, App):
        self.application = App
        self.config = App.config
        super().__init__(parent)
        self.configure(bg="cyan")

        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.purchases = self.config.load_purchase()

        #Label
        self.space = tkinter.Label(self, text="", font=("roboto sans-serif",25), bg="cyan", fg="white")
        self.space.grid(row=0, column=0)
        self.title = tkinter.Label(self, text="Purchases List", font=("roboto sans-serif", 25), bg="cyan", fg="black")
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

        # List
        self.style = ttk.Style()
        self.style.configure("my_style.Treeview", hightlightthickness=0, font=("roboto sans-serif", 9), rowheight=25,
                             bd=0)
        self.style.configure("my_style.Treeview.Heading", font=("roboto sans-serif", 9, "bold"), fg="black")

        self.purchase_treeview = ttk.Treeview(self.list_frame, style="my_style.Treeview",
                                           yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.config(command=self.purchase_treeview.yview)

        self.purchase_treeview['columns'] = ("List", "Product", "Quantity", "Price (per product)", "Retailer", "Customer", "Address", "Transact Date")
        self.purchase_treeview.column("#0", width=0, stretch=tkinter.NO)
        self.purchase_treeview.column("List", anchor=tkinter.CENTER, width=30)
        self.purchase_treeview.column("Product", anchor=tkinter.CENTER, width=114)
        self.purchase_treeview.column("Quantity", anchor=tkinter.CENTER, width=60)
        self.purchase_treeview.column("Price (per product)", anchor=tkinter.CENTER, width=120)
        self.purchase_treeview.column("Retailer", anchor=tkinter.CENTER, width=95)
        self.purchase_treeview.column("Customer", anchor=tkinter.CENTER, width=95)
        self.purchase_treeview.column("Address", anchor=tkinter.CENTER, width=90)
        self.purchase_treeview.column("Transact Date", anchor=tkinter.CENTER, width=100)

        #Creating Headings
        self.purchase_treeview.heading("#0", text="", anchor=tkinter.W)
        self.purchase_treeview.heading("List",text="List", anchor=tkinter.CENTER)
        self.purchase_treeview.heading("Product",text="Product",anchor=tkinter.CENTER)
        self.purchase_treeview.heading("Quantity", text="Quantity", anchor=tkinter.CENTER)
        self.purchase_treeview.heading("Price (per product)", text="Price (per product)", anchor=tkinter.CENTER)
        self.purchase_treeview.heading("Retailer", text="Retailer", anchor=tkinter.CENTER)
        self.purchase_treeview.heading("Customer", text="Customer", anchor=tkinter.CENTER)
        self.purchase_treeview.heading("Address", text="Address", anchor=tkinter.CENTER)
        self.purchase_treeview.heading("Transact Date", text="Transact Date", anchor=tkinter.CENTER)

        all_purchases = self.purchases
        count = 0
        index = 1
        for purchase in all_purchases:
            list_order = str(index)
            product_name = f"{all_purchases[purchase]['product_name']}"
            quantity = f"{all_purchases[purchase]['amount']}"
            price = f"{all_purchases[purchase]['product_price']}"
            retailer_name = f"{all_purchases[purchase]['retailer_name']}"
            customer_name = f"{all_purchases[purchase]['customer_name']}"
            address = f"{all_purchases[purchase]['address']}"
            transact_date = f"{all_purchases[purchase]['transact_date']}"
            self.purchase_treeview.insert(parent="", index="end", iid=count, text="", values=(list_order, product_name, quantity, price, retailer_name, customer_name, address, transact_date))
            count += 1
            index += 1
        self.purchase_treeview.pack(expand=True)

        self.add_button = tkinter.Button(self.button_frame, text="Add New Purchase", width=15, height=1, bd=2,
                                          relief=tkinter.FLAT, bg="white", fg="black",
                                          font=("roboto sans-serif", 10, "bold"), command=lambda:self.application.addpurchase())
        self.add_button.pack(expand=True, pady=3)

        self.edit_button = tkinter.Button(self.button_frame, text="Edit Purchase", width=15, height=1, bd=2, relief=tkinter.FLAT, bg="white", fg="black", font=("roboto sans-serif", 10, "bold"), command=self.edit_purchase)
        self.edit_button.pack(expand=True, pady=3)

        self.delete_button = tkinter.Button(self.button_frame, text="Delete Purchase", width=15, height=1, bd=2,
                                          relief=tkinter.FLAT, bg="white", fg="black",
                                          font=("roboto sans-serif", 10, "bold"), command=self.delete_purchase)
        self.delete_button.pack(expand=True, pady=3)

        self.return_button = tkinter.Button(self.button_frame, text="Back to Menu", width=15, height=1, bd=2, relief=tkinter.FLAT, bg="white", fg="black", font=("roboto sans-serif", 10, "bold"), command=lambda:self.application.gotomenu())
        self.return_button.pack(expand=True)


    def delete_purchase(self):
        try:
            selected = self.purchase_treeview.focus()
            #print(self.purchase_treeview.item(selected)['values'][0])
            index = self.purchase_treeview.item(selected)['values'][0]
            index = int(index)
            order = f"purchase{index}"
            #print(self.purchases[order])
            del self.purchases[order]
            with open(self.config.purchase_path, "w") as file:
                dump(self.purchases, file)
            self.purchase_treeview.delete(selected)
        except:
            print("You have to choose one of the items before editing!")

    def edit_purchase(self):
        try:
            self.selected = self.purchase_treeview.focus()
            self.index = self.purchase_treeview.item(self.selected)['values'][0]
            self.index = int(self.index)
            self.order = f"purchase{self.index}"
                #print(self.purchases[order]['customer_name'])
                # self.purchases[order] = {
                #
                # }
            self.pop = tkinter.Toplevel(self)
            self.pop.configure(bg="cyan")
            self.pop.geometry("730x500+500+200")

            title_frame = tkinter.Frame(self.pop, relief=tkinter.RIDGE, bg="cyan")
            title_frame.place(x=0, y=0, width=729, height=100)

            title_label = tkinter.Label(title_frame, text="Edit Purchase", bd=5, relief=tkinter.RIDGE,
                                                 bg="cyan",
                                                 fg="black", font=("roboto sans-serif", 24), pady=17)
            title_label.pack(side=tkinter.TOP, fill=tkinter.X)

            form_frame = tkinter.Frame(self.pop, bd=5, relief=tkinter.RIDGE, bg="cyan")
            form_frame.place(x=0, y=75, width=729, height=425)

            self.customer_name_text = tkinter.StringVar()
            customer_name_label = tkinter.Label(form_frame, text="Customer       :",
                                                         font=("roboto sans-serif", 14),
                                                         bg="cyan", fg="black", padx=7, pady=30)
            customer_name_label.grid(row=3, column=3, sticky=tkinter.W)
            customer_entry = tkinter.Entry(form_frame, textvariable=self.customer_name_text, width=20, bd=5,
                                                    font=("roboto sans-serif", 14))
            customer_entry.insert(0, self.purchases[self.order]['customer_name'])
            customer_entry.grid(row=3, column=4)

            self.product_name_text = tkinter.StringVar()
            product_name_label = tkinter.Label(form_frame, text="Product       :", font=("roboto sans-serif", 14),
                                                        bg="cyan", fg="black", padx=5, pady=30)
            product_name_label.grid(row=3, column=5, sticky=tkinter.W)
            product_entry = tkinter.Entry(form_frame, textvariable=self.product_name_text, width=18, bd=5,
                                                   font=("roboto sans-serif", 14))
            product_entry.insert(0, self.purchases[self.order]['product_name'])
            product_entry.grid(row=3, column=6)

            self.amount_text = tkinter.StringVar()
            amount_label = tkinter.Label(form_frame, text="Amount           : ", font=("roboto sans-serif", 14),
                                                  bg="cyan", fg="black", padx=7, pady=30)
            amount_label.grid(row=4, column=3, sticky=tkinter.W)
            amount_entry = tkinter.Entry(form_frame, textvariable=self.amount_text, width=20, bd=5,
                                                  font=("roboto sans-serif", 14))
            amount_entry.insert(0, self.purchases[self.order]['amount'])
            amount_entry.grid(row=4, column=4)

            self.address_text = tkinter.StringVar()
            address_label = tkinter.Label(form_frame, text="Address      : ", font=("roboto sans-serif", 14),
                                                   bg="cyan", fg="black", padx=5, pady=30)
            address_label.grid(row=4, column=5, sticky=tkinter.W)
            address_entry = tkinter.Entry(form_frame, textvariable=self.address_text, width=18, bd=5,
                                                   font=("roboto sans-serif", 14))
            address_entry.insert(0, self.purchases[self.order]['address'])
            address_entry.grid(row=4, column=6)

            self.date_text = tkinter.StringVar()
            date_label = tkinter.Label(form_frame, text="Transact Date : ", font=("roboto sans-serif", 14),
                                                bg="cyan", fg="black", padx=5, pady=30)
            date_label.grid(row=5, column=3, sticky=tkinter.W)
            date_entry = tkinter.Entry(form_frame, textvariable=self.date_text, width=20, bd=5,
                                                font=("roboto sans-serif", 14))
            date_entry.insert(0, self.purchases[self.order]['transact_date'])
            date_entry.grid(row=5, column=4)

            self.price_text = tkinter.StringVar()
            price_label = tkinter.Label(form_frame, text="Price           : ", font=("roboto sans-serif", 14),
                                                 bg="cyan", fg="black", padx=5, pady=30)
            price_label.grid(row=5, column=5, sticky=tkinter.W)
            price_entry = tkinter.Entry(form_frame, textvariable=self.price_text, width=18, bd=5,
                                                 font=("roboto sans-serif", 14))
            price_entry.insert(0 , self.purchases[self.order]['product_price'])
            price_entry.grid(row=5, column=6)

            self.retailer_text = tkinter.StringVar()
            retailer_label = tkinter.Label(form_frame, text="Retailer           :",
                                                    font=("roboto sans-serif", 14), bg="cyan", fg="black", padx=5, pady=30)
            retailer_label.grid(row=6, column=3, sticky=tkinter.W)
            retailer_entry = tkinter.Entry(form_frame, textvariable=self.retailer_text, width=20, bd=5,
                                                    font=("roboto sans-serif", 14))
            retailer_entry.insert(0, self.purchases[self.order]['retailer_name'])
            retailer_entry.grid(row=6, column=4)

            button_frame = tkinter.Frame(form_frame, bd=0, relief=tkinter.RIDGE, bg="cyan")
            button_frame.place(x=0, y=340, width=720, height=170)

            space = tkinter.Label(button_frame, text="                       ", font=("roboto sans-serif", 14),
                                           fg="white", bg="cyan")
            space.grid(row=2, column=3)

            edit_purchase_button = tkinter.Button(button_frame, text="Save", width=15, height=1, bd=2,
                                                          relief=tkinter.FLAT, font=("roboto sans-serif", 12, "bold"), command=self.save_edit_purchase)
            edit_purchase_button.grid(row=2, column=4, padx=60, pady=34)
            cancel_button = tkinter.Button(button_frame, text="Cancel", width=15, height=1, bd=2,
                                                    relief=tkinter.FLAT, font=("roboto sans-serif", 12, "bold"),
                                                    command=self.pop.destroy)
            cancel_button.grid(row=2, column=5, pady=34, padx=15)
        except:
            print("You need to click on the item you want to edit !")

    def save_edit_purchase(self):
        new_customer = self.customer_name_text.get()
        new_product = self.product_name_text.get()
        new_amount = self.amount_text.get()
        new_address = self.address_text.get()
        new_date = self.date_text.get()
        new_price = self.price_text.get()
        new_retailer = self.retailer_text.get()

        # print(self.order)
        self.purchases[self.order] = {
            "customer_name": new_customer,
            "product_name": new_product,
            "amount": new_amount,
            "address": new_address,
            "transact_date": new_date,
            "product_price": new_price,
            "retailer_name": new_retailer,
        }
        with open("./data/purchases.json", "w") as file:
            dump(self.purchases, file)
        #print(self.purchases[self.order])
        self.purchase_treeview.item(self.selected, text="", values=(self.index, new_product, new_amount, new_price,new_retailer, new_customer, new_address, new_date))
        self.pop.destroy()











