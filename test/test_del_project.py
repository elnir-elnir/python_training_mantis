#------------------------------------------------------------------------------
#qa:
#description: Тесты удаления объекта "Проект" (дз 25)
#------------------------------------------------------------------------------

import random

from model.project import Project


def test_del_project_via_project_list(app):
    app.session.login(username="administrator", password="root")

    if len(app.project.get_project_list()) == 0:

        project = Project(name="Проект MantisBT", status="в разработке", inherit_global="выключен",
                          view_state="публичный", description="дз 25")
        app.project.create_project(project)

    old_projects = app.project.get_project_list()
    print("old_projects: ", old_projects)

    project = random.choice(old_projects)

    app.project.delete_project_via_projects_page(project)

    new_projects = app.project.get_project_list()
    print("new_projects: ", new_projects)

    assert len(old_projects) - 1 == len(new_projects)

    old_projects.remove(project)
    print("new_old_projects: ", old_projects)

    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
