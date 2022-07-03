from config import obtener_conexion
from flask import jsonify



class ModelShopping():
    @classmethod
    def insertar_compra(self,nombre, precio, cantidad, iduser):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('INSERT INTO shopping(productName, price, quantity, iduser) VALUES (%s, %s, %s, %s)',
            (nombre, precio, cantidad, iduser))
        
        conexion.commit()
        conexion.close()
        return jsonify({'mensaje': "producto insertado"})

    

    @classmethod
    def eliminar_compra(self,id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('DELETE FROM shopping WHERE idshoppingCart = %s', (id))

        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': "compra eliminado"})
    

    @classmethod
    def obtener_compra_por_id(self,id):
        conexion = obtener_conexion()
        producto = None
        with conexion.cursor() as cursor:
            cursor.execute('SELECT idshoppingCart, productName, price, quantity, iduser FROM shopping WHERE iduser = %s', (id,))
            producto = cursor.fetchall()
            compras = []
            for fila in producto:
                direction = {'id':fila[0],'productName':fila[1],'price':fila[2],'quantity':fila[3],'iduser':fila[4]}
                compras.append(direction)

        conexion.close()
        
        return jsonify({'direcciones': compras})