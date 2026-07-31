#------------------------------------------------------------------------------
#qa:
#description: Тесты создания объекта "Проект" (дз 25)
#------------------------------------------------------------------------------

from model.project import Project

def test_create_project(app):
    app.session.login(username="administrator", password="root") # почему не запускается сам???
    project= Project(name="Проект Mantis", status="в разработке", inherit_global="Включен",
                               view_state="Публичный", description="дз 25")
    app.project.create_project(project)