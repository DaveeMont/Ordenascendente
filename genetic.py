#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:41:34 2020

@author: dave-mont
"""

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
    def fnMutar(padre):
        return _mutar(padre, geneSet, obtener_aptitud)
    for mejora in _obtener_mejoras(fnMutar, fnGenerarPadre):
        mostrar(mejora)
        if not aptitudOptima > mejora.Aptitud:
            return mejora
    