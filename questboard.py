class QuestBoard:
    def __init__(self, current_quests, available_quests, completed_quests):
        self._current_quests = current_quests
        self._available_quests = available_quests
        self._completed_quests = completed_quests

    def get_current_quests(self):
        """returns current_quests (DICT)"""
        return self._current_quests

    def get_available_quests(self):
        """returns available_quests (DICT)"""
        return self._available_quests
    
    def get_completed_quests(self):
        """returns completed quests (DICT)"""
        return self._completed_quests
    



    