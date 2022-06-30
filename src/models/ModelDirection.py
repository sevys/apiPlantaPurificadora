from flask import jsonify
from config import obtener_conexion



class ModelDirection():
    @classmethod
    def insertar_direccion(self, nombre, apellidos, codigoPostal, calle, telefono, descripcion, idUsuario):
        print(type(idUsuario))

        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            print(type(idUsuario))
            cursor.execute('INSERT INTO direction(name, lastName, postalCode, street, phone, descrption, iduser) VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (nombre, apellidos, codigoPostal, calle, telefono, descripcion, idUsuario))
        
        conexion.commit()
        conexion.close()
        return jsonify({'mensaje': "se inserto en la base de datos"})
    

    @classmethod
    def eliminar_direccion(self, id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute('DELETE FROM direction WHERE iddirection = %s', (id,))

        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': "direccion elimando"})


    @classmethod
    def actualizar_direccion(self, id, nombre, apellidos, codigPostal, calle, telefono, descripcion,iduser):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(
                'UPDATE direction SET name = %s, lastName = %s, postalCode = %s, street = %s, phone = %s, descrption = %s, iduser=%s WHERE iddirection = %s', 
            (nombre, apellidos, codigPostal,calle, telefono, descripcion,iduser, id))
        
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': "direccion actualizado"})
    

    @classmethod
    def obtener_direccion_por_id(self,id):
        conexion = obtener_conexion()
        direcciones = None
        with conexion.cursor() as cursor:
            cursor.execute('SELECT name, lastName, postalCode, Street, phone, descrption, iduser FROM direction WHERE iduser = %s', (id,))
            direcciones = cursor.fetchall()
            direc = []
            for fila in direcciones:
                direction = {'name':fila[0],'lastName':fila[1],'postalCode':fila[2],'street':fila[3],'phone':fila[4],'description':fila[5],'iduser':fila[6]}
                direc.append(direction)

        conexion.close()
        
        return jsonify({'direcciones': direc})