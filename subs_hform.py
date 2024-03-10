# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:15:53 2024

@author: braga
"""
from flask import Flask, render_template, request, session
from classes.docentes import Docentes
from classes.salas import Salas
from classes.turmas import Turmas
from classes.unidadeCurric import UnidadeCurric
from classes.class_horario import Class_horario
from classes.horario2Form import Horario2Form

from datetime import timedelta
from datetime import datetime

prev_option = ""

def gerah(sbl):
    sbl.reset()
    sbl("None", Class_horario, diacalen, 9, 12)
    objh = sbl.obj[sbl.lst[0]]
    return objh
    

def hform(cname=''):
    global prev_option
    global diacalen
    
    cname = 'Class_horario'
    ulogin=session.get("user")
    if (ulogin != None):
        cl = eval(cname)
        sbl = eval("Horario2Form")
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "''":
            diacalen = datetime.today()
            
            #objh = gerah(sbl)
        
        elif prev_option == 'insert' and option == 'save':
            if (cl.auto_number == 1):
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            # if auto_number = 1 the key stays the same
            for i in range(cl.auto_number,len(cl.att)):
                att = cl.att[i]
                setattr(obj, att, request.form[att])
            cl.update(getattr(obj, cl.att[0]))
            #objh = gerah(sbl)
            
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"

            elif option == "delete":
                obj = cl.current()
                cl.remove(obj.code)
                if not cl.previous():
                    cl.first()

            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"

            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option == "previousw":
                diacalen = diacalen + timedelta(days=-6)
                sbl.reset()
                sbl("None", Class_horario, diacalen, 9, 12)
                objh = sbl.obj[sbl.lst[0]]
                print('option == "previous":')
            elif option == "nextw":
                diacalen = diacalen + timedelta(days=6)
                sbl.reset()
                sbl("None", Class_horario, diacalen, 9, 12)
                objh = sbl.obj[sbl.lst[0]]
            elif option == "selcel":
                codev = request.args.get("codev")
                cl.current(codev)
                obj = cl.current()
                diacalen = obj._diahoradate
                
                
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))
        
        print (">>>>>>>>>>>>>>>>>>>>>>>",diacalen,type(diacalen))
        
        objh = gerah(sbl)
        prev_option = option
        obj = cl.current()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
        return render_template("hform.html", butshow=butshow, butedit=butedit,
                        cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                        ulogin=session.get("user"),auto_number=cl.auto_number,
                        objh=objh,selectedcell = diacalen)
    else:
        return render_template("index.html", ulogin=ulogin)

