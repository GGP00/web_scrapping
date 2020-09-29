from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import datetime

__author__= "Guzmán Gómez Pérez"
__email__= "gmgomezper@uoc.edu"
__status__= "DEV"
__version__= "1.0"
__license__= "Apache 2.0"


class Scrapper:
    '''
    Para acceder al contenido dinámico de la tabla primero hay que descargar el html
    en local y después screapearlo como otra página cualquiera. Para ello:

    * Tener instalado el navegador Firefox y haber instalado el requirements.txt

    1.- brew install geckodriver (en MAC OS)
    2.- terminal> which geckodriver
    3.- Copiar el path y pegarlo en el parámetro "executable_path"
    '''

    def __init__(self,  url):
        browser = webdriver.Firefox(executable_path = "/usr/local/bin/geckodriver")
        browser.get(url)
        time.sleep(3) # Darle tiempo a que se cargue la página en local
        html = browser.page_source
        self.soup = BeautifulSoup(html, "lxml")
        self.df = pd.DataFrame()

    def scrap_COVID(self)
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
        browser.close()
        browser.quit() 

    def save_data(self):
        self.df.to_csv(f'../data/COVID19_web_scrapping_data_{datetime.date.today()}.csv', header=True, sep=',', index=False, encoding='utf-8')
        print('Datos descargados con éxito:','\n',self.df.head()) 


if __name__ == "__main__":
    scrpr = Scrapper(url="https://www.google.com/covid19-map/?hl=es")
    scrpr.scrap_COVID()
    scrpr.save_data()