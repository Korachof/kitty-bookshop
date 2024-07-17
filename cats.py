class Cat:
    def __init__(self, name: str, relationship_level: int, relationship_points: int, stats: dict, coat_color: str, coat_pattern: str, favorite_food: str, favorite_toy: str):
        self._name = name
        self._relationship_level = relationship_level
        self._relationship_points = relationship_points
        self._stats = stats  # Chungus Level, cuddliness Level, Playfulness Level, Butthead Level, Stamina Level 
        self._coat_color = coat_color
        self._coat_pattern = coat_pattern
        self._favorite_food = favorite_food
        self._favorite_toy = favorite_toy

    def get_name(self):
        """returns the Cat name"""
        return self._name
    
    def get_relationship_level(self):
        """returns the Cat relationship level"""
        return self._relationship_level


class RandomCat:
    pass


