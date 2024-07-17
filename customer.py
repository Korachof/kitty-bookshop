from random import randrange


class Customer:
    def __init__(self, name: str, relationship_level: int, relationship_points: int, fave_genre: str, 
                 fave_cat_types: list, currency_level: int, price_tolerance: str, books_to_sell: list):
        self._name = name
        self._relationship_level = relationship_level
        self._relationship_points = relationship_points
        self._fave_genre = fave_genre
        self._fave_cat_types = fave_cat_types
        self._currency_level = currency_level
        self._price_tolerance = price_tolerance
        self._books_to_sell = books_to_sell
        self._customer_mode = 1             # 1 = buy, 2 = sell, 3 = cat time

    def get_name(self):
        """returns Customer name (STR)"""
        return self._name
    
    def get_relationship_level(self):
        """returns Customer relationship_level (INT)"""
        return self._relationship_level
    
    def get_relationship_points(self):
        """returns Customer relationship_points (INT)"""
        return self._relationship_points
    
    def get_fave_genre(self):
        """returns Customer fave genre (STR)"""
        return self._fave_genre
    
    def get_fave_cat_types(self):
        """returns Customer fave_cat_type (STR)"""
        return self._fave_cat_types
    
    def get_currency_level(self):
        """returns Customer currency_level (INT)"""
        return self._currency_level
    
    def get_price_tolerance(self):
        """returns Customer price_tolerance (STR)"""
        return self._price_tolerance
    
    def get_books_to_sell(self):
        """"returns Customer books_to_sell (LIST)"""
        return self._books_to_sell
    
    def add_book_to_sell(self, book: object):
        """adds a book to the books_to_sell list"""
        self._books_to_sell.append(book)

    def get_customer_mode(self):
        """returns current Customer customer_mode (INT)
        1: buy, 2: sell, 3: cat time"""
        return self._customer_mode
    
    def set_customer_mode(self):
        """changes the customer mode when they enter the store
        1: buy, 2: sell, 3: cat time"""
        mode = randrange(1, 101)
        if mode < 41:
            self._customer_mode = 1
        elif mode < 81:
            self._customer_mode = 3
        elif mode < 101:
            self._customer_mode = 2


class NamedCustomer(Customer):
     def __init__(self, name: str, relationship_level: int, relationship_points: int, fave_genre: str, 
                 fave_cat_types: list, currency_level: int, price_tolerance: str, books_to_sell: list):
        super().__init__(name, relationship_level, relationship_points, fave_genre, 
                 fave_cat_types, currency_level, price_tolerance, books_to_sell)




