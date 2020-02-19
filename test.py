



my_url = 'https://datastudio.google.com/reporting/188wX_8wKVwiG8VBhAGheljpcqU18Dov1/page/bCkF'


from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import csv
import schedule

from datetime import datetime






class medidordigital():

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.url = 'https://datastudio.google.com/reporting/188wX_8wKVwiG8VBhAGheljpcqU18Dov1/page/bCkF'
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


    def fetch_data(self):
        url = self.url
        self.driver.get(url)
        data_collected = []
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'table'))
            )
            pageSource = self.driver.page_source

            bsobj = BeautifulSoup(pageSource, features="html.parser")
            for i in bsobj.find("div", {"class": "word-wrap"}, text="2019.0071").next_siblings:
                data_collected.append(i.string)
            print(data_collected)
            return data_collected

        except:
            print("deu merda")

        finally:
            self.driver.quit()


    def save_data_csv(self,data):
        data_hora = datetime.now().strftime('%d/%m/%y %H:%M')
        with open('data.csv', mode='a', encoding='utf-8', newline='' ) as csv_file:
            print("passei auqi")
            fieldnames = ['data',  'dia', 'horas', 'tamanho' , 'medicao' , 'tamanho_cx' , 'distancia']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
          # writer.writeheader()
            writer.writerow({'data': data_hora, 'dia': data[0], 'horas': data[1], 'tamanho': data[2], 'medicao': data[3], 'tamanho_cx': data[4], 'distancia': data[5]})




medidor = medidordigital()
data_collected =  medidor.fetch_data()
if data_collected:
    medidor.save_data_csv(data_collected)





