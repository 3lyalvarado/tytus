
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Tanh(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("TANH")
        print(math.tanh(self.valor))
        return math.tanh(self.valor)

'''
instruccion = Tanh(1,None, 1,2)

instruccion.ejecutar(None,None)
'''