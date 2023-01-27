import os

from selenium import webdriver


class Base:

    @staticmethod
    def web_browser():
        TEST_DIR = os.path.dirname(os.path.abspath(__file__))
        PROJ_DIR = os.path.dirname(TEST_DIR)
        CHROME_DRIVER = PROJ_DIR + '/browsers/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        browser = webdriver.Chrome(chrome_options=options, executable_path=CHROME_DRIVER)

        return browser