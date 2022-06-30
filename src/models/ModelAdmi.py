from .entities.Admi import Administrator

from werkzeug.security import generate_password_hash
from config import obtener_conexion


class ModelAdministrator():

    @classmethod
    def login(self, user):
        try:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                cursor.execute( """SELECT idadministrator, user, password FROM administrator 
                    WHERE user = '{}'""".format(user.username))
  
            row = cursor.fetchone()
            if row != None:
                user = Administrator(row[0], row[1], Administrator.check_password(row[2], user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, fullname FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return Administrator(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def insertar(self, user, password):
        try:
            hashPassword = generate_password_hash(password)
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                    cursor.execute('INSERT INTO administrator(user, password) VALUES (%s, %s)',
                    (user, hashPassword))
                
            conexion.commit()
            conexion.close()
            return {'usuario': 'registrado'}
            
        except Exception as ex:
            raise Exception(ex)

