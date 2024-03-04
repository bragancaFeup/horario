# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class Salas

"""""
#%% Class Salas
# Import the generic class
from classes.gclass import Gclass


class Salas(Gclass):
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_NomeSala']
    # Class header title
    header = 'Salas'
    # field description for use in, for example, in input form
    des = ['Code','NomeSala']
    
    # Constructor: Called when an object is instantiated
    def __init__(self, code,NomeSala):
        # Object attributes
        self._code = code
        self._NomeSala = NomeSala

        # Add the new object to the Salas list
        Salas.obj[code] = self
        Salas.lst.append(code)
    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    # NomeSala property getter method
    @property
    def NomeSala(self):
        return self._NomeSala

    
    # setter methodes
    # code property setter method
    @code.setter
    def code(self, code):
        self._code = code
    # NomeSala property setter method
    @NomeSala.setter
    def NomeSala(self, NomeSala):
        self._NomeSala = NomeSala



if __name__ == "__main__":    
    
    Salas.read('../data/' 'horario.db')
    # Creates a Salas
    teste = Salas('B102','Salas B102')
    teste.insert('B102')
    print(teste)
      
    