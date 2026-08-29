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

        data = pandas.read_csv("cust-id.csv", index_col=0)
        id_length = len(data) + 1000
        print(f"ID created successfully")
        print(f"ID - {id_length}")

        new_customer_row = pandas.DataFrame([{"Name":self.name,
                                              "Age":self.age,
                                              "Gender":self.gender,
                                              "Email":self.email,
                                              "Phone":self.phone,
                                              "ID": id_length}],
                                               index=[id_length])
        data = pandas.concat([data, new_customer_row])
        data.to_csv("cust-id.csv")
