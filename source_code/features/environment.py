from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit()

def before_scenario(context, scenario):
    # only  navigate to the homepage, do not create a new driver
    if not hasattr(context, 'driver') or context.driver is None:
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()