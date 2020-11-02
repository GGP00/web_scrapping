from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import datetime
from pathlib import Path

data_folder = Path("../text_files/")

__status__= "DEV"
__version__= "1.0"
__license__= "Apache 2.0"


class Scrapper:
    '''
    Aplicación del scrapeado: Descarga el contenido en local de la URL pasada por parámetro y ejecuta el scrapping.
    '''

    def __init__(self,  url):
        self.browser = webdriver.Firefox(executable_path = "/usr/local/bin/geckodriver")
        self.browser.get(url)
        time.sleep(3) # Darle tiempo a que se cargue la página en local
        html = self.browser.page_source
        self.soup = BeautifulSoup(html, "lxml")
        self.df = pd.DataFrame()

    def scrap_COVID(self):
        table_body = self.soup.find('tbody', attrs={'class':'qEfTDe'})
        table_rows = table_body.findAll('tr', attrs={'class':'A5V3jc'})
        data = []
        for row in table_rows:
            r = []
            if row.next_sibling:
                for entry in row.next_sibling:
                    r.append(entry.text)
                data.append(r)   
        self.df = pd.DataFrame(data, columns =['Country','Positives','Pos.PerMillion','Recovered','Dead']) 
        self.browser.close()
        self.browser.quit() 

    def save_data(self):
        saving_path = f'data/'
        abs_path = Path(saving_path).resolve()
        self.df.to_csv(str(abs_path)+f'/COVID19_web_scrapping_data_{datetime.date.today()}.csv', header=True, sep=',', index=False, encoding='utf-8')
        print('Datos descargados con éxito:','\n',self.df.head(),'\n',f'Guardados en: {abs_path}') 


if __name__ == "__main__":
    scrpr = Scrapper(url="https://www.google.com/covid19-map/?hl=es")
    scrpr.scrap_COVID()
    scrpr.save_data()
