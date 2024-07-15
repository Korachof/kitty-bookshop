class Item:
    def __init__(self, name, description, price):
        self._name = name
        self._description = description
        self._price = price


class Book(Item):
    def __init__(self, name, author, description, edition_bool, signed_bool, price):
        super().__init__(name, description, price)
        self._author = author
        self._edition_bool = edition_bool
        self._signed_bool = signed_bool


class Food(Item):
    def __init__(self, name, description, price):
        super().__init__(name, description, price)


class Toy(Item):
    def __init__(self, name, description, price):
        super().__init__(name, description, price)
