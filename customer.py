import pandas

class NewCustomer:
    def __init__(self):
        pass

    def persnal_info(self):
        self.name = input("Please input your name :")
        self.age = input("Please input your age :")
        self.gender = input("Please input your gender[M/F] :")
        self.email = input("Please input your email address :")
        self.phone = input("Please input your phone number :")
        new_customer_data = {"ID":["id number"],
                             "Name":[self.name],
                             "age":[self.age],
                             "Gender":[self.gender],
                             "Email":[self.email],
                             "Phone":[self.phone]}
        data = pandas.DataFrame(new_customer_data)
        data.to_csv("cust-id.csv", mode="a")
