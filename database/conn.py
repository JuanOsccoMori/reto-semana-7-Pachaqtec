from pymongo import MongoClient, errors

class Conexion:
    def __init__(self, cadena_conexion, base_datos, coleccion):
        self.client = MongoClient(
            cadena_conexion 
        )
        self.db = self.client[base_datos]
        self.coleccion = self.db[coleccion]

    def insertar_registro(self, registro):
        resultado = self.coleccion.insert_one(registro)
        print(f'Se inserto el elemento a la coleccion {resultado.inserted_id}')

    def insertar_registros(self, registro):
        resultado = self.coleccion.insert_many(registro)
        print(f'Se inserto el elemento a la coleccion {resultado.inserted_ids}')

    def obtener_registros(self, condicion):
        registros = self.coleccion.find(condicion)
        return list(registros)

    def obtener_registro(self, condicion):
        registro = self.coleccion.find_one(condicion)
        return registro

    def actualizar_registro(self, condicion, atributos_cambiar):
        resultado = self.coleccion.update_one(
            condicion, {
                '$set': atributos_cambiar
            }
        )
        return resultado.modified_count > 0

    def eliminar_registro(self, condicion):
        resultado = self.coleccion.delete_one(
            condicion
        )
        return resultado.deleted_count > 0