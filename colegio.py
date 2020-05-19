from classes.integrantes import Colegio
from database.conn import Conexion

def registro():
    try:
        lista = []
        nro_docente= int(input('ingrese el nro de docentes: '))
        a = 1
        while True:
            try:
                docente = input(f'ingresa el nombre del docente nr°{a}: ')
                nro_alumnos = int(input('ingrese el numero de alumnos de tu clase: '))
                b = 1
                while True:
                    try:
                        nombre = input(f'ingrese el nombre del alumno Nr°{b}: ')
                        nro_notas = int(input('cuantas notas deseas agregar: '))
                        calificaciones = []
                        c = 1

                        while True:
                            try:
                                nota = int(input(f'ingresa la nota de {nombre}: '))
                                if nota < 0 or nota > 20:
                                    raise Exception('no es la nota dentro del promedio')
                                calificaciones.append(
                                    (nota)
                                )
                                c +=1
                                if c > nro_notas:
                                    break
                            except ValueError:
                                print('no ingresaste algo')

                        b += 1
                        if b > nro_alumnos:
                            break
                    except ValueError:
                        print('no ingresaste algo')

                registro = Colegio(docente, nombre, calificaciones)
                lista.append(registro)
                a += 1
                if a > nro_docente:
                    break
            except ValueError:
                print('debes de ingresar algo')

        if lista:
            Colegio.ingresarDatos(lista)

    except ValueError:
        print('no ingresaste algo')
    except KeyboardInterrupt:
        print('se corto!')
    except Exception as a:
        print(f'Se Encontro un error aqui: {str(a)}')

def listado():
    try:

        a = input('que curso que registrate deseas ver?: ')
        c = Conexion('mongodb://localhost', 'Colegio',a)
        listar = c.obtener_registros({})
        for i in enumerate(listar, start=1):
            print(i)

    except Exception as b:
        print(f'error aqui: {str(b)}')
    except KeyboardInterrupt:
        print('Forzaste a la aplicacion a cerrarla!')

def actualizar():
    try:
        f = input('de que colecion que creaste deseas Actualizar?: ')
        g = Conexion('mongodb://localhost', 'Colegio',f)
        profesor = input('como se llama el profesor?')
        documento = g.obtener_registros({
            'profesor': profesor
        })
        for b in documento:
            print(b)
        antiguo_profe = input('escriba el nombre del profesor para actualizar todo el campo: ')
        nuevo_profesor = input('ingrese el nuevo nombre del profesor: ')
        nuevo_alumno = input('ingrese el nuevo nombre del alumno: ')
        if documento:
            g.actualizar_registro(
                {
                    'profesor': antiguo_profe
                },
                {'profesor':nuevo_profesor ,'alumno': nuevo_alumno}
            )
        else:
            print('No se encuentran los datos')
    except ValueError:
        print('olvidaste poner algo')
    except Exception as a:
        print(f'Hubo un error aqui: {str(a)}')

def eliminar():
    try:
        e = input('de que colecion que creaste deseas eliminar?: ')
        d = Conexion('mongodb://localhost', 'Colegio',e)
        profesor = input('Como se llama tu profesor?: ')

        documento = d.obtener_registros({
            'profesor': profesor
        })
        for c in documento:
            print(c)
        
        eliminacion = input('que alumno deseas eliminar?: ')
        if documento:
            d.eliminar_registro(
                {
                    'alumno': eliminacion
                }
            )
            print('Se elimino con exito!')
        else:
            ('no esta el usuario registrado')
    except Exception as c:
        print(f'error aqui: {str(c)}')

def main():
    print('BIENVENIDO AL COLEGIO PEREZ DE CUELLAR')
    print('PARA AGREGAR UN NUEVO REGISTRO DE COLECIONES, ESCRIBA 1')
    print('PARA LISTAR LAS COLECIONES, ESCRIBA 2')
    print('PARA ACTUALIZAR UN USUARIO ESCRIBA 3')
    print('PARA ELIMINAR UN ALUMNO ESCRIBA 4')
    print('Si deseas salir escriba 7')

    opcion = int(input('ingresa el numero: '))

    if opcion == 1:
        registro()
    elif opcion == 2:
        listado()
    elif opcion == 3:
        actualizar()
    elif opcion == 4:
        eliminar()
    elif opcion == 7:
        return False

main()