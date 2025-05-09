from selenium import webdriver as wd


def screen(url):
    screenshoter = wd.Chrome()
    screenshoter.get(url)
    screenshoter.save_screenshot("web_screen.png")
    screenshoter.quit()
