from distutils.debug import DEBUG
import pymysql


class DevelopmentConfig():
    DEBUG = True
   
config = {
    'development': DevelopmentConfig
}

def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='01Hachico',
        db='mydb'
    )