import bookshop
import customer
import distributor
import questboard


class User:
    def __init__(self, name: str, level: int, experience: int, bookshop: object, adopted_cats: list, money: int, distributor: object, customers: list, quest_board: object):
        self._name = name
        self._level = level
        self._experience = experience
        self._bookshop = bookshop
        self._adopted_cats = adopted_cats
        self._money = money
        self._distributor = distributor
        self._customers = customers
        self._questboard = quest_board
        self.set_level()

    def get_name(self):
        """returns User name (STR)"""
        return self._name
    
    def set_name(self, name):
        """sets User name (STR)
        parameter: name (STR)"""
        self._name = name

    def get_level(self):
        """returns User level (INT)"""
        return self._level
    
    def set_level(self):
        """sets User level (INT)"""
        # tentative Level Structure (IN PROGRESS)
        # Level 1: 0-99
        # Level 2: 100-199
        # Level 3: 200-299
        # etc
        if self._experience < 100:
            self._level = 1
        else:
            self._level = self._experience // 100

    def get_experience(self):
        """returns User experience (INT)"""
        return self._experience
    
    def increment_experience(self, amount):
        """adds amount (INT) to User experience (INT)
        parameter: amount (INT)
        returns: self._experience"""
        self._experience += amount
        self.set_level()
        return self._experience
    
    def get_bookshop(self):
        """returns User bookshop (OBJ)"""
        return self._bookshop
    
    def set_bookshop(self, name, inventory, lifetime_profits):
        """creates a Bookshop class object and sets it as User bookshop"""
        self._bookshop = bookshop.Bookshop(name, inventory, lifetime_profits)
        return self._bookshop
    
    def get_adopted_cats(self):
        """returns User adopted cats (LIST)"""
        return self._adopted_cats
    
    def get_money(self):
        """returns User money (INT)"""
        return self._money
    
    def increment_money(self, amount):
        """adds amount (INT) to money (INT)"""
        self._money += amount

    def get_distributor(self):
        """returns User distributor (OBJ)"""
        return self._distributor
    
    def set_distributor(self):
        """creates a distributor object and sets it as User distributor (OBJ)"""
        # still need to create Distributor class beyond pass and figure out attributes
        self._distributor = distributor.Distributor()

    def get_customers(self):
        """returns User customers list (LIST)"""
        return self._customers
    
    def add_customer(self, name, genre, cat_type, currency, books_to_sell):
        """creates and adds a customer to the User customers list (LIST)"""
        self.customers.append(customer.Customer(name, genre, cat_type, currency, books_to_sell))
    
    def get_questboard(self):
        """returns User quest board list (LIST)"""
        return self._questboard
    
    def set_questboard(self, current, available, completed):
        """creates a questboard class object and sets it as user questboard"""
        self._questboard = questboard.QuestBoard(current, available, completed)
    


    
    

    




    
