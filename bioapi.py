"""API Biodiversidad.
   API Rest encargada de exponer información de biodiversidad en
   Boyaca y Cundinamarca que se encuentra contenida en los archivo en formato JSON:
   1	animales_boyaca.json
   2	animales_cundinamarca.json
   3	hongos_boyaca.json
   4	hongos_cundinamarca.json
   5	plantas_boyaca.json
   6	plantas_cundinamarca.json
   
   Expone funciones como servicios, y estos métodos reciben como argumento
   general el tipo de consulta para así saber cual fuente o archivo de datos usar.

   Adicionalmente según el caso reciben página inicial/final, y/o id del especimen a
   consultar.

   Utiliza el paquete FastAPI para exponer funciones como  servicios web tipo REST.
   """
__author__ = "Serpenblack"
__copyright__ = "Copyright 2024, Desaextremo"
__credits__ = ["Desaextremo", "G10", "G11"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Team Desaextremo"
__email__ = "desarrolloextremo@gmail.com"
__status__ = "Production"

from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import json

#Llamamos a FastAPI, y desde este momento haremos referencia a este mediante la variable 'app'
app = FastAPI()

# Permitir solicitudes desde todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto a los orígenes que desees permitir
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/consultar/{tipo_consulta}/{inferior}/{superior}")
def retornar_datos(tipo_consulta: int,inferior: int,superior: int):
    """Expone funcíon 'retornar_datos' con el path 'consultar', para
    procesar peticiones get.
    Consulta información de biodiversidad a partir de archivos JSON, seleccionando
    el archivo a partir del valor recibido en el parámetro 'tipo_consulta', y filtrando
    dentro del total de datos contenidos en la lista python 'datos', el especimen cuya
    llave '_id' coincide con el valor recibido recibido en el parámetro 'id_especimen'.

    Parámetros:
    tipo_consulta (int) Corresponde al archivo de datos en el cual se debe buscar
    id_especimen (str) Corresponde a la llave '_id' del especimen a buscar.

    Retorno: lista de diccionario Python con información de los especimenes según
    el valor recibido en el parámetro 'tipo_consulta'
    """
    datos = []
    nombre_archivo = 'animales_boyaca.json'

    if tipo_consulta==1:
        nombre_archivo = "animales_boyaca.json"
    elif tipo_consulta==2:
        nombre_archivo = "animales_cundinamarca.json"
    elif tipo_consulta==3:
        nombre_archivo = "hongos_boyaca.json"
    elif tipo_consulta==4:
        nombre_archivo = "hongos_cundinamarca.json"
    elif tipo_consulta==5:
        nombre_archivo = "plantas_boyaca.json"
    elif tipo_consulta==6:
        nombre_archivo = "plantas_cundinamarca.json"
        #abrir el contenido del archivo en una lista

    with open(nombre_archivo,"r",encoding="utf8") as archivo:
        datos = json.load(archivo)

        #obtener la longitud o cantidad de registros
        longitud =len(datos)
        
        #obtenermos una parte de esa gran lista
        datos = datos[inferior-1:superior]

        #inserto la cantidad de registros en la posición 0
        datos.insert(0,{"rows":longitud})
    
    return datos

@app.get("/consultar_detalle/{tipo_consulta}/{id_especimen}")
def retornar_datos_detalle(tipo_consulta: int, id_especimen: str):
    """Expone funcíon 'retornar_datos_detalle' con el path 'consultar_detalle', para
       procesar peticiones get.
       Consulta información de biodiversidad a partir de archivos JSON, seleccionando
       el archivo a partir del valor recibido en el parámetro 'tipo_consulta', y filtrando
       dentro del total de datos contenidos en la lista python 'datos', el especimen cuya
       llave '_id' coincide con el valor recibido recibido en el parámetro 'id_especimen'.

    Parámetros:
        tipo_consulta (int) Corresponde al archivo de datos en el cual se debe buscar
        id_especimen (str) Corresponde a la llave '_id' del especimen a buscar
    Retorno:
        bool
    """
    encontrado = False
    especimen_encontrado = None

    datos = []
    nombre_archivo = 'animales_boyaca.json'

    if tipo_consulta==1:
        nombre_archivo = "animales_boyaca.json"
    elif tipo_consulta==2:
        nombre_archivo = "animales_cundinamarca.json"
    elif tipo_consulta==3:
        nombre_archivo = "hongos_boyaca.json"
    elif tipo_consulta==4:
        nombre_archivo = "hongos_cundinamarca.json"
    elif tipo_consulta==5:
        nombre_archivo = "plantas_boyaca.json"
    elif tipo_consulta==6:
        nombre_archivo = "plantas_cundinamarca.json"
        #abrir el contenido del archivo en una lista

    with open(nombre_archivo,"r",encoding="utf8") as archivo:
        datos = json.load(archivo)

    #recorre la lista valdiando la ubicación del diccionario con id == id
    for i, especimen in enumerate(datos):
        if (especimen['_id'] == id_especimen):
            encontrado = True
            especimen_encontrado = especimen
            break;
    
    return encontrado,especimen_encontrado

#método main para iniciar el servidor
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)