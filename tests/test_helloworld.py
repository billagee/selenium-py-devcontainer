import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestWebApp:
    def test_helloworld(self):
        options = webdriver.ChromeOptions()

        # Instantiate remote session
        se_grid_host = os.environ.get('GRIDHOST')
        se_grid_port = os.environ.get('GRIDPORT')
        grid_url = "http://{0}:{1}/wd/hub".format(se_grid_host, se_grid_port)
        driver = webdriver.Remote(
            #desired_capabilities=self.desired_capabilities,
            options=options,
            command_executor=grid_url)

        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()
        driver.quit()
