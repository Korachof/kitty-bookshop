import items


class Store:
    def __init__(self, name, inventory, description):
        self._name = name
        self._inventory = inventory
        self._description = description

    def get_name(self):
        """returns the Store name (STR)"""
        return self._name
    
    def get_inventory(self):
        """returns the Store inventory (DICT)"""
        return self._inventory
    
    def add_to_inventory(self, item):
        """adds an item object to the inventory (DICT)"""
        self._inventory[item.get_genre()] = item

    def get_description(self):
        """returns the Store description (STR)"""
        return self._description


class PetStore(Store):
    def __init__(self, name, inventory, description):
        super().__init__(name, inventory, description)


class GroceryStore(Store):
    def __init__(self, name, inventory, description):
        super().__init__(name, inventory, description)
