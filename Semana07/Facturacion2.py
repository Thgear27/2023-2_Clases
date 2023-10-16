# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:28:50 2023

@author: Alumno
"""

import financieros

total = 1000.49
print(f"Subtotal: {financieros.obtenerSubtotalconTotal(total): .2f}")
print(f"IGV: {financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")
