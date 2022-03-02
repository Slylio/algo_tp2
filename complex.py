# -*- coding: utf-8 -*-
import math


class Complex(object):

   def __init__(self,a,b,cartPolaire):
      """Creates a complex
      input   -- self : instance of class Complex
      """
      self.cartPolaire=cartPolaire
      if cartPolaire:
         self.real=a
         self.imag=b
      else :
         self.rho=a
         self.theta=b

   def __str__(self):
      """Affiche un nombre complexe"""
      if (self.cartPolaire):
         if self.imag > 0:
            return str(round(self.real, 2))+"+"+"i."+str(round(self.imag, 2))
         else:
            return str(round(self.real, 2))+"-i."+str(round(-self.imag, 2))
      else :
         if self.theta > 0:
            return str(round(self.rho, 2))+"exp(i."+str(round(self.theta, 2))+")"
         else :
            return str(round(self.rho, 2))+"exp(-i."+str(round(-self.theta, 2))+")"

   def __add__(self, other):
      """additionne 2 nombres complexes
      input -- self : instance of class Complex
            -- other : instance of Class Complex
      output -- instance of class Complex the addition of self and other
      """
      if self.cartPolaire:
         result = Complex(0,0,True)
         result.real = self.real+other.real
         result.imag = self.real+other.imag  
      else :
         result = Complex(0,0,False)
         result.rho = self.rho+other.rho
         result.theta = self.theta+other.theta  
     
      return result

   def __sub__(self, other):
      """soustrait 2 nombres complexes
      input -- self : instance of class Complex
            -- other : instance of Class Complex
      output -- instance of class Complex the substraction of self and other
      """
      if self.cartPolaire:
         result = Complex(0,0,True)
         result.real = self.real-other.real
         result.imag = self.imag-other.imag
      else :
         result = Complex(0,0,False)
         result.rho = self.rho-other.rho
         result.theta = self.theta-other.theta
      
      return result

   def __mul__(self, other):
      """divise 2 nombres complexes
      input -- self : instance of class Complex
            -- other : instance of Class Complex
      output -- instance of class Complex the multiplication of self and other
      """
      if self.cartPolaire:
         result = Complex(0,0,True)
         result.real=self.real*other.real
         result.imag=self.imag*other.imag
      else :
         result = Complex(0,0,False)
         result.rho = self.rho*other.rho
         result.theta = self.theta*other.theta
      return result

   def __truediv__(self, other):
      """divise 2 nombres complexes 
      input -- self : instance of class Complex
            -- other : instance of Class Complex
      output -- instance of class Complex the divide of self and other
      """
      if self.cartPolaire:
         result = Complex(0,0,True)
         if other.real!=0 and other.imag!=0:
            result.real=self.real/other.real
            result.imag=self.imag/other.imag
      else :
         result = Complex(0,0,False)
         if other.rho!=0 and other.theta!=0:
            result.rho=self.rho/other.rho
            result.theta=self.theta/other.theta
      return result
   
   def to_polaire(self):
      """transforme un cartésien en polaire
      input -- self : instance of class Complex
      output -- instance of class Complex the polar version of self
      """
      r=math.sqrt(self.real^2+self.imag^2)
      t=1/math.tan(self.imag/self.real)
      return Complex(r, t, False)

   def to_cartesien(self):
      """transforme un polaire en cartésien
      input -- self : instance of class Complex
      output -- instance of class Complex the cartesian version of self
      """
      r=self.rho*math.cos(self.theta)
      i=self.rho*math.sin(self.theta)
      return Complex(r, i, True)

   def print_polaire(self):
      if not self.cartPolaire:
         if self.theta > 0:
            print(str(round(self.rho, 2))+"exp(i."+str(round(self.theta, 2))+")")
         else :
            print(str(round(self.rho, 2))+"exp(-i."+str(round(-self.theta, 2))+")")
      else :
         print("Entrez une expression Polaire")