"""
@author: António Brito / Carlos Bragança
(2024)
#objective: app.py

"""""

'''
no PC deve ter o ficheiro datafile.py com

filename = 'data/'

'''

from flask import Flask, render_template, request, session
from datafile import filename
from classes.turmas import Turmas
from classes.docentes import Docentes
from classes.salas import Salas
from classes.unidadeCurric import UnidadeCurric
from classes.class_horario import Class_horario

from classes.userlogin import Userlogin



app = Flask(__name__)

Docentes.read(filename + 'horario.db')
Salas.read(filename + 'horario.db')
Turmas.read(filename + 'horario.db')
UnidadeCurric.read(filename + 'horario.db')
Class_horario.read(filename + 'horario.db')
Userlogin.read(filename + 'horario.db')
prev_option = ""
app.secret_key = 'BAD_SECRET_KEY'

import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub
import subs_hform as gfhsub

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
     return gfsub.gform(cname)

    
@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    return gfTsub.gformT(cname)

@app.route("/hform/<cname>", methods=["post","get"])
def hform(cname=''):
    return gfhsub.hform(cname)
        
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname=""):
    global prev_option
    tlist = cname.split('_')
    cnames = tlist[0]
    scname = tlist[1]
    ulogin=session.get("user")
    if (ulogin != None):
        cl = eval(cnames)
        sbl = eval(scname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
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
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                lines = sbl.getlines(getattr(obj, cl.att[0]))
                for line in lines:
                    sbl.remove(line)
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
            elif option[:6] == "delrow":
                row = int(option.split("_")[1])
                obj = cl.current()
                lines = sbl.getlines(getattr(obj, cl.att[0]))
                print(row,lines[row])
                sbl.remove(lines[row])
            elif option == "addrow":
                butshow = "disabled"
                butedit = "disabled"
            elif option == "saverow":
                obj = cl.current()
                strobj = getattr(obj, cl.att[0])
                
                select = request.form.get('_product_code')
                strobj += ";"+str(select)
                
                for i in range(2,len(sbl.att)):
                    strobj += ";" + request.form[sbl.att[i]]
                    
                print(strobj)    
                objl = sbl.from_string(strobj)
                code = str(getattr(objl, sbl.att[0])) + str(getattr(objl, sbl.att[1]))
                #print(code, objl)
                sbl.insert(code)
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user")) 
        prev_option = option
        obj = cl.current()
        headers = list()
        objl = list()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            for att in cl.att:
                obj[att] = ""
        else:
            for i in range(1, len(sbl.att)): 
                    headers.append(sbl.att[i][1:])        
            lines = sbl.getlines(getattr(obj, cl.att[0])) 
            for line in lines:
                objl.append(sbl.obj[line])
        return render_template("subform.html", butshow=butshow, butedit=butedit,
                    cname=cname, obj=obj,att=cl.att,header=cl.header,des=cl.des,
                    ulogin=session.get("user"),objl=objl,headerl=sbl.header,
                    desl=sbl.des, attl=sbl.att, auto_number=cl.auto_number)
    else:
        return render_template("index.html", ulogin=ulogin)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True,port=7000)