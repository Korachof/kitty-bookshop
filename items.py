class Item:
    def __init__(self, name, description, price):
        self._name = name
        self._description = description
        self._price = price

    def get_name(self):
        """returns Item name (STR)"""
        return self._name
    
    def get_description(self):
        """returns Item description (STR)"""
        return self._description
    
    def get_price(self):
        """returns Item price (INT)"""
        return self._price


class Book(Item):
    def __init__(self, name, author, description, edition_bool, signed_bool, price):
        super().__init__(name, description, price)
        self._author = author
        self._edition_bool = edition_bool
        self._signed_bool = signed_bool

    def get_author(self):
        """returns Book author (STR)"""
        return self._author
    
    def get_edition_bool(self):
        """returns Book edition bool (BOOL)"""
        return self._edition_bool
    
    def get_signed_bool(self):
        """returns Book signed bool (BOOL)"""
        return self._signed_bool


class Food(Item):
    def __init__(self, name, category, description, price):
        super().__init__(name, description, price)
        self._category = category

    def get_category(self):
        """returns Item category"""
        return self._category


class Toy(Food):
    def __init__(self, name, category, description, price):
        super().__init__(name, category, description, price)