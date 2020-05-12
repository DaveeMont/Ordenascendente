#deip ijdlvrga
import datetime
import unittest

import genetic


def obtener_aptitud(genes):
    aptitud = 1
    brecha = 0

    for i in range(1, len(genes)):
        if genes[i] > genes[i - 1]:
            aptitud += 1
        else:
            brecha += genes[i - 1] - genes[i]
    return Aptitud(aptitud, brecha)


def mostrar(candidato, horaInicio):
    diferencia = (datetime.datetime.now() - horaInicio).total_seconds()
    print("{}\t=> {}\t{}".format(
        ', '.join(map(str, candidato.Genes)),
        candidato.Aptitud,
        diferencia))


# `nosetests` no admite caracteres como ú en el nombre de la clase
class PruebasDeNumerosOrdenados(unittest.TestCase):
    def test_ordenar_10_números(self):
        self.ordenar_números(10)

    def ordenar_números(self, númerosTotales):
        geneSet = [i for i in range(100)]
        horaInicio = datetime.datetime.now()

        def fnMostrar(candidato):
            mostrar(candidato, horaInicio)

        def fnObtenerAptitud(genes):
            return obtener_aptitud(genes)

        aptitudÓptima = Aptitud(númerosTotales, 0)
        mejor = genetic.obtener_mejor(fnObtenerAptitud, númerosTotales,
                                      aptitudÓptima, geneSet, fnMostrar)
        self.assertTrue(not aptitudÓptima > mejor.Aptitud)

    def test_comparativa(self):
        genetic.Comparar.ejecutar(lambda: self.ordenar_números(40))


class Aptitud:
    def __init__(self, númerosEnSecuencia, brechaTotal):
        self.NúmerosEnSecuencia = númerosEnSecuencia
        self.BrechaTotal = brechaTotal

    def __gt__(self, otro):
        if self.NúmerosEnSecuencia != otro.NúmerosEnSecuencia:
            return self.NúmerosEnSecuencia > otro.NúmerosEnSecuencia
        return self.BrechaTotal < otro.BrechaTotal

    def __str__(self):
        return "{} secuencial, distancia {}".format(
            self.NúmerosEnSecuencia,
            self.BrechaTotal)


if __name__ == '__main__':
    unittest.main()