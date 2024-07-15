class Bookshop:
    def __init__(self, name, inventory, lifetime_profits):
        self._name = name
        self._inventory = inventory
        self._lifetime_profits = lifetime_profits

    def get_name(self):
        """returns Bookshop name (STR)"""
        return self._name
    
    def get_inventory(self):
        """returns Bookshop inventory (DICT)"""
        return self._inventory
    
    def add_to_inventory(self):
        """adds an item object to the inventory (OBJ)"""
    
    def get_lifetime_profits(self):
        """returns Bookshop lifetime profits (INT)"""
        return self._lifetime_profits
    

    



