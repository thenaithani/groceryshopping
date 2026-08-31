from operator import index

import pandas
from pandas.errors import EmptyDataError


class Inventory:

    def __init__(self):
        pass

    def add_stuff(self):
        try:
            inventory_data = pandas.read_csv("inventory.csv")

            self.name = input("Displayed Name -")
            self.category = input("Displayed Category -")
            self.price = input("Displayed Price -")
            self.quantity = input("Displayed Quantity -")
            self.per = input("-Per -")

            df = pandas.DataFrame([{"Name": self.name,
                                    "Category": self.category,
                                    "Price": self.price,
                                    "Quantity": self.quantity,
                                    "-per":self.per}])

            to_add = pandas.concat([inventory_data, df])
            to_add.to_csv("inventory.csv",index=False)

        except EmptyDataError ,FileNotFoundError:
            self.name = input("Displayed Name -")
            self.category = input("Displayed Category -")
            self.price = input("Displayed Price -")
            self.quantity = input("Displayed Quantity -")
            self.per = input("-Per -")

            df = pandas.DataFrame([{"Name":self.name,
                                    "Category":self.category,
                                    "Price":self.price,
                                    "Quantity":self.quantity,
                                    "-per":self.per}])
            df.to_csv("inventory.csv", index=False)

    def check_inventory(self):
        try:
            inventory_data = pandas.read_csv("inventory.csv")
            print(inventory_data)

        except EmptyDataError:
            print("Inventory is empty")

        except FileNotFoundError:
            print("Inventory Not Yet Initialized")

    def change_price(self):
        try:
            with open("bars.txt", encoding="utf-8") as bars:
                print(bars.read())

            inventory_data = pandas.read_csv("inventory.csv", index_col="Name")
            print(inventory_data)

            with open("bars.txt", encoding="utf-8") as bars:
                print(bars.read())
            loc_value = input("Enter index loc value (index = Name) -")

            list_to_change = inventory_data.loc[loc_value, ["Price"]].tolist()
            print(f"Old Price = {list_to_change[0]}")

            price = int(input("Enter new price -"))
            inventory_data.loc[loc_value, ["Price"]] = price
            inventory_data.to_csv("inventory.csv")


        except EmptyDataError:
            print("Inventory is empty")
        except FileNotFoundError:
            print("Inventory Not Yet Initialized")


