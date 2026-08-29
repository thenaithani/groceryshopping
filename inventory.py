import pandas
from pandas.errors import EmptyDataError


class Inventory:

    def __init__(self):
        pass

    def add_stuff(self):
        try:
            inventory_data = pandas.read_csv("inventory.csv", index_col=0)

            self.name = input("Displayed Name -")
            self.category = input("Displayed Category -")
            self.price = input("Displayed Price -")
            self.quantity = input("Displayed Quantity -")

            df = pandas.DataFrame([{"Name": self.name,
                                    "Category": self.category,
                                    "Price": self.price,
                                    "Quantity": self.quantity}],
                                  index=[self.category])

            to_add = pandas.concat([inventory_data, df])
            to_add.index.name = "Category-index"
            to_add.to_csv("inventory.csv")

        except EmptyDataError ,FileNotFoundError:
            self.name = input("Displayed Name -")
            self.category = input("Displayed Category -")
            self.price = input("Displayed Price -")
            self.quantity = input("Displayed Quantity -")

            df = pandas.DataFrame([{"Name":self.name,
                                    "Category":self.category,
                                    "Price":self.price,
                                    "Quantity":self.quantity}],
                                  index= [self.category])
            df.to_csv("inventory.csv")
