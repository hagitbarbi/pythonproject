import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class ProductScrapCdata:
    def __init__(self, name, category="", price=0, currency=0, sku="", main_image="", additional_images=None,
                 description="", features=None, manufacturer=""):
        self.name = name
        self.category = category
        self.price = price
        self.currency = currency
        self.sku = sku
        self.main_image = main_image
        self.additional_images = additional_images if additional_images is not None else []
        self.description = description
        self.features = features if features is not None else []
        self.manufacturer = manufacturer


def login_function(login_url, username, password):
    # Create a dictionary with the user's credentials
    payload = {
        'username': username,
        'password': password
    }

    # Send a POST request to the login URL with the user's credentials
    response = requests.post(login_url, data=payload)

    # Check if the login was successful
    if response.status_code == 200:
        print("התחברת בהצלחה!")
        # You can add additional code here to perform actions after successful login
    else:
        print("התחברות נכשלה. נסה שוב.")

login_url = "https://cdata.com/" 
username = "admin" 
password = "admin"  
login_function(login_url, username, password)       

