from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

# Connect to the website
driver = webdriver.Chrome()
driver.get("https://webschedule.smccd.edu/list_classes_default_search.php?term_code=202308&keywords=Computer+science&college_code%5B%5D=2")

# Find all rows of tables
tablerows = driver.find_elements(By.XPATH, "//tbody/tr")
data = []

# For each row, find the status, crn, coursetitle, professor
for tablerow in tablerows:
    status = tablerow.find_element(By.CLASS_NAME, "text-danger")
    CRN = tablerow.find_element(By.XPATH, ".//td[@class='hidden-xs'][3]")
    courseTitle = tablerow.find_element(By.XPATH, ".//td[4]")
    professor = tablerow.find_element(By.XPATH, ".//td[@class='hidden-xs'][6]")

    data_item = {
        'Status': status.text,
        'CRN': CRN.text,
        'Course Title': courseTitle.text.split("\n")[0],
        'Professor': professor.text
    }

    data.append(data_item)

driver.quit()
df = pd.DataFrame(data)
df.to_csv("Data.csv", mode='w')


