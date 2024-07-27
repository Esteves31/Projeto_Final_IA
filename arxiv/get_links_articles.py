import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def esperar(tempo:int):
    time.sleep(tempo)

with open('arxiv/links_years_final.txt', 'r') as file_links:
    with open('arxiv/links_articles_DS.txt', 'w') as file_articles:
        for link in file_links.readlines():
            driver = webdriver.Chrome()

            driver.get(link)

            esperar(5)

            div_articles = driver.find_element(By.ID, "articles")

            dts = div_articles.find_elements(By.TAG_NAME, "dt")
            dds = div_articles.find_elements(By.TAG_NAME, "dd")

            for dd, dt in zip(dds, dts):
                list_subjects = dd.find_element(By.CLASS_NAME, 'list-subjects')
                if('math.DS' in list_subjects.text):
                    links = dt.find_elements(By.TAG_NAME, 'a')
                    file_articles.write(links[1].get_attribute('href') + '\n')

            driver.quit()

