#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import intset as iset

"""
Tests unitaires de la classe IntSet
"""

#%% Test de la méthode __str__ 
e = iset.IntSet()
for i in range(1,5):
    e.insert(i)
print('e:', e)

v = iset.IntSet()
print('v:', v)

#%% test de la méthode member
s = iset.IntSet()
for i in [1,5,4,3]:
    s.insert(i)
m5 = s.member(5)
m2 = s.member(2)
print('s:', s)
print('5 member of s:', m5)
print('2 member of s:', m2)

#%% Test de la méthode remove
s = iset.IntSet()
for i in [1,5,4,3]:
    s.insert(i)
print('s:', s)
r3 = s.remove(3)
print('3 removed from s:', r3)
r7 = s.remove(7)
print('7 removed from s:', r7)
print('s:', s)

#%% Test de la méthode intersect
s1 = iset.IntSet()
for i in [1,5,4,3]:
    s1.insert(i)
s2 = iset.IntSet()
for i in [1,6,4,7]:
    s2.insert(i)
s = s1.intersect(s2)
print('s1:', s1)
print('s2:', s2)
print('s1 ∩ s2:', s)

#%% Test de la méthode union
s1 = iset.IntSet()
for i in [1,5,4,3]:
    s1.insert(i)
s2 = iset.IntSet()
for i in [5,7,8,9]:
    s2.insert(i)
s = s1.union(s2)
print('s1:', s1)
print('s2:', s2)
print('s1 U s2:', s)

#%% Test de la méthode différence
s1 = iset.IntSet()
for i in [1,5,4,3,8]:
    s1.insert(i)
s2 = iset.IntSet()
for i in [5,7,8,9]:
    s2.insert(i)
s = s1.difference(s2)
print('s1:', s1)
print('s2:', s2)
print('s1 \ s2:', s)

#%% Test de la méthode différence symétrique
s1 = iset.IntSet()
for i in [1,5,4,3,8]:
    s1.insert(i)
s2 = iset.IntSet()
for i in [5,7,8,9]:
    s2.insert(i)
s = s1.diff_sym(s2)
print('s1:', s1)
print('s2:', s2)
print('s1 Δ s2:', s)

#%% Test de la méthode différence symétrique (bis)
s1 = iset.IntSet()
for i in [1,5,4,3,8]:
    s1.insert(i)
s2 = iset.IntSet()
for i in [5,7,8,9]:
    s2.insert(i)
s = s1.diff_sym_bis(s2)
print('s1:', s1)
print('s2:', s2)
print('s1 Δ s2:', s)
