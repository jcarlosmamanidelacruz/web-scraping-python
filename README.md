# Web Scraping con Python

El proyecto se centra en la creación de un sistema de extracción de datos a partir de información pública disponible en el sitio web de la Universidad Nacional de San Marcos. El objetivo principal es recopilar datos relevantes sobre los postulantes y las carreras universitarias ofrecidas por esta institución. Para lograrlo, se emplea técnicas de web scraping utilizando Python, junto con el almacenamiento de datos en una base de datos PostgreSQL y la generación de informes interactivos con Power BI. A continuación, se detallan los pasos seguidos para llevar a cabo este proyecto.

**1. Análisis del Sitio Web:**

Comencé analizando la estructura del sitio web objetivo para entender cómo estaban organizados los datos y las páginas relevantes que contenían la información que necesitaba.

**2. Selección de Herramientas:**

Para desarrollar este proyecto, utilicé las siguientes herramientas:

- Python: Principalmente para el desarrollo del web scraping y la manipulación de datos.
- PostgreSQL: Para almacenar los datos extraídos del sitio web y facilitar su gestión.
- Power BI: Para crear informes interactivos y visualizaciones atractivas basadas en los datos almacenados en PostgreSQL.

**3. Desarrollo del Web Scraping:**

Escribí código en Python utilizando las bibliotecas BeautifulSoup y Requests para extraer la información relevante del sitio web de la Universidad Nacional de San Marcos.

**4. Almacenamiento de los Datos:**

Los datos extraídos se almacenaron en una base de datos PostgreSQL. 

**5. Limpieza y Transformación de Datos:**

Una vez que los datos fueron extraídos y almacenados, se realizó un proceso de limpieza y transformación para asegurar la coherencia y la calidad de los datos. Esto incluyó la eliminación de duplicados, la corrección de errores y la estandarización de formatos.

**6. Desarrollo de Informes con Power BI:**

Utilicé Power BI para crear informes y visualizaciones interactivas basadas en los datos almacenados en PostgreSQL. Esto permitió analizar fácilmente los datos extraídos y obtener insights valiosos a partir de ellos.

# Lista de URLs analizadas

En esta sección, se presenta la lista de URLs principales utilizadas como punto de partida para el análisis y desarrollo del proyecto. Cada una de estas URLs contiene enlaces a páginas internas que también fueron analizadas.

- Examen de admisión 2023-1
https://admision.unmsm.edu.pe/Res_20231_Area_A/

	Esta URL principal contiene enlaces a páginas de categorías, tales como:
	
	- 	https://admision.unmsm.edu.pe/Res_20231_Area_A/A.html
	- 	https://admision.unmsm.edu.pe/Res_20231_Area_A/A/011/0.html

- Examen de admisión 2023-2
https://admision.unmsm.edu.pe/WebsiteExa_20232/

	Esta URL principal contiene enlaces a páginas de categorías, tales como:
	
	- 	https://admision.unmsm.edu.pe/WebsiteExa_20232/A.html
	- 	https://admision.unmsm.edu.pe/WebsiteExa_20232/A/011/0.html
	
- Examen de admisión 2024-1
https://admision.unmsm.edu.pe/Website20241/

	Esta URL principal contiene enlaces a páginas de categorías, tales como:
	
	- 	https://admision.unmsm.edu.pe/Website20241/A.html
	- 	https://admision.unmsm.edu.pe/Website20241/A/011/0.html
	
- Examen de admisión 2024-2
https://admision.unmsm.edu.pe/Website20242/

	Esta URL principal contiene enlaces a páginas de categorías, tales como:
	
	- 	https://admision.unmsm.edu.pe/Website20242/A.html
	- 	https://admision.unmsm.edu.pe/Website20242/A/011/0.html
	
### Capturas de Pantalla de las Páginas Analizadas - Examen de admisión 2024-2

1. Captura de la Página Principal:

[![pagina-principal.png](https://i.postimg.cc/nhgC5Wp6/pagina-principal.png)](https://postimg.cc/5X54QnH3)
2. Captura de la Página 2:

[![pagina-2-escuelas-profesionales.png](https://i.postimg.cc/BQtZ0CYs/pagina-2-escuelas-profesionales.png)](https://postimg.cc/TpMvjnvH)
3. Captura de la Página 3:

[![pagina-3-resultados.png](https://i.postimg.cc/qRVRjC4n/pagina-3-resultados.png)](https://postimg.cc/GBKdptBh)
