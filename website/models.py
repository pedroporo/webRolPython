from website.MongoDB import get_connection
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
    def addDaño(self,daño:str):
        self.daño=daño
    def addDificultad(self,dificultad:int):
        self.dificultad=dificultad
class Hechizo:
    nombre: str
    etiquetas=[]
    accion: TipoAccion
    escuela:Escuelas
    descripcion: str
    dificultades=[]
    def __init__(self,nombre:str,accion:TipoAccion,descripcion:str,escuela:Escuelas) -> None:
        self.nombre=nombre
        self.accion=accion
        self.descripcion=descripcion
        self.escuela=escuela
    def addDificultad(self,dificultad:nivelHechizo):
        self.dificultades.append(dificultad)
    def remDificultad(self,dificultad:nivelHechizo):
        self.dificultades.remove(dificultad)

class HechizoSQLDao:
    hechizos=db.Hecizos
    def addHechizo(Hechizo:Hechizo):
        pass