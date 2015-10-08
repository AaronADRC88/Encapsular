__author__ = 'aferreiradominguez'


class Persoa:
    """Clase que definae unha persoa """

    def __init__(self, nome):
        self.nome = nome

    def sauda(self):
        print("Ola " + self.nome)


persona = Persoa("aaron")
persona.sauda()


class Oficio:
    """Clase que define oficio"""

    def __init__(self, oficio):
        self.oficio = oficio

    def mostraOfi(self):
        print("O oficio e: " + self.oficio)


class Traballador(Persoa, Oficio):
    """Herdanza multiple"""

    def __init__(self, nome, oficio, soldo):
        Persoa.__init__(self, nome)
        Oficio.__init__(self, oficio)
        self.soldo = soldo
        """chamamos ao metodo privado"""
        self.__mostraDatos()

    def mostraSoldo(self):
        print("O soldo e: " + str(self.soldo))

    """Metodo privado"""

    def __mostraDatos(self):
        print("O soldo e: " + str(self.soldo) + " O nome e: " + self.nome + " O oficio e: " + str(self.oficio))


t = Traballador("Pepinho", "Canteiro", 1000)
t.sauda()
t.mostraOfi()
t.mostraSoldo()
"""chamamos ao metodo privado"""
t._Traballador__mostraDatos()


class Fecha(object):
    def __init__(self):
        self.__dia = 1

    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
        else:
            print("error")

    dia = property(getDia, setDia)


data = Fecha()
print(data.dia)
data.setDia(23)
print(data.getDia())
data.dia = 33
