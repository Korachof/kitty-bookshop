class Customer:
    def __init__(self, name, relationship_level, relationship_points, fave_genre,
                 fave_cat_type, fave_snack, currency_level, price_tolerance, books_to_sell):
        self._name = name
        self._relationship_level = relationship_level
        self._relationship_points = relationship_points
        self._fave_genre = fave_genre
        self._fave_cat_type = fave_cat_type
        self._fave_snack = fave_snack
        self._currency_level = currency_level
        self._price_tolerance = price_tolerance
        self._books_to_sell = books_to_sell

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
    
    def get_fave_cat_type(self):
        """returns Customer fave_cat_type (STR)"""
        return self._fave_cat_type
    
    def get_fave_snack(self):
        """returns Customer fave snack (STR)"""
        return self._fave_snack
    
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



