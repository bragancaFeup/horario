# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class UnidadeCurric

"""""
#%% Class UnidadeCurric
# Import the generic class
from classes.gclass import Gclass

class UnidadeCurric(Gclass):
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_NomeUC']
    # Class header title
    header = 'Unidade Corricular'
    # field description for use in, for example, in input form
    des = ['Code','NomeUC']
    
    # Constructor: Called when an object is instantiated
    def __init__(self, code,nomeUC):
        # Object attributes
        self._code = code
        self._NomeUC = nomeUC

        # Add the new object to the UnidadeCurric list
        UnidadeCurric.obj[code] = self
        UnidadeCurric.lst.append(code)
    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    # NomeUC property getter method
    @property
    def NomeUC(self):
        return self._NomeUC

    
    # setter methodes
    # code property setter method
    @code.setter
    def code(self, code):
        self._code = code
    # NomeUC property setter method
    @NomeUC.setter
    def NomeUC(self, NomeUC):
        self._NomeUC = NomeUC

  


if __name__ == "__main__":    
    
    UnidadeCurric.read('../data/' 'horario.db')
    # Creates a UnidadeCurric
    teste = UnidadeCurric('PC1','NomeUC')
    teste.insert('PC1')
    print(teste)
      
    