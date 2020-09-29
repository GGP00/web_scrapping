# web_scrapping
Caso práctico educativo para minar datos de páginas web. Máster Data Science - UOC.

## Integrantes del equipo

* Guzmán Gómez Pérez: ggomezper@uoc.edu.

## Datos:

Datos sobre la mortalidad, recuperación y contagio en todos los países del mundo descargados de la [página web de Google](https://www.google.com/covid19-map/?hl=es).

## Legalidad:

Se puede observar que no existe restricción alguna para el  scrappeado en el recurso "covid19-map" mediante un CTR-F en el archivo [robots.txt de Google](https://www.google.com/robots.txt).

## Entorno:
```
git clone https://github.com/GGP00/web_scrapping.git
directorio local repo > pip install -r requirements.txt
```
Para acceder al contenido dinámico de la tabla primero hay que descargar el html en local y después screapearlo como otra página cualquiera. Para ello  hay que tener instalado el navegador Firefox y haber instalado el requirements.txt y seguir los siguientes pasos:

```
    1.- brew install geckodriver (en MAC OS)
    2.- terminal> which geckodriver
    3.- Copiar el path y pegarlo en el parámetro "executable_path"
```

## Scrapping:

```python src/scrapper.py```

## Licencia:

Apache 2.0
