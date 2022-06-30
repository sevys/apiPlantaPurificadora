from config import obtener_conexion
from werkzeug.security import generate_password_hash
from .entities.User import User


class ModelUser():
    @classmethod
    def insertar(self, user, password, email):
        try:
            hashPassword = generate_password_hash(password)
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                    cursor.execute('INSERT INTO users(user, password, email) VALUES (%s, %s, %s)',
                    (user, hashPassword, email))
                
            conexion.commit()
            conexion.close()
            return {'usuario': 'registrado'}
            
        except Exception as ex:
            raise Exception(ex)

    

    @classmethod
    def eliminar_cuenta(id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('DELETE FROM users WHERE iduser = %s', (id,))

        conexion.commit()
        
    

    @classmethod
    def actualizar_cuenta(id, user, password, email):
        password = generate_password_hash(password)
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('UPDATE users SET user = %s, password = %s, email = %s WHERE iduser = %s', 
            (user, password, email, id))
        
        conexion.commit()
        
    

    @classmethod
    def login(self, user):
        try:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                cursor.execute( """SELECT iduser, user, password, email FROM users 
                    WHERE user = '{}'""".format(user.username))
  
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)