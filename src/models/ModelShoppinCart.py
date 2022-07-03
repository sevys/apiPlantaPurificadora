from config import obtener_conexion
from flask import jsonify



class ModelShoppingCart():
    @classmethod
    def insertar_compra(self,nombre, precio, cantidad, iduser):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('INSERT INTO shoppingcart(productName, price, quantity, iduser) VALUES (%s, %s, %s, %s)',
            (nombre, precio, cantidad, iduser))
        
        conexion.commit()
        conexion.close()
        return jsonify({'mensaje': "producto insertado"})


    @classmethod
    def eliminar_compra(self, id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('DELETE FROM shoppingcart WHERE idshoppingCart = %s', (id,))

        conexion.commit()
        conexion.close()
        return jsonify({'mensaje': "producto insertado"})
    
    
    @classmethod
    def actualizar_compra(self, id, nombre, precio, cantidad, iduser):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('UPDATE shoppingcart SET productName = %s, price = %s, quantity = %s, iduser = %s WHERE idshoppingCart = %s', 
            (nombre, precio, cantidad, iduser, id))
        
        conexion.commit()
        conexion.close()
        return jsonify({'mensaje': "carrito actualizado"})
    

    @classmethod
    def obtener_carrito_por_id(self,id):
        conexion = obtener_conexion()
        producto = None
        with conexion.cursor() as cursor:
            cursor.execute('SELECT idshoppingCart, productName, price, quantity, iduser FROM shoppingcart WHERE iduser = %s', (id,))
            producto = cursor.fetchall()
            compras = []
            for fila in producto:
                direction = {'id':fila[0],'productName':fila[1],'price':fila[2],'quantity':fila[3],'iduser':fila[4]}
                compras.append(direction)

        conexion.close()
        
        return jsonify({'productos de carrito': compras})