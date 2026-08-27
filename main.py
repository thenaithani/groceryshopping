with open("Fresh-Grow.txt", encoding="utf-8") as logo:
    data = logo.read()
    print(data)
from customer import NewCustomer

login = input("Please login (Enter Fresh-Grow ID)"
      " {Type 'new' for a new customer} \n- ")
if login.lower() == "new":
    new_customer = NewCustomer()
    new_customer.persnal_info()

else:
    pass

