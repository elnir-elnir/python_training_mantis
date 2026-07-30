#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

from selenium import webdriver

from fixture.session import SessionHelper



class Application:

    # Введена переменная browser для определения типа веб-драйвера в зависимости от браузера (урок 5-8)
    # Удалено ожидание self.wd.implicitly_wait(10)
    # driver is initialized when the fixture is created
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # helper gets a reference to an object of the Application class
        self.session = SessionHelper(self)
        self.base_url = base_url


    # Checks that the WebDriver can interact with the current browser window    #
    # Used for safe execution of operations when the browser may be closed
    def is_valid(self):
        try:
            # Requesting the URL of the currently open page
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        # Функция изменена в связи с добавлением hook в рамках урока 5-8
        #wd.get("http://localhost/addressbook/")
        wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()
