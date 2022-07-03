from config import obtener_conexion
from flask import jsonify



class ModelProducts():
    @classmethod
    def insertar_producto(self,nombre, precio, cantidad, descripcion):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('INSERT INTO products(name, price, quantity, description) VALUES (%s, %s, %s, %s)',
            (nombre, precio, cantidad, descripcion))
        
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': "producto insertado"})

    
    @classmethod
    def obtener_productos(self):
        conexion = obtener_conexion()
        direcciones = None

        with conexion.cursor() as cursor:
            cursor.execute('SELECT idproduct, name, price, quantity, description FROM products')
            direcciones = cursor.fetchall()
            direc = []
            for fila in direcciones:
                direction = {'id':fila[0],'Name':fila[1],'price':fila[2],'quantity':fila[3],'description':fila[4]}
                direc.append(direction)

        conexion.close()
        print(direc)
        return jsonify({'productos': direc})
        
    

    @classmethod
    def eliminar_producto(self,id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('DELETE FROM products WHERE idproduct = %s', (id,))

        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': "producto eliminado"})
    


    @classmethod
    def actualizar_producto(self,id, nombre, precio, cantidad, descripcion):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('UPDATE products SET name = %s, price = %s, quantity = %s, description = %s WHERE idproduct = %s', 
            (nombre, precio, cantidad, descripcion, id))
        
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': "producto actualizado"})