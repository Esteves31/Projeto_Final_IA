import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def esperar(tempo:int):
    time.sleep(tempo)

with open('arxiv/initial_links.txt', 'r') as file:
    with open('arxiv/links_years_final.txt', 'w') as file_links:
        for url in file.readlines():
            driver = webdriver.Chrome()
            driver.get(url)

            esperar(10)

            qtnd_articles = driver.find_element(By.CLASS_NAME, 'paging')
            qtnd_articles = qtnd_articles.find_elements(By.TAG_NAME, 'a')

            qtnd_articles = qtnd_articles[-1].text

            qtnd_articles = qtnd_articles.split('-')
            qtnd_articles = qtnd_articles[-1]

            print(qtnd_articles)

            i = 0

            for j in range(0, int(qtnd_articles), 2000):
                url_new = url.replace('skip=0', f'skip={j}')
                file_links.write(url_new)

            driver.quit()


