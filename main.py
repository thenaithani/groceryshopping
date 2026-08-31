import pandas
import time
import inventory
with open("Fresh-Grow.txt", encoding="utf-8") as logo:
    data = logo.read()
    print(data)
from customer import NewCustomer

running = True
login = input("Please login (Enter Fresh-Grow ID) \n{Type 'new' for a new customer} \n- ")


if login.lower() == "new":
    new_customer = NewCustomer()
    new_customer.persnal_info()

data = pandas.read_csv("cust-id.csv")
existing_id = data["ID"]
for i in existing_id:
    if login == str(i):
        print("Matched")

if login.lower() == "admin":
    password = input("Please enter your password: ")
    if password.lower() == "admin":
        admin = inventory.Inventory()
        with open("Welcome-Back-Cheif.txt", encoding="utf-8") as greet:
            print(greet.read())
        operations = str(input("""1- Add items
2- Check Inventory
3- Change Price
4- Customers List
5- Change Stock Quantity
6- Exit
- """))
        if operations == "1":
            admin.add_stuff()

        if operations == "2":
            admin.check_inventory()

        if operations == "3":
            admin.change_price()

        if operations == "4":
            customer_data = pandas.read_csv("cust-id.csv")
            print(customer_data.to_string(index=False))

        if operations == "5":
            print("to be added")

        if operations == "6":
            running = False
