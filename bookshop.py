import items

class Bookshop:
    def __init__(self, name, inventory, lifetime_profits):
        self._name = name
        self._inventory = inventory
        self._lifetime_profits = lifetime_profits

    def get_name(self):
        """returns Bookshop name (STR)"""
        return self._name
    
    def set_name(self, new_name):
        """edits the Bookshop name (STR) to new_name (STR)"""
        self._name = new_name
    
    def get_inventory(self):
        """returns Bookshop inventory (DICT)"""
        return self._inventory
    
    def add_to_inventory(self, item):
        """adds an item object to the inventory (DICT)"""
        self._inventory[item.get_genre()] = item

    def remove_from_inventory(self, remove_item):
        """removes an item object from the inventory (DICT)"""
        count = 0
        for item in self._inventory[remove_item.get_genre()]:
            if item.get_name() == remove_item.get_name():
                self._inventory[item.get_name()].pop(count)
            count += 1
    
    def get_lifetime_profits(self):
        """returns Bookshop lifetime profits (INT)"""
        return self._lifetime_profits
    
    def increment_lifetime_profits(self, amount):
        """add ammount to lifetime_profits"""
        self._lifetime_profits += amount
        return self._lifetime_profits
    

    



