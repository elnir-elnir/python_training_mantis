#------------------------------------------------------------------------------
#qa:
#description: Тесты удаления объекта "Проект" (дз 25)
#------------------------------------------------------------------------------

from model.project import Project


def test_del_project(app):
    app.session.login(username="administrator", password="root")

    project = Project(name="Проект MantisBT", status="в разработке", inherit_global="выключен",
                      view_state="публичный", description="дз 25")
    app.project.create_project(project)

    old_projects = app.project.get_project_list()
    print("old_projects: ", old_projects)

    app.project.delete_project_via_projects_page(project)
    #app.project.delete_project_by_name(project.name)