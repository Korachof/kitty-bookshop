class Store:
    def __init__(self, name, inventory, description):
        self._name = name
        self._inventory = inventory
        self._description = description


class PetStore(Store):
    def __init__(self, name, inventory, description):
        super().__init__(name, inventory, description)


class GroceryStore(Store):
    def __init__(self, name, inventory, description):
        super().__init__(name, inventory, description)
