# olor
# asentamiento
# contaminacion
from function.functions import input_data, input_string, mayor, menor, promedio, mayor_problematica, menor_problematica
from classes.my_class import Municipio

municipios = [Municipio('Medellin', 100, 5, 35, 60), Municipio('Bogota', 300, 20, 35, 45), Municipio('Ibague', 50, 40, 11, 49)]
flag = True

while flag:
    accion = input_data('Ingrese la opcion correspondiente a la accion a realizar: \n\
    1. Ingresar un nuevo municipio. \n\
    2. Visualizar el municipio que mas toneladas por dia genera. \n\
    3. Visualizar el municipio que menos toneladas por dia genera. \n\
    4. Visualizar el promedio de toneladas por dia generadas. \n\
    5. Visualizar el promedio de toneladas por mes generadas. \n\
    6. Visualizar el mayor problema ambiental promedio. \n\
    7. Visualizar el menor problema ambiental promedio. \n\
    8. Visualizar el promedio de olores ofensivos. \n\
    9. Visualizar el promedio de asentamientos ilegales. \n\
    10. Visualizar el promedio de contaminacion de corrientes hidricas. \n\
    11. Salir del programa. \n\
    La opcion elegida es: ')
    if accion == 1:
        nuevo_municipio = Municipio(input_string('Introduzca el nombre del municipio: '), 
                                    input_data('Introduzca las toneladas por dia generadas: '),
                                    input_data('Introduzca el porcentaje del olor: '),
                                    input_data('Introduzca el porcentaje del asentamiento: '), 
                                    input_data('Introduzca el porcentaje de la contaminacion: '))
        municipios.append(nuevo_municipio)
    elif accion == 2:
        print(mayor(municipios,'toneladas dia'), 'toneladas dia.')
    elif accion == 3:
        print(menor(municipios, 'toneladas dia'), 'toneladas dia.')
    elif accion == 4:
        print(promedio(municipios, 'toneladas dia'), 'toneladas dia.')
    elif accion == 5:
        print(promedio(municipios, 'toneladas dia') * 30, 'toneladas mes.')
    elif accion == 6:
        mayor_problematica(municipios)
    elif accion == 7:
        menor_problematica(municipios)
    elif accion == 8:
        print(promedio(municipios, 'olor'), 'olores promedio.')
    elif accion == 9:
        print(promedio(municipios, 'asentamiento'), 'creacion de asentamientos ilegales promedio.')
    elif accion == 10:
        print(promedio(municipios, 'contaminacion'), 'contaminacion de corrientes hidricas promedio.')
    elif accion == 11:
        flag = False

