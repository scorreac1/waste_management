from function.functions import input_data
class Municipio:
    def __init__(self, name, ton_dia, olor, asentamiento, contaminacion):
        self.name = name
        self.ton_dia = ton_dia
        self.verificar_valores(olor, asentamiento,contaminacion)

    def verificar_valores(self, olor, asentamiento,contaminacion):
        if (olor + asentamiento + contaminacion) == 100.0:
            self.olor = olor
            self.asentamiento = asentamiento
            self.contaminacion = contaminacion
        else:
            self.verificar_valores(input_data('Introduzca el porcentaje del olor: '),
                              input_data('Introduzca el porcentaje del asentamiento: '), 
                              input_data('Introduzca el porcentaje de la contaminacion: '))

    @property
    def dict(self) -> dict:
        return {
            "nombre": self.name,
            "toneladas dia": self.ton_dia,
            "olor": self.olor,
            "asentamiento": self.asentamiento,
            "contaminacion": self.contaminacion,
        }