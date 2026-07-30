#------------------------------------------------------------------------------
#qa:
#description: Вспомогательные методы для класса "Project" (дз 25)
#------------------------------------------------------------------------------


from selenium.webdriver.common.by import By

from model.project import Project


class GroupHelper:

    def __init__(self, app):
        self.app = app


    def open_control_page(self):
        wd = self.app.wd


    def open_projects_page(self):
        wd = self.app.wd


    def create_project(self):
        wd = self.app.wd


    def fill_project_form(self):
        wd = self.app.wd


    def edit_project(self):
        wd = self.app.wd


    def delete_project(self):
        wd = self.app.wd
