#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 23:09:27 2020

@author: dave-mont
"""

import unittest
import datetime
import genetic
    #funcion para devolver el numero de genes que 
    #estan en orden ascendete
def obtener_aptitud(genes):
    #La funcion devolvera un recuento de los numeros adiacentes
    #muestra los genes acitales, su aptitud y 
    #el tiempo transcurrido
    # No admite caracteres como el nombre de la clase
    aptitud = 1
    brecha = 0
    for i in range(1,len(genes)):
        if genes [i] > genes [i - 1]:
            aptitud +=1
        else:
            brecha += genes[i - 1] - genes[i]
    return Aptitud(aptitud, brecha)
    
def mostrar(candidato, horaInicio):
    #mostrara los valores del arreglo separados por una coma
    diferencia = (datetime.datetime.now() - horaInicio).total_seconds()
    print("{}\t=> {}\t{}".format(', '.join(map(str, candidato.Genes)),candidato.Aptitud,diferencia))
class PruebasNumerosOrdenados(unittest.TestCase):
    def test_ordena_3_numeros(self):
        self.ordenar_numeros(3)
        
    def test_ordena_10_numeros(self):
        self.ordenar_numeros(10)    
        
    def ordenar_numeros(self, numerosTotales):
        #Inicia el temporizador
        #crea las funciones auxiliares y la aptitud optima
        # Despues lamma a genetic.obtener_mejor()
        #Finalmente, asevera que la aptitud del resultado es optima
        genSet = [i for i in range(100)] #LISTA POR COMPRENSION
        aptitudOptima = Aptitu(numerosTotales, 0)
        mejor = genetic.obtener_mejor(fnObtenerAptitud, numerosTotales, aptitudOptima, genSet, fnMostrar)
        self.assertTrue(not aptitudOptima > mejor.Aptitud)

class Aptitud:
    def __init__(self, numerosEnSecuencia,brechaTotal):
        self.NumerosEnSecuencia = NumerosEnSecuencia
        self.BrechaTotal = brechaTotal
    
    def __gt__(self,otro): #Funcion que busca el comparador >
        if self.NumerosEnSecuencia !=otro.NumerosEnSecuencia:
            return self.NumerosEnSecuencia > otro.NumerosEnSecuencia
        return self.BrechaTotal < otro.BrechaTotal
            
    def __str__(self):
        return "{}secuencial, distancia {}".format(self.NumerosEnSecuencia,self.BrechaTotal)
def obtener_mejor(obtener_aptitud, longitudObjetivo,aptitudOptima, genSet, mostrar ):
    if not aptitudOptima > mejorPadre.Aptitud:
        return mejorPadre
    while True:
        niño = _mutar(mejorPadre, genSet, Obtener_aptitud)
        if not niño.Aptitud > mejorPadre.Aptitud:
            continue
        monstrar(niño)
        if not aptitudOptima > niño.Aptitud:
            return niño
        mejorPadre = niño
def test_comparativa(self):
    genetic.Comparar.ejecutar(lambda: self.ordenar_numeros(40))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        