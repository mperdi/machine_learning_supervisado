# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:21:50 2021

@author: Usuario
"""

def espejo(c):
    valor = ord(c)
    if valor >= ord('a') and valor <= ord('z'):
        valor = ord(c)
        resta = ord('z') - valor
        espejo = ord('a') + resta
        espejo_caracter = chr(espejo)
    else:
        return c
    return espejo_caracter
    

def espejo1(inic, fin, c):
    valor_inicial = ord(inic)
    valor_final = ord(fin)
    valor_c = ord(c)
    if valor_c >= valor_inicial and valor_c <= valor_final:
        resta = valor_final - valor_c
        suma = valor_inicial + resta
    else:
        return c
    return chr(suma)


def caracter_menor(string):
    menor = ord(string[0])
    for i in range(1, len(string)):
        if menor > ord(string[i]):
            menor = ord(string[i])
        else:
            pass
    return chr(menor)

def caracter_mayor(string):
    mayor = ord(string[0])
    for i in range(1, len(string)):
        if mayor < ord(string[i]):
            mayor = ord(string[i])
        else:
            pass
    return chr(mayor)

def codifica_espejo(string):
    menor = caracter_menor(string)
    mayor = caracter_mayor(string)
    nuevo_string = ''
    for i in range(0, len(string)):
        nueva_letra = espejo1(menor, mayor, string[i])
        nuevo_string = nuevo_string + nueva_letra
    return nuevo_string
    
    
    

    