from abc import ABC, abstractmethod


class User:
    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._age = None
        self._phone_number = None
        self._address = None
        self._email_address = None

    def set_firstname(self, first_name):
        self._first_name = first_name

    def set_lastname(self, last_name):
        self._last_name = last_name

    def set_age(self, age):
        self._age = age

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_address(self, address):
        self._address = address

    def set_email_address(self, email_address):
        self._email_address = email_address

    @property
    def firstname(self):
        return self._first_name

    @property
    def lastname(self):
        return self._last_name

    @property
    def age(self):
        return self._age

    @property
    def phonenumber(self):
        return self._phone_number

    @property
    def address(self):
        return self._address

    @property
    def emailaddress(self):
        return self._email_address

    def display(self):
        print(f"\n First Name: {self.firstname}\n Last Name: {self.lastname}")


class UserBuilder(ABC):

    @abstractmethod
    def add_firstname(self, f_name):
        pass

    @abstractmethod
    def add_lastname(self, l_name):
        pass

    @abstractmethod
    def add_age(self, age=None):
        pass

    @abstractmethod
    def add_phone_number(self, ph_number=None):
        pass

    @abstractmethod
    def add_address(self, addrs=None):
        pass

    @abstractmethod
    def add_email_address(self, email_addrs):
        pass


class CustomUserBuilder(UserBuilder):

    def __init__(self):
        self.user = User()

    def add_firstname(self, f_name):
        self.user.set_firstname(f_name)
        return self

    def add_lastname(self, l_name):
        self.user.set_lastname(l_name)
        return self

    def add_age(self, age=None):
        self.user.set_age(age)
        return self

    def add_phone_number(self, ph_number=None):
        self.user.set_phone_number(ph_number)
        return self

    def add_address(self, addrs=None):
        self.user.set_address(addrs)
        return self

    def add_email_address(self, email_addrs):
        self.user.set_email_address(email_addrs)
        return self

    def get_user(self):
        return self.user


class UserDirector:
    def __init__(self, builder):
        self.builder = builder

    def create_user(self, params) -> User:
        self.builder.add_firstname(params.get("first_name"))
        self.builder.add_lastname(params.get("last_name"))
        self.builder.add_age(params.get("age"))
        self.builder.add_phone_number(params.get("phone_number"))
        self.builder.add_address(params.get("address"))
        self.builder.add_email_address(params.get("email"))
        return self.builder.get_user()


# Utilization of the code
data = {
    "first_name": "Shubham",
    "last_name": "Ranjan",
    "age": 20,
    "phone_number": 1234567,
    "address": "some address",
    "email": "abcd@gmail.com"
}

b = CustomUserBuilder()
d = UserDirector(b)
u = d.create_user(data)

print(u.firstname)
print(u.age)
