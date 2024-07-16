class Distributor:
    def __init__(self, book_inventory, rare_inventory):
        self._book_inventory = book_inventory
        self._rare_inventory = rare_inventory

    def get_book_inventory(self):
        """returns book inventory (DICT)
        {genre1: [book1, book2], genre2: [book3, book4]}"""
        return self._book_inventory
    
    def add_book_to_inventory(self, book):
        """add book item object to Distributor book_inventory (DICT)"""
        self._book_inventory[book.get_genre()].append(book)

    def get_rare_inventory(self):
        """returns Distributor rare_inventory (DICT)"""
        return self._rare_inventory
    
    def add_item_to_rare_inventory(self, item):
        """add item object to Distributor rare_inventory (DICT)"""
        self._rare_inventory[item.get_genre()].append(item)

    def remove_item_from_rare_inventory(self, remove_item):
        """remove item object from Distributor rare_inventory (DICT)"""
        count = 0
        for item in self._rare_inventory[remove_item.get_genre()]:
            if item.get_name() == remove_item.get_name():
                self._rare_inventory[remove_item.get_genre()].pop(count)
            count += 1

