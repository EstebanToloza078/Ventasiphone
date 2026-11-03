from waitress import serve
from app import app

if __name__ == '__main__':
    print("Servidor corriendo en http://0.0.0.0:5000")
    print("Acceso local: http://127.0.0.1:5000")
    print("Acceso desde red: http://192.168.1.14:5000")
    serve(app, host='0.0.0.0', port=5000, threads=8)
