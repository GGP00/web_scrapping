# web_scrapping
Educational practical case oriented to learn to identify the relevant data for an analytical project and to use data extraction (web scrapping) tools. 

## Entorno:

git clone https://github.com/GGP00/web_scrapping.git
directorio local repo > pip install -r requirements.txt

 Para acceder al contenido dinámico de la tabla primero hay que descargar el html en local y después screapearlo como otra página cualquiera. Para ello  hay que tener instalado el navegador Firefox y haber instalado el requirements.txt y seguir los siguientes pasos:

    1.- brew install geckodriver (en MAC OS)
    2.- terminal> which geckodriver
    3.- Copiar el path y pegarlo en el parámetro "executable_path"

## Scrapping:

python src/scrapper.py
