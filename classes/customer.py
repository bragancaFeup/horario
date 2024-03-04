# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class Customer_login

"""""
#%% Class Customer_login
# Import the generic class
from classes.gclass import Gclass

class Customer(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_name','_address','_phone','_login']
    # Class header title
    header = 'Customers'
    # field description for use in, for example, in input form
    des = ['Code','Name','Address','Phone','User Login']
    # Constructor: Called when an object is instantiated
    def __init__(self, code,name,address,phone,login):
        super().__init__()
        # Object attributes
        self._code = code
        self._name = name
        self._address = address
        self._phone = phone
        self._login = login
        # Add the new object to the Customer_login list
        Customer.obj[code] = self
        Customer.lst.append(code)

    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    # name property getter method
    @property
    def name(self):
        return self._name
    # address property getter method
    @property
    def address(self):
        return self._address
    # phone property getter method
    @property
    def phone(self):
        return self._phone
    # login property getter method
    @property
    def login(self):
        return self._login
    # name property setter method
    @name.setter
    def name(self, name):
        self._name = name
    # address property setter method
    @address.setter
    def address(self, address):
        self._address = address
    # phone property setter method
    @phone.setter
    def phone(self, phone):
        self._phone = phone
    # login property setter method
    @login.setter
    def login(self, login):
        self._login = login