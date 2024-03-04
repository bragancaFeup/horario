# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class Turmas

"""""
#%% Class Turmas
# Import the generic class
from classes.gclass import Gclass

class Turmas(Gclass):
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_desTurma']
    # Class header title
    header = 'Turmas'
    # field description for use in, for example, in input form
    des = ['Code','Desturma']
    
    # Constructor: Called when an object is instantiated
    def __init__(self, code,desTurma):
        # Object attributes
        self._code = code
        self._desTurma = desTurma

        # Add the new object to the Turmas list
        Turmas.obj[code] = self
        Turmas.lst.append(code)
    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    # desTurma property getter method
    @property
    def desTurma(self):
        return self._desTurma

    
    # setter methodes
    # code property setter method
    @code.setter
    def code(self, code):
        self._code = code
    # desTurma property setter method
    @desTurma.setter
    def desTurma(self, desTurma):
        self._desTurma = desTurma

 

if __name__ == "__main__":    
    
    Turmas.read('../data/' 'horario.db')
    # Creates a Turmas
    teste = Turmas('T1','Turma 1 MIEGI')
    teste.insert('T1')
    print(teste)
    
   
    
    