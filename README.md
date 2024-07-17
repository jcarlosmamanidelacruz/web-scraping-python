# Web Scraping con Python

<img src="https://i.postimg.cc/qRpQFpMP/web-Scraping-python.png" alt="">

El web scraping es una técnica poderosa utilizada para extraer datos de sitios web de manera automatizada. En este proyecto, se emplea el web scraping para recopilar información relevante del sitio web de la Universidad Nacional de San Marcos. Esto incluye datos sobre postulantes y las carreras universitarias ofrecidas por esta prestigiosa institución educativa.

## Beneficios del Web Scraping

El uso de técnicas de web scraping permite acceder y analizar datos que de otro modo serían difíciles de obtener manualmente. Al automatizar el proceso de extracción, podemos obtener datos en tiempo real, mantener actualizada la información y facilitar su análisis y visualización.

## Objetivos del Proyecto

- Extraer datos públicos de la Universidad Nacional de San Marcos utilizando técnicas de web scraping.
- Almacenar los datos extraídos en una base de datos PostgreSQL para facilitar su gestión y análisis.
- Crear informes interactivos con Power BI para visualizar y analizar los datos de manera efectiva.

<img src="https://i.postimg.cc/mgfd9vFF/Web-Scraping.png" alt="">

A continuación, se detallan los pasos seguidos para llevar a cabo este proyecto.

#### 1. Análisis del Sitio Web:

Inicié el proyecto con un exhaustivo análisis de la estructura del sitio web objetivo. Este paso fue fundamental para comprender la organización de los datos y identificar las páginas clave que contienen la información necesaria para el scraping. Este proceso incluyó explorar la jerarquía del sitio, revisar el diseño de las páginas y estudiar las rutas de acceso a los datos requeridos.

#### 2. Selección de Herramientas:

Para desarrollar este proyecto, utilicé las siguientes herramientas:

- **Python:** Principalmente para el desarrollo del web scraping y la manipulación de datos.
- **PostgreSQL:** Se empleó para almacenar los datos extraídos del sitio web, proporcionando una gestión eficiente de la base de datos.
- **Power BI:** Se utilizó para crear informes interactivos y visualizaciones atractivas basadas en los datos almacenados en PostgreSQL, facilitando así el análisis de los datos obtenidos.

#### 3. Desarrollo del Web Scraping:

Desarrollé el código en Python utilizando las bibliotecas BeautifulSoup y Requests para extraer de manera eficiente la información relevante del sitio web de la Universidad Nacional de San Marcos.

#### 4. Almacenamiento de los Datos:

Los datos extraídos fueron almacenados de manera eficiente en una base de datos PostgreSQL.

#### 5. Limpieza y Transformación de Datos:

Para el análisis y visualización de los datos, se utilizó Power BI. Esta herramienta permitió la creación de informes interactivos y visualizaciones basadas en los datos almacenados en PostgreSQL, facilitando la generación de valiosos insights a partir de los datos extraídos.

#### 6. Desarrollo de Informes con Power BI:

Utilicé Power BI para crear informes y visualizaciones interactivas basadas en los datos almacenados en PostgreSQL. Esto permitió analizar fácilmente los datos extraídos y obtener insights valiosos a partir de ellos.

# Ejemplo de Fragmento de Código

<img src="https://i.postimg.cc/k4MVpvBy/codigo-python.png" alt="">

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

<img src="https://i.postimg.cc/nhgC5Wp6/pagina-principal.png" alt="">

##### 2. Captura de la Página 2:

<img src="https://i.postimg.cc/BQtZ0CYs/pagina-2-escuelas-profesionales.png" alt="">

##### 3. Captura de la Página 3:

<img src="https://i.postimg.cc/qRVRjC4n/pagina-3-resultados.png" alt="">

## Estructura del Proyecto:

sql/: Carpeta que contiene los archivos SQL.

- create_tables.sql: Script para crear la tabla en la base de datos.

pbi/: Esta carpeta contiene el archivo de Power BI con los informes elaborados para el análisis de la información extraída.

- PBI_postulantes_USM.pbi: Informe desarrollado en Powe BI.
  
README.md: Este archivo, que proporciona una guía sobre el proyecto y su estructura.

<img src="https://i.postimg.cc/nhMkWRyD/estructura-proyecto.png" alt="">

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

<img src="https://i.postimg.cc/Wb1C2nR2/Table.png" alt="">

## Informe PBI desarrollado

<img src="https://i.postimg.cc/d0sWJ2S2/pbi1.png" alt="">

<img src="https://i.postimg.cc/Sxrr1XNJ/pbi2.png" alt="">

## Enlace del informe publicado en la web

<a href="https://app.powerbi.com/view?r=eyJrIjoiNzJmNzhmMDMtNjVhYy00M2E4LWI5YWMtYmY5NzVkN2E1MDk4IiwidCI6ImFlNWFkYzNmLWI2MDUtNGRjMy04NmM3LWM5NDgzNjE2MDk3MiJ9" target="_blank"> Ver Informe Publicado en la Web</a>

