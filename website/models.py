from website.MongoDB import get_connection
from abc import ABCMeta,abstractmethod
db=get_connection()
class Personaje:
    puntos=29
    nombre=""
    def __init__(self,id_creador):
        self.owner_id=id_creador
    






from enum import Enum
class TipoAccion(Enum):
    PRINCIPAL='Principal'
    SECUNDARIA='Secundaria'
    REACCION='Reacción'
    GRATUITA='Gratuita'
    PASIVA='Pasiva'
    MANTENIDA='Mantenida'
    ESPECIAL='Especial'

class Escuelas(Enum):
    GENERALES='General'
    FIRMAMENTO='Firmamento'
    LUZ='Luz'
    GUERRA='Guerra'
    FUEGO='Fuego'
    MASCARA='La Mascara'
    ABISMO='Abismo'
    GRANMADRE='Gran Madre'
    TIERRA='Tierra'

class nivelHechizo:
    nombre:str
    coste:int
    descripcion:str
    daño:str
    dificultad:int
    def __init__(self,nombre:str,coste:int,descripcion:str) -> None:
        self.nombre=nombre
        self.coste=coste
        self.descripcion=descripcion
        self.daño=""
        self.dificultad=0
    def addDaño(self,daño:str):
        self.daño=daño
    def addDificultad(self,dificultad:int):
        self.dificultad=dificultad
class Hechizo:
    id:int
    nombre: str
    etiquetas=[]
    accion: TipoAccion
    escuela:Escuelas
    descripcion: str
    dificultades=[]
    def __init__(self,id:int,nombre:str,accion:TipoAccion,descripcion:str,escuela:Escuelas) -> None:
        self.id=id
        self.nombre=nombre
        self.accion=accion
        self.descripcion=descripcion
        self.escuela=escuela
    def addDificultad(self,dificultad:nivelHechizo):
        self.dificultades.append(dificultad)
    def remDificultad(self,dificultad:nivelHechizo):
        self.dificultades.remove(dificultad.getDificultad)
    def getDificultades(self):
        a=[]
        for dificultad in self.dificultades:
            
            a.append(dificultad)
        return a

class HechizoDAO(metaclass=ABCMeta):
    @abstractmethod
    def findAll(self):
        pass
    @abstractmethod
    def findAllE(self,escuela:Escuelas):
        pass
    @abstractmethod
    def findAllA(self,accion:TipoAccion):
        pass
    @abstractmethod
    def add(self,hechizo:Hechizo):
        pass
    @abstractmethod
    def update(self,hechizo:Hechizo):
        pass
    @abstractmethod
    def remove(self,hechizo:Hechizo):
        pass
class HechizoSQLDao(HechizoDAO):
    hechizosDB=db['Hechizos']
    def findAll(self):
        todos=[]
        for documento in self.hechizosDB.find({}):
            todos.append(self.pasarHechizo(documento))
        return todos
    def findAllE(self,escuela:Escuelas):
        busqueda={"escuela":escuela.value}
        todos=[documento for documento in self.hechizosDB.find(busqueda)]
        return todos
    def findAllA(self,accion:TipoAccion):
        busqueda={"accion":accion.value}
        todos=[documento for documento in self.hechizosDB.find(busqueda)]
        return todos
    def add(self, hechizo: Hechizo, dif1:nivelHechizo, dif2:nivelHechizo, dif3:nivelHechizo):
        
        dbh={
            "id":hechizo.id, 
            "nombre": hechizo.nombre,
            "etiquetas":hechizo.etiquetas,
            "accion":hechizo.accion,
            "escuela":hechizo.escuela,
            "descripcion":hechizo.descripcion,
            "dificultades":[
                {
                    "nombre": dif1.nombre,
                    "coste":dif1.coste,
                    "descripcion":dif1.descripcion,
                    "daño":dif1.daño,
                    "dificultad":dif1.dificultad
                },
                {
                    "nombre": dif2.nombre,
                    "coste":dif2.coste,
                    "descripcion":dif2.descripcion,
                    "daño":dif2.daño,
                    "dificultad":dif2.dificultad
                },
                {
                    "nombre": dif3.nombre,
                    "coste":dif3.coste,
                    "descripcion":dif3.descripcion,
                    "daño":dif3.daño,
                    "dificultad":dif3.dificultad
                }
            ]
            }
        return self.hechizosDB.insert_one(dbh)
    def update(self,hechizo:Hechizo, dif1:nivelHechizo, dif2:nivelHechizo, dif3:nivelHechizo):
        querry={"id":hechizo.id}
        valoresNuevos={ "$set": {
            "nombre": hechizo.nombre,
            "etiquetas":hechizo.etiquetas,
            "accion":hechizo.accion,
            "escuela":hechizo.escuela,
            "descripcion":hechizo.descripcion,
            "dificultades":[
                {
                    dif1.nombre: dif1.nombre,
                    "coste":dif1.coste,
                    "descripcion":dif1.descripcion,
                    "daño":dif1.daño,
                    "dificultad":dif1.dificultad
                },
                {
                    dif2.nombre: dif2.nombre,
                    "coste":dif2.coste,
                    "descripcion":dif2.descripcion,
                    "daño":dif2.daño,
                    "dificultad":dif2.dificultad
                },
                {
                    dif3.nombre: dif3.nombre,
                    "coste":dif3.coste,
                    "descripcion":dif3.descripcion,
                    "daño":dif3.daño,
                    "dificultad":dif3.dificultad
                }
            ]
            } }
        return self.hechizosDB.update_one(querry,valoresNuevos)
    def pasarHechizo(document):
        hechizo = Hechizo(
            id=document['id'],
            nombre=document['nombre'],
            accion=TipoAccion[document['accion']],
            descripcion=document['descripcion'],
            escuela=Escuelas[document['escuela']]
        )
        for dificultad in document['dificultades']:
            nivel=nivelHechizo(
                nombre=dificultad['nombre'],
                coste=dificultad['coste'],
                descripcion=dificultad['descripcion']
                )
            nivel.addDaño(dificultad['daño'])
            nivel.addDificultad(dificultad['dificultad'])
            hechizo.addDificultad(dificultad=nivel)
        return hechizo