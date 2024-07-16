from abc import ABC, abstractmethod

class Member(ABC):
    def __init__(self, member_id, name, email, password, home_address, phone):
        self.member_id = member_id
        self._name = name
        self._email = email
        self._password = password
        self._home_address = home_address
        self._phone = phone

    @property
    def name(self):
        return self._name

    @abstractmethod
    def display_info(self):
        pass

class Buyer(Member):
    def __init__(self, member_id, name, email, password, home_address, phone, shipping_address):
        super().__init__(member_id, name, email, password, home_address, phone)
        self._shipping_address = shipping_address

    def display_info(self):
        return f"Buyer: {self._name}, Shipping Address: {self._shipping_address}"

class Seller(Member):
    def __init__(self, member_id, name, email, password, home_address, phone, bank_account, routing_number):
        super().__init__(member_id, name, email, password, home_address, phone)
        self._bank_account = bank_account
        self._routing_number = routing_number

    def display_info(self):
        return f"Seller: {self._name}, Bank Account: {self._bank_account}"