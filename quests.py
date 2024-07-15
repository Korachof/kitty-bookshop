class Quest:
    def __init__(self, title, quest_type, monetary_reward, other_reward, description):
        self._title = title
        self._quest_type = quest_type
        self._monetary_reward = monetary_reward
        self._other_reward = other_reward
        self._description = description

    def get_title(self):
        """returns the Quest title (STR)"""
        return self._title
    
    def get_quest_type(self):
        """returns the Quest type (STR)"""
        return self._quest_type
    
    def get_monetary_reward(self):
        """returns the Quest monetary reward (INT)"""
        return self._monetary_reward
    
    def get_other_reward(self):
        """returns the Quest other reward (if there is one) (either cat OBJ, item OBJ, or NONE)"""
        return self._other_reward
    
    def get_description(self):
        """returns the Quest description (STR)"""
        return self._description
    


