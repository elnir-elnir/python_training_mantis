#------------------------------------------------------------------------------
#qa:
#description: Тесты создания объекта "Проект" (дз 25)
#------------------------------------------------------------------------------
import time

from model.project import Project

def test_create_project(app):
    app.session.login(username="administrator", password="root") # почему не запускается сам???

    old_projects = app.project.get_project_list()
    print("old_projects: ", old_projects)

    project= Project(name="Проект MantisBT", status="в разработке", inherit_global="включен",
                               view_state="публичный", description="дз 25")
    app.project.create_project(project)

    time.sleep(5)

    new_projects = app.project.get_project_list()
    print("new_projects: ", new_projects)

    assert len(old_projects) + 1 == len(new_projects)

    old_projects.append(project)
    print("new_old_projects: ", old_projects)

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
