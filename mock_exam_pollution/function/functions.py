def input_data(message):
    try:
        needed_data = float(input(message))
        return needed_data
    except ValueError:
        print('ValueError, try again.')
        return input_data(message)
    
def input_string(message):
    needed_data = input(message)
    return needed_data


# {"nombre": self.name,
#  "toneladas dia": self.ton_dia,
# "olor": self.olor,
# "asentamiento": self.asentamiento,
# "contaminacion": self.contaminacion}

def mayor(municipios, parametro):
    lista_diccionarios = []
    if len(municipios) < 1:
        return 'No hay municipios creados'
    for i in municipios:
        lista_diccionarios.append(i.dict)
    mayores = [lista_diccionarios[0]]
    for j in lista_diccionarios:
        if j[parametro] > mayores[0][parametro]:
            mayores.clear()
            mayores.append(j)
        elif j[parametro] == mayores[0][parametro]:
            mayores.append(j)
    return mayores    


def menor(municipios, parametro):
    lista_diccionarios = []
    if len(municipios) < 1:
        return 'No hay municipios creados'
    for i in municipios:
        lista_diccionarios.append(i.dict)
    menores = [lista_diccionarios[0]]
    for j in lista_diccionarios:
        if j[parametro] < menores[0][parametro]:
            menores.clear()
            menores.append(j)
        elif j[parametro] == menores[0][parametro]:
            menores.append(j)
    return menores    

def promedio(municipios, parametro):
    sumatoria = 0.0
    lista_diccionarios = []
    if len(municipios) < 1:
        return 'No hay municipios creados'
    for i in municipios:
        lista_diccionarios.append(i.dict)
    for j in lista_diccionarios:
        sumatoria += j[parametro] 
    promedio = sumatoria/len(municipios)
    return promedio   

def mayor_problematica(municipios):
    prom_olor = promedio(municipios, 'olor')
    prom_asentamiento = promedio(municipios, 'asentamiento')
    prom_contaminacion = promedio(municipios, 'contaminacion') 
    if prom_olor > prom_asentamiento:
        if prom_contaminacion > prom_olor:
            print('El mayor problema es la contaminacion')
        else:
            print('El mayor problema es el olor')
    else:
        if prom_asentamiento > prom_contaminacion:
            print('El mayor problema es el asentamiento')
        else:
            print('El mayor problema es la contaminacion')


def menor_problematica(municipios):
    prom_olor = promedio(municipios, 'olor')
    prom_asentamiento = promedio(municipios, 'asentamiento')
    prom_contaminacion = promedio(municipios, 'contaminacion') 
    if prom_olor < prom_asentamiento:
        if prom_contaminacion < prom_olor:
            print('El menor problema es la contaminacion')
        else:
            print('El menor problema es el olor')
    else:
        if prom_asentamiento < prom_contaminacion:
            print('El menor problema es el asentamiento')
        else:
            print('El menor problema es la contaminacion')