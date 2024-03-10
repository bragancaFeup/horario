# -*- coding: utf-8 -*-

"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class Class_horario

"""""
import datetime

from datetime import timedelta
# Import the generic class
from classes.gclass import Gclass

class Class_horario(Gclass):
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_diahora','_cod_turma','_cod_prof','_cod_uc','_cod_sala','_obs']
    # Class header title
    header = 'Class_horario'
    # field description for use in, for example, in input form
    des = ['code','diahora','cod_turma','cod_prof','cod_uc','cod_sala','obs']
    # Constructor: Called when an object is instantiated
    def __init__(self, code,diahora,cod_turma,cod_prof,cod_uc,cod_sala,obs):
        #Uncomment in case of auto number on
        if code == 'None':
            codes = Class_horario.getatlist('_code')
            if codes == []:
                code = str(1)
            else:
                code = str(max(map(int,Class_horario.getatlist('_code'))) + 1)
        # Object attributes
        self._code = code
        self._diahoradate = self.str2datetime(diahora)
        self._diahora = self.str2datetimestr(self._diahoradate)
        
        self._cod_turma = cod_turma
        self._cod_prof = cod_prof
        self._cod_uc = cod_uc
        self._cod_sala = cod_sala
        self._obs = obs

        # Add the new object to the Class_horario list
        Class_horario.obj[code] = self
        Class_horario.lst.append(code)
    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    # diahora property getter method
    @property
    def diahora(self):
        return self._diahora
    # cod_turma property getter method
    @property
    def cod_turma(self):
        return self._cod_turma
    # cod_prof property getter method
    @property
    def cod_prof(self):
        return self._cod_prof
    # cod_uc property getter method
    @property
    def cod_uc(self):
        return self._cod_uc
    # cod_sala property getter method
    @property
    def cod_sala(self):
        return self._cod_sala
    # obs property getter method
    @property
    def obs(self):
        return self._obs
    
    # dia property getter method
    @property
    def dia(self):
        return self.diahora.date()

    
    # setter methodes
    # code property setter method
    @code.setter
    def code(self, code):
        self._code = code
    # diahora property setter method
    @diahora.setter
    def diahora(self, diahora):
        self._diahora = diahora
    # cod_turma property setter method
    @cod_turma.setter
    def cod_turma(self, cod_turma):
        self._cod_turma = cod_turma
    # cod_prof property setter method
    @cod_prof.setter
    def cod_prof(self, cod_prof):
        self._cod_prof = cod_prof
    # cod_uc property setter method
    @cod_uc.setter
    def cod_uc(self, cod_uc):
        self._cod_uc = cod_uc
    # cod_sala property setter method
    @cod_sala.setter
    def cod_sala(self, cod_sala):
        self._cod_sala = cod_sala
    # obs property setter method
    @obs.setter
    def obs(self, obs):
        self._obs = obs
        
    def str2datetimestr(self,date):
        
        return str(date)
        
    def str2datetime(self,datestr):
        
        datestr = datestr.replace("/", ";")
        datestr = datestr.replace("-", ";")
        datestr = datestr.replace(":", ";")
        datestr = datestr.replace(" ", ";")
        
        diahorastr =list(map(int, datestr.split(";")))
        
        date = datetime.datetime(diahorastr[0], diahorastr[1], diahorastr[2])
        if len(diahorastr)>3:
            date=date.replace(hour = diahorastr[3])
        if len(diahorastr)>4:
            date=date.replace(minute=  diahorastr[4])
        if len(diahorastr)>5:
            date=date.replace(second = diahorastr[5])
            date.replace
        
        return date
 

if __name__ == "__main__":    
    
  
    # Creates a Class_horario
    Class_horario.read('../data/' 'horario.db')
    
    teste = Class_horario('None','2024/4/17 10:00:00','t14','p14','uc14','s14','NOTA 14') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    
    teste = Class_horario('None','2024/3/4 11:00:00','t1','p1','uc1','s1','NOTA 1') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/5 12:00:00','t2','p2','uc2','s2','NOTA 2') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/6 14:00:00','t3','p3','uc3','s3','NOTA 3') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/7 15:00:00','t4','p4','uc4','s4','NOTA 4') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/8 16:00:00','t5','p5','uc5','s5','NOTA 5') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/9 11:00:00','t6','p6','uc6','s6','NOTA 6') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/10 12:00:00','t7','p7','uc7','s7','NOTA 7') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/11 13:00:00','t8','p8','uc8','s8','NOTA 8') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/12 14:00:00','t9','p9','uc9','s9','NOTA 9') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/13 15:00:00','t10','p10','uc10','s10','NOTA 10') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/14 16:00:00','t11','p11','uc11','s11','NOTA 11') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/15 17:00:00','t12','p12','uc12','s12','NOTA 12') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/16 18:00:00','t13','p13','uc13','s13','NOTA 13') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    teste = Class_horario('None','2024/3/17 19:00:00','t14','p14','uc14','s14','NOTA 14') 
    Class_horario.insert(getattr(teste, Class_horario.att[0]))


    #code,diahora,cod_turma,cod_prof,cod_uc,cod_sala,obs
    Class_horario.insert(getattr(teste, Class_horario.att[0]))
    print(Class_horario.current())
    print(teste)
      
    