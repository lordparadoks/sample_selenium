from selenium import webdriver


class Browser:
    def __init__(self):
        self.driver = None
        self.profile = None

    def start(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference('browser.usedOnWindows10.introURL', '')
        self.profile.set_preference('startup.homepage_welcome_url.additional', '')
        self.driver = webdriver.Firefox(firefox_profile=self.profile)
        self.driver.maximize_window()
        return self.driver

    def stop(self):
        self.driver.close()
