import pymysql

class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'



class DevelopmentConfig():
    DEBUG = True
    # MYSQL_HOST = 'localhost'
    # MYSQL_USER = 'root'
    # MYSQL_PASSWORD = '01Hachico'
    # MYSQL_DB = 'mydb'
   
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