from selenium import webdriver


class WD:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1400,800")
        # Suppress bluetooth chrome error
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.wd = webdriver.Chrome(options=chrome_options)
