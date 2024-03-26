# Web Scraping con Python

El proyecto se centra en la creación de un sistema de extracción de datos a partir de información pública disponible en el sitio web de la Universidad Nacional de San Marcos. El objetivo principal es recopilar datos relevantes sobre los postulantes y las carreras universitarias ofrecidas por esta institución. Para lograrlo, se emplea técnicas de web scraping utilizando Python, junto con el almacenamiento de datos en una base de datos PostgreSQL y la generación de informes interactivos con Power BI.

[![Arquitectura-de-Flujo-de-Datps-Web-Scraping-drawio.png](https://i.postimg.cc/26x6WBQ7/Arquitectura-de-Flujo-de-Datps-Web-Scraping-drawio.png)](https://postimg.cc/WFhTLzfd)

A continuación, se detallan los pasos seguidos para llevar a cabo este proyecto.

#### 1. Análisis del Sitio Web:

Comencé analizando la estructura del sitio web objetivo para entender cómo estaban organizados los datos y las páginas relevantes que contenían la información que necesitaba.

#### 2. Selección de Herramientas:

Para desarrollar este proyecto, utilicé las siguientes herramientas:

- Python: Principalmente para el desarrollo del web scraping y la manipulación de datos.
- PostgreSQL: Para almacenar los datos extraídos del sitio web y facilitar su gestión.
- Power BI: Para crear informes interactivos y visualizaciones atractivas basadas en los datos almacenados en PostgreSQL.

#### 3. Desarrollo del Web Scraping:

Escribí código en Python utilizando las bibliotecas BeautifulSoup y Requests para extraer la información relevante del sitio web de la Universidad Nacional de San Marcos.

#### 4. Almacenamiento de los Datos:

Los datos extraídos se almacenaron en una base de datos PostgreSQL. 

#### 5. Limpieza y Transformación de Datos:

Una vez que los datos fueron extraídos y almacenados, se realizó un proceso de limpieza y transformación para asegurar la coherencia y la calidad de los datos. Esto incluyó la eliminación de duplicados, la corrección de errores y la estandarización de formatos.

#### 6. Desarrollo de Informes con Power BI:

Utilicé Power BI para crear informes y visualizaciones interactivas basadas en los datos almacenados en PostgreSQL. Esto permitió analizar fácilmente los datos extraídos y obtener insights valiosos a partir de ellos.

# Lista de URLs analizadas

En esta sección, se presenta la lista de URLs principales utilizadas como punto de partida para el análisis y desarrollo del proyecto. Cada una de estas URLs contiene enlaces a páginas internas que también fueron analizadas.

- Examen de admisión 2023-1<br>
https://admision.unmsm.edu.pe/Res_20231_Area_A/

	Esta URL principal contiene enlaces a páginas de categorías, tales como:
	
	- 	https://admision.unmsm.edu.pe/Res_20231_Area_A/A.html
	- 	https://admision.unmsm.edu.pe/Res_20231_Area_A/A/011/0.html

- Examen de admisión 2023-2<br>
https://admision.unmsm.edu.pe/WebsiteExa_20232/

	Esta URL principal contiene enlaces a páginas de categorías, tales como:
	
	- 	https://admision.unmsm.edu.pe/WebsiteExa_20232/A.html
	- 	https://admision.unmsm.edu.pe/WebsiteExa_20232/A/011/0.html
	
- Examen de admisión 2024-1<br>
https://admision.unmsm.edu.pe/Website20241/

	Esta URL principal contiene enlaces a páginas de categorías, tales como:
	
	- 	https://admision.unmsm.edu.pe/Website20241/A.html
	- 	https://admision.unmsm.edu.pe/Website20241/A/011/0.html
	
- Examen de admisión 2024-2<br><br>
https://admision.unmsm.edu.pe/Website20242/

	Esta URL principal contiene enlaces a páginas de categorías, tales como:
	
	- 	https://admision.unmsm.edu.pe/Website20242/A.html
	- 	https://admision.unmsm.edu.pe/Website20242/A/011/0.html
	
### Capturas de Pantalla de las Páginas Analizadas - Examen de admisión 2024-2

##### 1. Captura de la Página Principal:

[![pagina-principal.png](https://i.postimg.cc/nhgC5Wp6/pagina-principal.png)](https://postimg.cc/5X54QnH3)
##### 2. Captura de la Página 2:

[![pagina-2-escuelas-profesionales.png](https://i.postimg.cc/BQtZ0CYs/pagina-2-escuelas-profesionales.png)](https://postimg.cc/TpMvjnvH)
##### 3. Captura de la Página 3:

[![pagina-3-resultados.png](https://i.postimg.cc/qRVRjC4n/pagina-3-resultados.png)](https://postimg.cc/GBKdptBh)

## Estructura del Proyecto:

sql/: Carpeta que contiene los archivos SQL.

- create_tables.sql: Script para crear la tabla en la base de datos.

pbi/: Esta carpeta contiene el archivo de Power BI con los informes elaborados para el análisis de la información extraída.

- PBI_postulantes_USM.pbi: Informe desarrollado en Powe BI.
  
README.md: Este archivo, que proporciona una guía sobre el proyecto y su estructura.


[![estructura-proyecto.png](https://i.postimg.cc/nhMkWRyD/estructura-proyecto.png)](https://postimg.cc/k23K6cXJ)

## Instrucciones para Configurar el Entorno del Proyecto

1. Clona este repositorio en tu máquina local.
2. Abre tu cliente de PostgreSQL o cualquier otro cliente de SQL que prefieras.
3. Utiliza el cliente para cargar el script create_tables.sql y crear las tablas en la base de datos. Por lo general, puedes abrir el archivo en el cliente y ejecutarlo directamente.
4. Una vez creadas las tablas, carga el archivo querys.sql en tu cliente de SQL.
5. Activa el entorno viirtual del proyecto.
6. Instala las dependencias desde el archivo **requirements.txt**
7. Ejecuta el archivo python **Scraping_usm.py**
8. Abre el archivo de Power BI proporcionado en la carpeta **"pbi"** del repositorio. Puedes abrirlo con Power BI Desktop, que puedes descargar gratuitamente desde el sitio web oficial de Microsoft. Una vez abierto, carga los datos desde la base de datos PostgreSQL para visualizar los informes y análisis preparados.

## Instrucciones de activación del entorno virtual

Para activar el entorno virtual en su sistema, siga estos pasos:

#### 1. Navegue hasta la carpeta del proyecto utilizando la terminal o el símbolo del sistema.

		web-scraping-python/entonovirtual/Scripts

#### 2. Dentro de la carpeta `Scripts`, ejecute el siguiente comando:

		activate

#### 3. Instrucciones para instalar dependencias:

Para instalar las dependencias del proyecto, siga estos pasos:

1. Asegúrese de haber activado el entorno virtual como se describe anteriormente.
2. Ejecute el siguiente comando en la terminal:

		pip install -r requirements.txt

## Tabla para almacenar los datos
[![Table.png](https://i.postimg.cc/Wb1C2nR2/Table.png)](https://postimg.cc/hhNpsVPw)

## Informe PBI desarrollado

[![pbi1.png](https://i.postimg.cc/d0sWJ2S2/pbi1.png)](https://postimg.cc/yDGhPZKx)

[![pbi2.png](https://i.postimg.cc/Sxrr1XNJ/pbi2.png)](https://postimg.cc/211hVSWD)

## Enlace del informe publicado en la web

<a href="https://app.powerbi.com/view?r=eyJrIjoiNzJmNzhmMDMtNjVhYy00M2E4LWI5YWMtYmY5NzVkN2E1MDk4IiwidCI6ImFlNWFkYzNmLWI2MDUtNGRjMy04NmM3LWM5NDgzNjE2MDk3MiJ9" target="_blank"> Ver Informe Publicado en la Web</a>
