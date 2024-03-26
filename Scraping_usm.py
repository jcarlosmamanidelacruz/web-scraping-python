# LIBRERIAS UTILIZADAS PARA EL PROYECTO
import requests  # Utilizado para realizar solicitudes HTTP y obtener el contenido de las páginas web.
from bs4 import BeautifulSoup  # Utilizado para analizar el contenido HTML de las páginas web y extraer datos.
import pandas as pd  # Utilizado para manejar y manipular datos en forma de tablas (DataFrames).
import psycopg2  # Utilizado para interactuar con la base de datos PostgreSQL.

# Conexión a la base de datos PostgreSQL utilizando psycopg2.
cn_basdat = psycopg2.connect(
    user='postgres',  # Nombre de usuario de PostgreSQL.
    password='acceso123',  # Contraseña de PostgreSQL.
    host='localhost',  # Host donde se encuentra la base de datos.
    port='5433',  # Puerto de la base de datos.
    database='postgres'  # Nombre de la base de datos.
)

# Lista de URL de inicio para el web scraping.
# Cada elemento de la lista contiene información sobre una URL de inicio,
# incluyendo la URL principal, el año de postulación, el número de proceso, y el ID de la tabla a extraer.
ls_start_url = [
    {
        "url_pad": "https://admision.unmsm.edu.pe/Res_20231_Area_A/",
        "ani_pos": 2023,
        "num_pos": "I",
        "id_tabla": "tabla"
    },
    {
        "url_pad": "https://admision.unmsm.edu.pe/WebsiteExa_20232/",
        "ani_pos": 2023,
        "num_pos": "II",
        "id_tabla": "tabla"
    },
    {
        "url_pad": "https://admision.unmsm.edu.pe/Website20241/",
        "ani_pos": 2024,
        "num_pos": "I",
        "id_tabla": "tabla"
    },
    {
        "url_pad": "https://admision.unmsm.edu.pe/Website20242/",
        "ani_pos": 2024,
        "num_pos": "II",
        "id_tabla": "tablaPostulantes"
    }
]

# Convertir la lista de URL de inicio en un DataFrame de pandas
df_start_url= pd.DataFrame(ls_start_url)

# Iterar sobre cada fila del DataFrame
for index, row in df_start_url.iterrows():
    url_pad = row['url_pad']  # URL de inicio
    ani_pos = row['ani_pos']  # Año de postulación
    num_pos = row['num_pos']  # Número de proceso
    ide_tab = row['id_tabla']  # ID de la tabla a extraer

    # Hacer una solicitud GET a la URL de inicio
    start_url = requests.get(url_pad)
    
    # Crear un objeto BeautifulSoup para analizar el contenido HTML de la página de inicio
    soup = BeautifulSoup(start_url.content, 'html.parser')

    modalidades_ingreso_dict_list = [] # Inicializar una lista para almacenar los datos de las modalidades de ingreso
    modalidades_ingresos = soup.find_all('td', attrs={"class":"text-center"}) # Encontrar todas las filas de la tabla que contienen la class text-center

    # Iterar sobre cada fila de la tabla de modalidades de ingreso
    for filas in modalidades_ingresos:
        fila_dict = {} # Inicializar un diccionario para almacenar los datos de cada fila
        modalida_ingreso = filas.text # Extraer el nombre de la modalidad de ingreso
        a_tag = filas.find('a') # Encontrar el enlace dentro de la fila
        modalida_ingreso_url= a_tag.get('href') # Extraer la URL del enlace
        # Agregar los datos al diccionario de la fila
        fila_dict['modalida_ingreso'] = modalida_ingreso 
        fila_dict['modalida_ingreso_url'] = modalida_ingreso_url
        fila_dict['url_destino'] = url_pad + modalida_ingreso_url
        # Agregar el diccionario de la fila a la lista de modalidades de ingreso
        modalidades_ingreso_dict_list.append(fila_dict)
    # Crear un DataFrame de pandas con los datos de las modalidades de ingreso
    df = pd.DataFrame(modalidades_ingreso_dict_list)

    # ESCUELAS PROFESIONALES
    escuelas_profesionales_dict_list = [] # Inicializar una lista para almacenar los datos de las escuelas profesionales

    # Iterar sobre cada URL de destino en el DataFrame
    for items in df["url_destino"]:
        # Tiempo de espera entre cada requerimiento. Nos ayuda a proteger nuestra IP.
        download_delay = 2
        r2 = requests.get(items) # Realizar una solicitud GET a la URL de destino
        soup2 = BeautifulSoup(r2.content, 'html.parser') # Analizar el contenido HTML de la página de destino
        escuelas_profesionales = soup2.find_all('td', attrs={"class":"text-center"}) # Encontrar todas las filas de la tabla que contienen la class text-center
        
        # Iterar sobre cada fila de la tabla de escuelas profesionales
        for filas2 in escuelas_profesionales:
            fila_dict2 = {} # Inicializar un diccionario para almacenar los datos de cada fila
            escuela_profesional = filas2.text # Extraer el nombre de la escuela profesional
            a_tag2 = filas2.find('a') # Encontrar el enlace dentro de la fila
            escuela_profesional_url= a_tag2.get('href') # Extraer la URL de la escuela profesional
            # Agregar los datos al diccionario de la fila
            fila_dict2['escuela_profesional'] = escuela_profesional
            fila_dict2['escuela_profesional_url'] = escuela_profesional_url
            fila_dict2['url_origen'] = items
            v_url_destino = url_pad + escuela_profesional_url # Construir la URL completa de destino
            v_url_destino = v_url_destino.replace('/./', '/')
            fila_dict2['url_destino'] = v_url_destino
            # Agregar el diccionario de la fila a la lista de escuelas profesionales
            escuelas_profesionales_dict_list.append(fila_dict2)
    # Crear un DataFrame de pandas con los datos de las escuelas profesionales
    df2 = pd.DataFrame(escuelas_profesionales_dict_list)

    # POSTULANTES
    
    # Crear una lista con las cabeceras del DataFrame
    cabeceras = ['url_origen', 'ani_pos', 'num_pos', 'CODIGO', 'APELLIDOS Y NOMBRES', 'ESCUELA PROFESIONAL (PRIMERA OPCION)', 'PUNTAJE', 'MERITO E.P', 'OBSERVACION', 'ESCUELA PROFESIONAL (SEGUNDA OPCION)']
    df_unificado = pd.DataFrame(columns= cabeceras) # Crear un DataFrame vacío con las cabeceras especificadas

    # Iterar sobre cada URL de destino en el DataFrame df2
    for items in df2["url_destino"]:
        # Definir un tiempo de espera entre cada requerimiento para proteger la IP
        download_delay = 2
        r3 = requests.get(items) # Realizar una solicitud GET a la URL de destino
        soup3 = BeautifulSoup(r3.content, 'html.parser') # Analizar el contenido HTML de la página de destino
        tabla = soup3.find('table', {'id': ide_tab}) # Encontrar la tabla por su id

        # Verificar si se encontró la tabla
        if tabla:
            filas = tabla.find_all('tr') # Encontrar todas las filas de datos en el cuerpo de la tabla
            datos = [] # Crear una lista para almacenar los datos
            
            # Iterar sobre cada fila y extraer los datos de cada celda
            for fila in filas:
                celdas = fila.find_all(['td']) # Encontrar todas las celdas en la fila
                datos_fila = [celda.get_text(strip=True) for celda in celdas] # Extraer el texto de cada celda y añadirlo a la lista de datos
                # Insertar datos adicionales al principio de la lista
                datos_fila.insert(0, items)
                datos_fila.insert(1, ani_pos)
                datos_fila.insert(2, num_pos)
                # Insertar None en la posición 10 si ani_pos es igual a 2023
                if (ani_pos == 2023):
                    datos_fila.insert(10, None)
                # Añadir los datos de la fila a la lista de datos
                datos.append(datos_fila)
            # Crear un DataFrame con los datos y lo agrega al DataFrame unificado 
            df3 = pd.DataFrame(datos[1:], columns=cabeceras)
            df_unificado = pd.concat([df_unificado, df3], ignore_index=True)
        else:
            print("No se encontró la tabla con el id 'tablaPostulantes'.")

    # Unir el DataFrame df_unificado con df2 utilizando las URLs de origen y destino como claves de unión
    df_postulantes = pd.merge(df_unificado, df2, left_on='url_origen', right_on='url_destino')
    # Seleccionar las columnas relevantes del DataFrame resultante
    df_postulantes = df_postulantes[['ani_pos', 'num_pos','CODIGO', 'APELLIDOS Y NOMBRES', 'ESCUELA PROFESIONAL (PRIMERA OPCION)', 'PUNTAJE', 'MERITO E.P', 'OBSERVACION', 'ESCUELA PROFESIONAL (SEGUNDA OPCION)', 'url_origen_y', 'escuela_profesional']]
    # Unir el DataFrame df_postulantes con df utilizando las URLs de origen y destino como claves de unión
    df_postulantes = pd.merge(df_postulantes, df, left_on='url_origen_y', right_on='url_destino')
    # Seleccionar las columnas relevantes del DataFrame resultante
    df_postulantes = df_postulantes[['ani_pos', 'num_pos', 'modalida_ingreso', 'escuela_profesional', 'CODIGO', 'APELLIDOS Y NOMBRES', 'ESCUELA PROFESIONAL (PRIMERA OPCION)', 'PUNTAJE', 'MERITO E.P', 'OBSERVACION', 'ESCUELA PROFESIONAL (SEGUNDA OPCION)']]
    
    # Convertir el DataFrame en una lista de tuplas
    data = [tuple(x) for x in df_postulantes.to_numpy()]

    # Ejecutar una consulta SQL para insertar los datos en la tabla tbingresos
    with cn_basdat.cursor() as cursor_basdat:
        v_sql_insert = "INSERT INTO public.tbingresos (ani_pos, num_pos, mod_ing, esc_pro, cod_est, nom_ape, esc_pri, num_pun, num_mer, des_obs, esc_seg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor_basdat.executemany(v_sql_insert, data)
        cn_basdat.commit() 
    
    # Consulta para actualizar el campo can_pun cuando des_obs es 'ALCANZO VACANTE PRIMERA OPCIÓN' o 'ALCANZO VACANTE SEGUNDA OPCIÓN'
    sql_query_1 = f"""
        update public.tbingresos set can_pun = num_pun::numeric
        where des_obs in (
            'ALCANZO VACANTE PRIMERA OPCIÓN',
            'ALCANZO VACANTE SEGUNDA OPCIÓN'
        )
        and ani_pos = {ani_pos}
        and num_pos = '{num_pos}'
        ;
    """
    # Consulta para actualizar el campo can_pun cuando des_obs tiene una longitud de 0
    sql_query_2 = f"""
    update public.tbingresos set can_pun = num_pun::numeric
    where length(des_obs) = 0
    and ani_pos = {ani_pos}
    and num_pos =  '{num_pos}'
    ;
    """
    # Consulta para actualizar el campo ord_mer cuando des_obs es 'ALCANZO VACANTE PRIMERA OPCIÓN' o 'ALCANZO VACANTE SEGUNDA OPCIÓN'
    sql_query_3 = f"""
    update public.tbingresos set ord_mer = num_mer::smallint
    where des_obs in (
        'ALCANZO VACANTE PRIMERA OPCIÓN',
        'ALCANZO VACANTE SEGUNDA OPCIÓN'
    )
    and ani_pos = {ani_pos}
    and num_pos = '{num_pos}'
    ;
    """
    # Ejecutamos las consultas SQL en la base de datos para actualizar registros
    with cn_basdat.cursor() as cursor_basdat:
        cursor_basdat.execute(sql_query_1)
        cursor_basdat.execute(sql_query_2)
        cursor_basdat.execute(sql_query_3)
        cn_basdat.commit() 