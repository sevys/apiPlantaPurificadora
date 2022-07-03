from flask import Flask, flash, jsonify, request, flash
from config import config
#modelos
from models.ModelAdmi import ModelAdministrator
from models.ModelUser import ModelUser
from models.ModelDirection import ModelDirection
from models.ModelProducts import ModelProducts
from models.ModelShopping import ModelShopping
from models.ModelShoppinCart import ModelShoppingCart
#entities
from models.entities.Admi import Administrator
from models.entities.User import User



app = Flask(__name__)

@app.route('/registrarAdministrador', methods=['POST'])
def registrar_administrador():
    try:
        userregister = ModelAdministrator.insertar( request.form['user'], request.form['password'])

        return userregister
    except Exception as ex:
        return 'error ', ex


@app.route('/loginadministrador', methods=['POST'])
def login_administrador():
    user = Administrator(0, request.form['user'], request.form['password'])
    loggedUser = ModelAdministrator.login(user)
    if loggedUser != None:
        if loggedUser.password:
            return ' se logueo el usuario'
        else:
            return 'contraseña incorrecta'
    else:
        flash("usuario no escontrado")
        return 'no existe'

#direccion
@app.route('/registrarDireccion', methods=['POST'])
def registrar_direccion():
    try:
        registrarDireccion = ModelDirection.insertar_direccion(request.form['nombre'], request.form['apellidos'],request.form['codigopostal'], request.form['calle'],
                                request.form['telefono'], request.form['descripcion'], request.form['iduser'])
        return registrarDireccion
    except Exception as ex:
        return ex


@app.route('/eliminarDireccion/<id>', methods=['DELETE'])
def eliminar_direccion(id):
    try:
        eliminarDireccion= ModelDirection.eliminar_direccion(id)
        return eliminarDireccion
    except Exception as ex: 
        return ex


@app.route('/actualizarDireccion/<id>', methods=['PUT'])
def actualizar_direccion(id):
    try:
        actualizar = ModelDirection.actualizar_direccion(id, 
                                 request.form['nombre'], request.form['apellidos'],request.form['codigopostal'], request.form['calle'],
                                request.form['telefono'], request.form['descripcion'], request.form['iduser'])

        return actualizar
    except Exception as ex:
        return ex


@app.route('/obtenerDireccion/<id>', methods=['GET'])
def obtener_direccion_por_usuario(id):
    try:
        obtenerDirecciones = ModelDirection.obtener_direccion_por_id(id)
        print(obtenerDirecciones)
        return obtenerDirecciones
    except Exception as ex:
        return ex

#products
@app.route('/insertarProducto', methods=['POST'])
def insertar_producto():
    try:
        registrarDireccion = ModelProducts.insertar_producto(request.form['nombre'], request.form['precio'],request.form['cantidad'], request.form['descripcion'],)
        return registrarDireccion
    except Exception as ex:
        return ex


@app.route('/eliminarProducto/<id>', methods=['DELETE'])
def eliminar_producto(id):
    try:
        eliminarDireccion= ModelProducts.eliminar_producto(id)
        return eliminarDireccion
    except Exception as ex: 
        return ex


@app.route('/actualizarProducto/<id>', methods=['PUT'])
def actualizar_producto(id):
    try:
        actualizar = ModelProducts.actualizar_producto(id, 
                                 request.form['nombre'], request.form['precio'],request.form['cantidad'], request.form['descripcion'])

        return actualizar
    except Exception as ex:
        return ex


@app.route('/obtenerProductos', methods=['GET'])
def obtener_productos():
    try:
        obtenerProductos = ModelProducts.obtener_productos()
       
        return obtenerProductos
    except Exception as ex:
        return ex

#shopping
@app.route('/insertarCompras', methods=['POST'])
def insertar_compras():
    try:
        registrarDireccion = ModelShopping.insertar_compra(request.form['nombre'], request.form['precio'],request.form['cantidad'], request.form['iduser'])
        return registrarDireccion
    except Exception as ex:
        return ex


@app.route('/eliminarCompra/<id>', methods=['DELETE'])
def eliminar_compra(id):
    try:
        eliminarCompra= ModelShopping.eliminar_compra(id)
        return eliminarCompra
    except Exception as ex: 
        return ex


@app.route('/obtenerCompras/<iduser>', methods=['GET'])
def obtener_productos_por_usuario(iduser):
    try:
        obtenerProductosPorUsuario = ModelShopping.obtener_compra_por_id(iduser)
       
        return obtenerProductosPorUsuario
    except Exception as ex:
        return ex

#carrito de compras
@app.route('/insertarproductoCarrito', methods=['POST'])
def insertar_compras_encarrito():
    try:
        registrarDireccion = ModelShoppingCart.insertar_compra(request.form['nombre'], request.form['precio'],request.form['cantidad'], request.form['iduser'])
        return registrarDireccion
    except Exception as ex:
        return ex

@app.route('/eliminarCarrito/<id>', methods=['DELETE'])
def eliminar_carrito(id):
    try:
        eliminarCarrito= ModelShoppingCart.eliminar_compra(id)
        return eliminarCarrito
    except Exception as ex: 
        return ex


@app.route('/obtenerproductoenCarrito/<iduser>', methods=['GET'])
def obtener_carrito_por_usuario(iduser):
    try:
        obtenerProductosPorUsuario = ModelShoppingCart.obtener_carrito_por_id(iduser)
       
        return obtenerProductosPorUsuario
    except Exception as ex:
        return ex


@app.route('/registerUser', methods=['POST'])
def registar_usuario():
    try:
        
        userRegister = ModelUser.insertar(request.form['user'], request.form['password'], request.form['email'])
        return userRegister
    except Exception as ex:
        return 'error ', ex


@app.route('/loginUser', methods=['POST'])
def login_usuario():
    user = User(0, request.form['user'], request.form['password'])
    loggedUser = ModelUser.login(user)
    if loggedUser != None:
        if loggedUser.password:
            return ' se logueo el usuario'
        else:
            return 'contraseña incorrecta'
    else:
        flash("usuario no escontrado")
        return 'no existe'



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
 