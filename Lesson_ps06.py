import requests
from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

url = ("https://tomsk.hh.ru/vacancies/programmist")
driver = webdriver.Firefox()
driver.get(url)
time.sleep(3)
vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-card--H8LvOiOGPll0jZvYpxIF")
parsed_data = []
for vacancy in vacancies:
    try:
        title  = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGcRW0YDmp3BHuNOP').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге {e}")
        continue


    parsed_data.append([title, company, salary, link])

driver.quit()

with open('hh.csv','w', newline='', encoding ='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии','Название компании', 'Зарплата', 'Ссылка'])
    writer.writerows(parsed_data)





# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# rows = soup.find_all("tr")
# data =[]
# for row in rows:
#     cols = row.find_all("td")
#     cleaned_cols = [col.text.strip() for col in cols]
#     data.append(cleaned_cols)
#
# print(data)

# data = [
#     ["100", "110", "120"],
#     ['400', '500', '600'],
#     ['150', '130', '140']
#     ]

# numbers =[]
# for row in data:
#     for text in row:
#         number = int(text)
#         numbers.append(number)
#
# print(numbers)

