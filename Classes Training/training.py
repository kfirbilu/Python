class User:
    def log(self):
        print(self)

class Funk:
    def speak(self):
        print("working")


class Teacher(User):
    def log(self):
        print("Im a teacher!")

    def bark(self):
        print("bark")


class Customer(Teacher,Funk):
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        self.age = 4

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self, name):
        del self._name

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




users = [Customer("Kfir", "Gold"),
         Customer("Yadin", "Silver"), Teacher()]

c = Customer("lior","gold")

c.speak()




