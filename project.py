import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

Options=Options()
Options.add_experimental_option("detach",True)  # משאיר את הבראוזר פתוח  



driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                         options=Options)

driver.get("http://www.neuralnine.com/")
driver.maximize_window()

links=driver.find_elements("xpath","//a[@href]")
for link in links:
        if "Books" in link.get_attribute("innerHTML"):
                link.click()
                break
        
book_links=driver.find_elements("xpath",
                                "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(.,'7 IN 1')]]][count(.//a)=2]//a")

book_links[0].click()

driver.switch_to.window(driver.window_handles[1])

time.sleep(3)

buttons=driver.find_elements("xpath", "//a[.//span[text()[contains(., 'Paperback')]]]//span[text()[contains(.,'$')]]")

for button in buttons:
        print(button.get_attribute("innerHTML").replace("&nbsp;"," "))
