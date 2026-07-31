import time

#------------------------------------------------------------------------------
#qa:
#description: Вспомогательные методы для класса "Project" (дз 25)
#------------------------------------------------------------------------------

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import re

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


    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_visible_value("status", project.status)
        if project.inherit_global == "включен":
            self.set_checkbox("inherit_global", enable=True)
        if project.inherit_global == "выключен":
            self.set_checkbox("inherit_global", enable=False)
        self.change_visible_value("view_state", project.view_state)
        self.change_field_value("description", project.description)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)


    # Метод для управления заданным чек-боксом, где enable: True — включить, False — выключить
    def set_checkbox(self, checkbox_name, enable=True):
        wd = self.app.wd
        checkbox = wd.find_element(By.NAME, checkbox_name)

        checkbox_id = checkbox.get_attribute("id")
        #label = wd.find_element(By.XPATH, f'//label[@for="{checkbox_id}"]') # это не сработало

        def checkbox_locator():
            try:
                label = wd.find_element(By.CSS_SELECTOR, f'label[for="{checkbox_id}"]')
                label.click()
            except:
                # Клик по родительскому td
                parent = checkbox.find_element(By.XPATH, "..")
                parent.click()

        if enable and not checkbox.is_selected():
            checkbox_locator()

        if not enable and checkbox.is_selected():
            checkbox_locator()



    def change_visible_value(self, param_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, param_name).click()
            Select(wd.find_element(By.NAME, param_name)).select_by_visible_text(text)


    def select_project_by_id (self, project_id):
        wd = self.app.wd
        #wd.find_element(By.CSS_SELECTOR, f'a[href*="project_id={project_id}"]').click()
        # xpath = f"(//table[@class='table table-striped table-bordered table-condensed table-hover'])[1]//a[contains(@href, 'project_id={project_id}')]"
        # link = wd.find_element(By.XPATH, xpath)
        # wd.execute_script("arguments[0].click();", link)
        xpath = f"//a[contains(@href,'manage_proj_edit_page.php?project_id={project_id}')]"
        wd.find_element(By.XPATH, xpath).click()


    def select_project_by_name(self, project_name):
        wd = self.app.wd

        #wd.find_element(By.XPATH, f"//a[text()='{project_name}']").click()
        # xpath=(//a[contains(text(),'Проект1')])[3] # что означает [3]? попробовать !!!!
        wd.find_element(By.LINK_TEXT, f"{project_name}").click()


    def go_to_edit_project_page_by_id(self, project_name):
        #self.select_project_by_id(project_id)
        self.select_project_by_name(project_name)


    def delete_project_via_projects_page(self, project):
        wd = self.app.wd
        self.open_control_page()
        self.open_projects_page()
        self.go_to_edit_project_page_by_id(project)
        wd.find_element(By.CSS_SELECTOR, 'button[formaction="manage_proj_delete.php"]').click()
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()


    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_control_page()
        self.open_projects_page()
        time.sleep(10)
        wd.find_element(By.XPATH, f"//tr[.//a[contains(text(), '{name}')]]").click()
        time.sleep(10)
        wd.find_element(By.CSS_SELECTOR, 'button[formaction="manage_proj_delete.php"]').click()
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()


    # Получаем ссылку с project_id для проекта по названию
    def get_link_on_project_id(self, project_name):
        wd = self.app.wd
        # Ищем ссылку по точному тексту
        link = wd.find_element(By.XPATH, f"//a[text()='{project_name}']")
        return link


    # Получаем id проекта из ссылки
    def get_project_id_by_link(self,link):
        href = link.get_attribute("href")
        match = re.search(r'project_id=(\d+)', href)
        project_id = int(match.group(1)) if match else None
        #print("id_from_app: ", project_id, "href: ", href)
        return project_id


    # Получаем id проекта по названию проекта
    def get_project_id_by_project_name(self, project_name):
        link = self.get_link_on_project_id(project_name)
        project_id = self.get_project_id_by_link(link)
        #print("id_from_app: ", project_id)
        return project_id


    def get_project_list(self):
        wd = self.app.wd
        self.open_control_page()
        self.open_projects_page()

        # Проверяем, что загрузилась страница "Проекты"
        current_url = wd.current_url
        print(f"Текущий URL: {current_url}")
        assert "manage_proj_page.php" in current_url, "Не на странице управления проектами"

        projects = []

        # Выбираем только таблицу "Проекты" (первая таблица с классом table)
        projects_table = wd.find_element(
            By.XPATH, "(//table[@class='table table-striped table-bordered table-condensed table-hover'])[1]")

        # Получаем строки только в первой таблице
        rows = projects_table.find_elements(By.XPATH, ".//tbody/tr")

        # Получаем ссылки с project_id только в первой таблице
        links = projects_table.find_elements(By.XPATH, ".//a[contains(@href, 'project_id=')]")

        for r in range(len(rows)):
            # Получаем все ячейки в строке
            cells = rows[r].find_elements(By.TAG_NAME, "td")

            # Получаем id из ссылки
            id = self.get_project_id_by_link(links[r])
            print("id: ", id)

            # Отладка: выводим в консоль информацию из каждой ячейки таблицы
            for c in range(len(cells)):
                print(f"cell[{c}]: '{cells[c].text}'")

            # Получаем значения конкретных параметров из ячеек по их индексу
            name = cells[0].text.strip()
            status = cells[1].text.strip()
            view_state = cells[3].text.strip()
            print("name:", name, "status:", status, "view_state:", view_state, "\n")

            project = Project(id=id, name=name, status=status, view_state=view_state)
            projects.append(project)
            print("projects: ", projects)

        return projects
