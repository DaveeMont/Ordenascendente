#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:41:34 2020

@author: dave-mont
"""
import statistics
import time
import sys

class Cromosoma:
    def __init__(self, genes, aptitud):
        self.Genes = genes
        self.Aptitud = aptitud
def _mutar(padre, geneSet, obtener_aptitud):
    indice = random. randrange(0, len(padre.Genes))
    genesNiño = list(padre.Genes)

    genes = ''.join(genesDelNiño)
    aptitud = obtener_aptitud(genes)
    return Cromosoma(genes, aptitud)

def _generar_padre(longitud, geneSet, obtener_aptitud):
    
    genes = ''.join(genes)
    aptitud = obtener_aptitud(genes)
    return Cromosoma(genes, aptitud)
#def obtener_mejor(obtener_aptitud, longitudObjetivo, aptitudOptima,geneSet, mostrar):
    
    


def _obtener_mejoras(nuevo_niño, generar_padre):
    mejorPadre = generar_padre()
    yield mejorPadre
    while True:
        niño = nuevo_niño(mejorPadre)
        if mejorPadre.Aptitud > niñoAptitud:
            continue
        if not niño.Aptitud > mejorPadre.Aptitud:
            mejorPadre = niño
            continue
        yield niño
        mejorPadre = niño
def obtener_mejor(obtener_aptitud, longitud,Objetivo, aptitudOptima, geneSet, mostrar):
    random.seed()
    mejorPadre = _generar_padre(longitudObjetivo, geneSet, obtener_aptitud)
    mostrar(mejorPadre)
    if mejorPadre.Aptitud >= aptitudOptima:
        return mejorPadre
    
    while True:
        niño = _mutar(mejorPadre, geneSet, obtener_aptitud)
        if mejorPadre.Aptitud >= niño.Aptitud:
            continue
        mostrar(niño)
        if niño.Aptitud >= aptitudOptima:
            return niño
        mejorPadre = niño
    
    def fnMutar(padre):
        return _mutar(padre, geneSet, obtener_aptitud)
    for mejora in _obtener_mejoras(fnMutar, fnGenerarPadre):
        mostrar(mejora)
        if not aptitudOptima > mejora.Aptitud:
            return mejora
    
class Comparar:
    @staticmethod
    def ejecutar(funcion):
        cronometrajes = []
        
        stdout - sys.stdout
        for i in range(100):
            sys.stdout = NullWriter()
            horaInicio = time.time()
            funcion()
            segundos = time.time() - horaInicio
            sys.stdout - stdout
            cronometrajes.append(segundos)
            promedio = statistics.mean(cronometrajes)
            if i < 10 or i % 10 == 9:
                print("{} {:3.2f} {:3.2f}".format(1 + i, promedio, statistics.stdev(cronometrajes, promedio) if i > 1 else 0))
class NullWriter():
    def write(self,s):
        pass
    
