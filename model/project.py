#------------------------------------------------------------------------------
#qa:
#description: Структура объекта "Проект" (дз 25)
#------------------------------------------------------------------------------


class Project:
    def __init__(self, id=None, name=None, status=None, inherit_global=None, view_state=None, description=None):
        self.id = id # Primary
        self.name = name # обязательное поле (UNI)
        self.status = status # Optional
        #enabled # появляется после создания, Optional
        #access_min # из БД, Optional
        #file_path # из БД, Optional
        self.inherit_global = inherit_global # Optional
        self.view_state = view_state # Optional
        self.description = description # Optional
        #category_id # из БД, Optional
