# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:19:40 2023

@author: Alumno
"""

igv= 0.18

def obtenerIGVconSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv*subtotal
    #subtotal*(1+0.18)
    
    return subtotal*(1 + igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)