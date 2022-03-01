# -*- coding: utf-8 -*-

class IntSet(object):
    """An IntSet is a set of integers
    The values contained in the set are represented by a list of integers: self.vals
    Each integer in the set occurs in self.vals exactly once.
    """
    
    def __init__(self):
        """Creates an empty set of integers
        input   -- self : instance of class IntSet
        """
        self.vals = []
        
    def __str__(self):
        """Returns a string representation of self
        input   -- self : instance of class IntSet
        output  -- string: shows the list of elements in self (string type)
        """
        res=""
        if (len(self.vals)==0):
            res=""
        else :
            res+="{"+str(self.vals[0])
            for i in range(1,len(self.vals)):
                res+=", "+str(self.vals[i])
            res+="}"
        return res

    def insert(self, e):
        """Inserts e into self
        input   -- self : instance of class IntSet
                -- e : integer
        """ 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Returns True if e is in self, and False otherwise
        input   -- self : instance of class IntSet
                -- e : integer, the value to be tested
        output  -- bool, is True if e is in self, False otherwise
        """
        return e in self.vals

    def remove(self, e):
        """Removes e from self. If e is not in self, do nothing
        Raises ValueError if e is not in self
        input   -- self : instance of class IntSet
                -- e : integer
        output  -- bool, True if e has been removed
        """
        if self.member(e):
            self.vals.remove(e)
            return True
        return False

    def intersect(self, other):
        """Returns the intersection of the sets self and other
        input  -- self : instance of class IntSet
               -- other : instance of class IntSet
        output -- instance of class IntSet, the intersection of self and other 
        """
        
        result=IntSet()
        for i in self.vals:
            if (other.member(i)):
                result.insert(i)
        return result
    
    def union(self, other):
        """Returns the union of the sets self and other
        input  -- self : instance of class IntSet
               -- other : instance of class IntSet
        output -- instance of class IntSet, the union of self and other 
        """
        result=IntSet()
        for i in self.vals:
            result.insert(i)
            
        for j in other.vals:
            if (not result.member(j)):
                result.insert(j)
                
        return result
    
    def difference(self, other):
        """Returns the difference of the sets self and other
        input  -- self : instance of class IntSet
               -- other : instance of class IntSet
        output -- instance of class IntSet, the difference of self and other 
        """
        result=IntSet()
        for i in self.vals:
            if not other.member(i):
                result.insert(i)
        return result
    
    def diff_sym(self, other):
        """Returns the symetric difference of the sets self and other, i.e. e set
           that contains all elements that appear only once in the sets self and other
        input  -- self : instance of class IntSet
               -- other : instance of class IntSet
        output -- instance of class IntSet, the difference of self and other 
        """
        result=IntSet()
        for i in self.vals:
            if not other.member(i):
                result.insert(i)
        for j in other.vals:
            if not self.member(j):
                result.insert(j)
        return result

    
    def diff_sym_bis(self, other):
        """Returns the symetric difference of the sets self and other, i.e. e set
           that contains all elements that appear only once in the sets self and other
        input  -- self : instance of class IntSet
               -- other : instance of class IntSet
        output -- instance of class IntSet, the difference of self and other 
        """
        uni=self.union(other)
        inter=self.intersect(other)
        return uni.difference(inter)
        
                
#%%
if __name__ == '__main__':
    
    print('Hello IntSet !!!')
