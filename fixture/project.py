
#------------------------------------------------------------------------------
#qa:
#description: Вспомогательные методы для класса "Project" (дз 25)
#------------------------------------------------------------------------------

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from model.project import Project



class ProjectHelper:

    def __init__(self, app):
        self.app = app


    def open_control_page(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, ".fa-gears").click()


    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Проекты").click()


    def create_project(self, project):
        wd = self.app.wd
        self.open_control_page()
        self.open_projects_page()
        wd.find_element(By.CSS_SELECTOR, ".widget-toolbox > .form-inline > .btn").click()
        self.fill_project_form(project)
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    # Переписать метод (с использованием change_field_value и change_visible_value)
    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element(By.ID, "project-name").click()
        wd.find_element(By.ID, "project-name").send_keys(name=project.name)
        wd.find_element(By.ID, "project-status").click()
        Select(wd.find_element(By.ID, "project-status")).select_by_visible_text(project.status)
        if project.inherit_global == "Выключен":
            wd.find_element(By.CSS_SELECTOR, ".lbl").click()
        Select(wd.find_element(By.ID, "project-view-state")).select_by_visible_text(project.view_state)
        wd.find_element(By.ID, "project-description").click()
        wd.find_element(By.ID, "project-description").send_keys(description=project.description)


    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("project_name", project.name)
        self.change_field_value("project_header", project.description)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)


    def change_visible_value(self, param_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, param_name).click()
            Select(wd.find_element(By.NAME, param_name)).select_by_visible_text(text)


    def select_project_by_id (self, project_id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, f'a[href*="project_id={project_id}"]').click()


    def go_to_edit_project_page_by_id(self, project_id):
        self.select_project_by_id(project_id)


    def delete_project(self, project):
        wd = self.app.wd
        self.go_to_edit_project_page_by_id(project)
        wd.wd.find_element(By.CSS_SELECTOR, 'button[formaction="manage_proj_delete.php"]').click()
