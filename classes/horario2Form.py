# -*- coding: utf-8 -*-

"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class HorarioForm

"""""
#import datetime
from datetime import datetime

from datetime import timedelta
# Import the generic class
from classes.gclass import Gclass



class Horario2Form(Gclass):
    # Dictionary of objects
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['code','classEvents', 'selectedDiaHora','horaIni','horaFim']
    # Class header title
    header = 'horario to form'
    # field description for use in, for example, in input form
    des = ['code','classEvents', 'selectedDiaHora','horaIni','horaFim']
    # Constructor: Called when an object is instantiated
    def __init__(self, code,classEvents, selectedDiaHora,horaIni,horaFim):
        #Uncomment in case of auto number on
        if code == 'None':
            codes = Horario2Form.getatlist('_code')
            if codes == []:
                code = str(1)
            else:
                code = str(max(map(int,Horario2Form.getatlist('_code'))) + 1)
        # Object attributes
        self.code = code
        self.classEvents = classEvents
        self.selectedDiaHora = self.str2datetimeDiaHora(selectedDiaHora)
        self.horaIni = horaIni
        self.horaFim = horaFim
        self._eventsdiahseleted = []
        
        self.config_horario()
        self.fillMatiz()
        
        
        


        # Add the new object to the Class_horario list
        Horario2Form.obj[code] = self
        Horario2Form.lst.append(code)
#%% property
    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    #classEvents property getter method
    @property
    def classEvents(self):
        return self._classEvents
    # horaIni property getter method
    @property
    def horaIni(self):
        return self._horaIni
    # horaFim property getter method
    @property
    def horaFim(self):
        return self._horaFim
    # selectedDia property getter method
    @property
    def selectedDia(self):
        return self.selectedDiaHora.date()
    # eventsbydiahora property getter method
    @property
    def eventsdiahseleted(self):
        return self._eventsdiahseleted
    
    
    
    
   

#%% setter
    
    # setter methodes
    # code property setter method
    @code.setter
    def code(self, code):
        self._code = code
    # classEvents property setter method
    @classEvents.setter
    def classEvents(self, classEvents):
        self._classEvents = classEvents
    # horaIni property setter method
    @horaIni.setter
    def horaIni(self, horaIni):
        self._horaIni = horaIni
    # horaFim property setter method
    @horaFim.setter
    def horaFim(self, horaFim):
        self._horaFim = horaFim

   


#%% def    


           
       
    def str2datetimeDiaHora(self,datestr):
        
        if type (datestr) == str:
            datestr = datestr.replace("/", ";")
            datestr = datestr.replace("-", ";")
            datestr = datestr.replace(":", ";")
            datestr = datestr.replace(" ", ";")
            
            
            
            try:
                
                diahorastr =list(map(int, datestr.split(";")))
                
                 
                date = datetime(diahorastr[0], diahorastr[1], diahorastr[2])
                if len(diahorastr)>3:
                    date=date.replace(hour = diahorastr[3])
                if len(diahorastr)>4:
                    date=date.replace(minute=  diahorastr[4])
                if len(diahorastr)>5:
                    date=date.replace(second = diahorastr[5])
            except:
                date = datetime.now()
                
            # print('str2datetimeDiaHora', date)
        else:
            date = datestr
        
        date = datetime(date.year, date.month, date.day,date.hour)
        return date
    

    def config_horario(self):
        #dia a mostrar  no horario
        # self.selectedDia
        
    
        #calcular o 1º e ultimo dia da semana que contem o dia
        self.diaInicial = self.selectedDia+timedelta(days=-int(self.selectedDia.strftime("%w")))
        self.diaFinal = self.diaInicial+timedelta(days=+6)
        
        self.colunas=('D','2ª','3ª','4ª','5ª','6ª','S')
        self.colunasdia = list()
        for k in range(7):
            self.colunasdia.append(self.diaInicial+ timedelta(k))
        
    # Fill matiz from class
    def fillMatiz(self):
        
        cs=int(self.selectedDiaHora.strftime("%w"))
        ls=int(self.selectedDiaHora.strftime("%H"))
        
        self.semanaTree = [[''] * 7 for i in range(24)]

        self.horas = []
        for k in range(24):
            self.horas.append(k)
        
        
        for c in range(7):
            dia = self.diaInicial+ timedelta(c)
            for l in range(24):
                self.semanaTree[l][c] = celulaform(l,c,dia,l)
                
        
        for k in self.classEvents.lst:
            evento = self.classEvents.obj[k]
            diaEvento = datetime.strptime(evento.diahora,'%Y-%m-%d %H:%M:%S').date()
            diahEvento = datetime.strptime(evento.diahora,'%Y-%m-%d %H:%M:%S')
            
            if diaEvento >= self.diaInicial and diaEvento <= self.diaFinal:
                
                c=int(diahEvento.strftime("%w"))
                l=int(diahEvento.strftime("%H"))
                if l < self.horaIni:
                    self.horaIni = l
                if l> self.horaFim:
                    self.horaFim = l
                    
                self.semanaTree[l][c].codeevent = evento.code 
                self.semanaTree[l][c].texto = self.text_to_horario(evento) 
                
                if c == cs and l == ls:
                    self._eventsdiahseleted.append([evento.code,str(evento),len(str(evento))])
                    
                
        

      
    def text_to_horario(self,evento):
        texto = f"{evento.cod_uc} - {evento.cod_turma}- {evento.cod_prof}- {evento.cod_sala} "
        #print("--------",texto,"---------")
        return texto
       
    
 
        
        
                
class celulaform():
    def __init__(self,l,c,dia,hora):
        self.cores = {
            0: 'White',
            1: 'GreenYellow',
            2: 'OrangeRed',
            3: 'red'}
        
        self.nevents = -1
        self.l = l
        self.c = c
        self.dia = dia
        self.hora =hora
        self.codeevent = "None"
        self.texto = "" 
        
    # codeevent property getter method
    @property
    def codeevent(self):
        return self._codeevent
    
    # cor property getter method
    @property
    def cor(self):
        if self.nevents in self.cores.keys():
            temp = self.cores[self.nevents]
        else:
            temp = self.cores[len(self.cores)-1]
        
        return temp
    
    
    # codeevent property setter method
  
    @codeevent.setter
    def codeevent(self, codeevent):
        self.nevents += 1
        self._codeevent = codeevent
    
    def __str__(self):
        return f'{self.l} -{self.c} -{self.dia} -{self.hora} -{self.codeevent} -{self.texto} - '
          


#%% Teste    

      
    