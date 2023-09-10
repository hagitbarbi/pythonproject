from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class ProductScrapCdata:
    def __init__(self, driver_path, website_url):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.website_url = website_url

    def login(self, username, password, login_url):
        try:
            # פתיחת הדפדפן וניווט לעמוד הכניסה
            self.driver.get(login_url)

            # מציאת שדות הקלט של שם המשתמש והסיסמה
            username_field = self.driver.find_element(By.NAME, "username")
            password_field = self.driver.find_element(By.NAME, "password")

            # הזנת שם משתמש וסיסמה
            username_field.send_keys(username)
            password_field.send_keys(password)

            # לחיצה על כפתור הכניסה
            login_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'התחברות')]")
            login_button.click()

            # אם הכניסה הצליחה, החזרת אובייקט Selenium WebDriver
            return self.driver

        except Exception as e:
            print(f"אירעה שגיאה בעת התחברות: {str(e)}")
            return None

    def close_browser(self):
        # סגירת הדפדפן בסיום
        self.driver.quit()

# השימוש במחלקה:
if __name__ == "__main__":
    driver_path = 'מסלול_ל_webdriver_chrome.exe'
    website_url = 'https://cdata.co.il'
    login_url = 'https://cdata.co.il/login'
    username = 'שם_משתמש'
    password = 'סיסמה_כאן'

    scraper = ProductScrapCdata(driver_path, website_url)
    driver = scraper.login(username, password, login_url)

    if driver:
      
        scraper.close_browser()
