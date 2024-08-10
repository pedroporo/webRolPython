from flask import Blueprint,render_template,request,jsonify
import json
from website.models import *
vistas=Blueprint('vistas',__name__)

@vistas.route('/')
def home():
    user_details_json=request.cookies.get('user_details_json')
    if user_details_json is not None:
        user_details = json.loads(user_details_json)
        return render_template("home.html",user=user_details)
    return render_template("home.html",user=user_details_json)
@vistas.route('/hechizos')
def hechizos():
    user_details_json=request.cookies.get('user_details_json')
    user_details = json.loads(user_details_json)
    hechizos=HechizoSQLDao.findAll(self=HechizoSQLDao)
    return render_template("hechizos.html",user=user_details,hechizos=hechizos)

@vistas.route('/hechizosAdd' , methods=['GET', 'POST'])
def hechizosAdd():
    #print(len(HechizoSQLDao.findAll(self=HechizoSQLDao)))
    #for documento in HechizoSQLDao.hechizosDB.find({}):
    #        print(documento)
    if request.method == 'POST':
        nombre_hechizo=request.form['Nombre_Hechizo']
        accion=request.form['Accion']
        escuela=request.form['Escuela']
        descripcion_hechizo=request.form['Descripcion_Hechizo']
        magia=Hechizo(id=len(HechizoSQLDao.findAll(self=HechizoSQLDao))+1,nombre=nombre_hechizo,accion=accion,descripcion=descripcion_hechizo,escuela=escuela)
        
        nombreDificultadBase=request.form['Nombre_Dificultad_Base']
        costeBasico=request.form['Coste_Basico']
        descripcionDificultadBase=request.form['Descripcion_dificultad_Base']
        dañoBasico=request.form['Daño_Basico']
        dificultadBasica=request.form['Dificultad_Basica']
        nivelBasico=nivelHechizo(nombre=nombreDificultadBase,coste=costeBasico,descripcion=descripcionDificultadBase)
        if dañoBasico != '':
            nivelBasico.addDaño(daño=dañoBasico)
        if dificultadBasica != '':
            nivelBasico.addDificultad(dificultad=dificultadBasica)

        nombreDificultadMediano=request.form['Nombre_Dificultad_Alzado']
        costeMediano=request.form['Coste_Mediano']
        descripcionDificultadMediano=request.form['Descripcion_dificultad_Mediana']
        dañoMediano=request.form['Daño_Mediano']
        dificultadMediana=request.form['Dificultad_Mediana']
        nivelMediana=nivelHechizo(nombre=nombreDificultadMediano,coste=costeMediano,descripcion=descripcionDificultadMediano)
        if dañoMediano != '':
            nivelMediana.addDaño(daño=dañoMediano)
        if dificultadMediana != '':
            nivelMediana.addDificultad(dificultad=dificultadMediana)
        
        nombreDificultadAvanzado=request.form['Nombre_Dificultad_Arcano']
        costeAvanzado=request.form['Coste_Avanzado']
        descripcionDificultadAvanzada=request.form['Descripcion_dificultad_Avanzada']
        dañoAvanzado=request.form['Daño_Avanzado']
        dificultadAvanzada=request.form['Dificultad_Avanzada']
        nivelAvanzado=nivelHechizo(nombre=nombreDificultadAvanzado,coste=costeAvanzado,descripcion=descripcionDificultadAvanzada)
        if dañoAvanzado != '':
            nivelAvanzado.addDaño(daño=dañoAvanzado)
        if dificultadAvanzada != '':
            nivelAvanzado.addDificultad(dificultad=dificultadAvanzada)
        print(nivelBasico)
        magia.addDificultad(dificultad=nivelBasico)
        magia.addDificultad(dificultad=nivelMediana)
        magia.addDificultad(dificultad=nivelAvanzado)
        
        HechizoSQLDao.add(self=HechizoSQLDao,hechizo=magia,dif1=nivelBasico,dif2=nivelMediana,dif3=nivelAvanzado)
        

    user_details_json=request.cookies.get('user_details_json')
    user_details = json.loads(user_details_json)
    return render_template("hechizos_form.html",user=user_details,acciones=TipoAccion,escuelas=Escuelas)