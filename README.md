# BIOAPI

## API Biodiversidad.
API Rest encargada de exponer información de biodiversidad en Boyaca y Cundinamarca que se encuentra contenida en los archivo en formato JSON:

1	animales_boyaca.json
2	animales_cundinamarca.json
3	hongos_boyaca.json
4	hongos_cundinamarca.json
5	plantas_boyaca.json
6	plantas_cundinamarca.json

* Expone funciones como servicios, y estos métodos reciben como argumento general el tipo de consulta para así saber cual fuente o archivo de datos usar.
* Adicionalmente según el caso reciben página inicial/final, y/o id del especimen a consultar.
* Utiliza el paquete FastAPI para exponer funciones como  servicios web tipo REST.
