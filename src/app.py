from flask import Flask
from config import config
from flask_mysqldb import MySQL



app = Flask(__name__)

conexion = MySQL(app)


@app.route('/products')
def get_products():
    try:
        return 'ok'

    except Exception as ex:
        return 'error ', ex


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
 