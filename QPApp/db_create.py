from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3

conn = sqlite3.connect('pdf_links.db')
cursor = conn.cursor()

subject_name = ""

driver = webdriver.Chrome()
driver.get("https://libportal.manipal.edu/MIT/Question%20Paper.aspx")

conn.execute('''CREATE TABLE IF NOT EXISTS PDF_LINKS (ID INTEGER PRIMARY KEY AUTOINCREMENT, LINK TEXT)''')
conn.commit()


def traverse():
    web_table = {}
    tbody = driver.find_element(By.ID, 'ctl00_ctl00_chmain_MITContent_FileGridCS_gvFiles').find_element(By.TAG_NAME,
                                                                                                        'tbody')
    for ele in tbody.find_elements(By.TAG_NAME, 'tr'):
        try:
            link = ele.find_element(By.TAG_NAME, 'td').find_element(By.TAG_NAME, 'a')
            web_table[link.get_attribute('id')] = link.text
        except Exception:
            pass

    for ele_id in web_table:
        if '..' in web_table[ele_id]:
            pass
        elif len(web_table[ele_id]) == 0:
            dummyElement = driver.find_element(By.ID, ele_id)
            trueElement = dummyElement.find_element(By.XPATH, '..').find_element(By.CSS_SELECTOR, "a[target='_blank']")
            if subject_name.lower() in trueElement.text.lower():
                print("Found file:", trueElement.get_attribute('href'))
                conn.execute('''INSERT INTO PDF_LINKS (LINK) VALUES (?)''', (trueElement.get_attribute('href'),))
                conn.commit()

            else:
                continue
        else:

            if any(year in web_table[ele_id] for year in ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']):
                continue
            else:
                driver.find_element(By.ID, ele_id).click()
                traverse()
                driver.back()


traverse()