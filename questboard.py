import quests


class QuestBoard:
    def __init__(self, current_quests, available_quests, completed_quests):
        # {quest_type: [quest1, quest2], quest_typ2: [quest3, quest4]}
        self._current_quests = current_quests
        self._available_quests = available_quests
        self._completed_quests = completed_quests

    def get_current_quests(self):
        """returns current_quests (DICT)"""
        return self._current_quests
    
    def add_current_quest(self, quest):
        """adds a quest obj to QuestBoard current_quests (DICT)"""
        self._current_quests[quest.get_quest_type()].append(quest)

    def get_available_quests(self):
        """returns available_quests (DICT)"""
        return self._available_quests
    
    def add_available_quest(self, quest):
        """adds a quest obj to QuestBoard available_quests (DICT)"""
        self._available_quests[quest.get_quest_type()].append(quest)
    
    def get_completed_quests(self):
        """returns completed quests (DICT)"""
        return self._completed_quests
    
    def add_completed_quest(self, quest):
        """adds a quest obj to Questboard completed_quests (DICT)"""
        self._completed_quests[quest.get_quest_type()].append(quest)




    