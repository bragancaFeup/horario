# -*- coding: utf-8 -*-
    
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class Docentes

"""""
#%% Class Docentes
# Import the generic class
from classes.gclass import Gclass

class Docentes(Gclass):
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_nomeDocente']
    # Class header title
    header = 'Docentes'
    # field description for use in, for example, in input form
    des = ['Code','NomeDocente']
    
    # Constructor: Called when an object is instantiated
    def __init__(self, code,nomeDocente):
        super().__init__()
        # Object attributes
        self._code = code
        self._nomeDocente = nomeDocente

        # Add the new object to the Docentes list
        Docentes.obj[code] = self
        Docentes.lst.append(code)
    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    # nomeDocente property getter method
    @property
    def nomeDocente(self):
        return self._nomeDocente

    
    # setter methodes
    # code property setter method
    @code.setter
    def code(self, code):
        self._code = code
    # nomeDocente property setter method
    @nomeDocente.setter
    def nomeDocente(self, nomeDocente):
        self._nomeDocente = nomeDocente

 
if __name__ == "__main__":    
    
  
    # Creates a Docentes
    Docentes.read('../data/' 'horario.db')
    
    teste = Docentes('d1','Manuel Silva')
    teste.insert('d1')
    print(teste)
      
    