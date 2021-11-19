class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        self.age = 4

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(customers):
        for c in customers:
            print(c)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    __hash__ = None

    __repr__ = __str__




customers = [Customer("Kfir", "Gold"),
             Customer("Yadin", "Silver")]

Customer.print_all_customers(customers)

print(customers)
