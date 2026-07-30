#------------------------------------------------------------------------------
#qa:
#description: Структура объекта "Проект" (дз 25)
#------------------------------------------------------------------------------


class Project:
    def __init__(self, id=None, name=None, status=None, inherit_global=None, view_state=None, description=None):
        self.id = id
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.description = description
