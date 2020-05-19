from database.conn import Conexion

class Colegio:
    def __init__(self, profesor, alumno, notas):
        self.profesor = profesor
        self.alumno = alumno
        self.notas = notas


    @staticmethod
    def ingresarDatos(content):
        colecion = str(input('que curso enseñas?: ')) 
        c = Conexion('mongodb://localhost', 'Colegio', colecion)
        insertar = []
        for i in content:
            calificaciones = i.notas
            promedio = sum(calificaciones) / len(calificaciones)
            crear = {
                'profesor': i.profesor,
                'alumno': i.alumno,
                'notas': calificaciones,
                'min_nota': min(calificaciones),
                'max_nota': max(calificaciones),
                'promedio': promedio
            }
            insertar.append(crear)
        if content:
            c.insertar_registros(insertar)
            print("Se creo una BD con su respectiva coleccion que es el nombre del curso!")
