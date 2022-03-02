#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import complex as com
"""
Tests unitaires de la classe Complex
"""

#%% Test méthode __str__
c1=com.Complex(1,2,True)
c2=com.Complex(3,-4,True)
print("c1 = "+str(c1))
print("c2 = "+str(c2))

# %% Test méthode __add__
print("c1+c2 = "+str(c1.__add__(c2)))

#%%Test méthode __sub__
print("c1-c2 = "+str(c1.__sub__(c2)))

#%%Test méthode __mul
print("c1*c2 = "+str(c1.__mul__(c2)))

#%%Test méthode __truediv__
print("c1/c2 = "+str(c1.__truediv__(c2)))

#%%Test nouveau constructeur
z = com.Complex(1,2,True)
w = com.Complex(1.4,1.5,False)
print("z = "+str(z))
print("w = "+str(w))

# %%Test to_polar et to_cartesien
z = com.Complex(1,2,True)   #cartésien
zPolar = z.to_polaire()
w = com.Complex(1.4,1.5,False)
wCart = w.to_cartesien()
print("zPolar = "+str(zPolar))
print("wCart = "+str(wCart))

#%%Test print polaire
z = com.Complex(1,2,False)
z.print_polaire()