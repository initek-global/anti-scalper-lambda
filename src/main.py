
## Load selectors

# with open(PATH + "selectors.json", "r") as f:
#     saved = json.load(f)

# try:
#     public_selectors = requests.get(
#         "https://raw.githubusercontent.com/initek-global/Anti-Scalp/main/selectors.json"
#     ).json()
#     if os.path.exists(PATH + "selectors.json"):
#         with open(PATH + "selectors.json", "r") as f:
#             own_selectors = json.load(f)

#         for name in public_selectors:
#             own_selectors[name] = public_selectors[name]

#         with open(PATH + "selectors.json", "w") as f:
#             json.dump(own_selectors, f, indent=4)
# except:
#     with open(PATH + "selectors.json", "w") as f:
#         json.dump(saved, f, indent=4)


# ## Write chromedriver for selenium  (if not already done)
# def chromedriver():
#     if os.path.exists(PATH + "chromedriver.exe"):
#         return

#     with open(PATH + "chromedriver.exe", "wb") as f:
#         f.write(requests.get("https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_win32.zip").content)

    
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path # this will get you the path variable
import time
import tldextract  
import json
from aws_lambda_powertools import Logger

logger = Logger()

service_object = Service(binary_path)
driver = webdriver.Chrome(service=service_object)

# deprecated but works in older selenium versions
# driver = webdriver.Chrome(executable_path=binary_path)
list_of_urls = ["https://www.amazon.com/dp/B09DTK1JG9"]

for url in list_of_urls:
    driver.get(url)

    time.sleep(5)

    ## load selectors from json file
    with open("selectors.json","r") as selectors_file:
        selectors = json.load(selectors_file)

    ## get shop name
    shop = tldextract.extract(driver.current_url).domain
    logger.info("Shop: This is the shop {shop}")

    ## get selector
    driver.fin

    # https://www.geeksforgeeks.org/find_element_by_xpath-driver-method-selenium-python/
    driver.find_element_by_css_selector(selector)



    selector = selectors[shop]["buyable"]

    element = driver.find_element_by_css_selector(selector)
    if element is not None:
        return True
    else:
        return False
