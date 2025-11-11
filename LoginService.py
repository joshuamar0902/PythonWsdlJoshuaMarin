from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import mysql.connector # 1. Importamos el conector de MySQL
# import psycopg2 # -> Ya no lo usamos

class loginService(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Unicode)
    def login(ctx, username, password):
        
        conn = None
        cursor = None # Definimos cursor aquí para el 'finally'
        
        # --- Credenciales de MySQL ---
        DB_HOST = "127.0.0.1"
        DB_NAME = "mi_proyecto_soap"
        DB_USER = "root" # (usualmente 'root' en local)
        DB_PASS = "Piolin09"
        
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            
            # 3. Crear cursor
            cursor = conn.cursor()
            
            # 4. Misma consulta SQL (MySQL usa %s para parámetros)
            # Asumimos que la columna se llama 'password' (y guarda texto plano)
            sql = "SELECT password FROM usuarios WHERE username = %s"
            
            # 5. Ejecutar la consulta de forma segura
            cursor.execute(sql, (username,))
            
            # 6. Obtener el resultado
            result = cursor.fetchone()
            
            if result:
                # El usuario existe, ahora verificamos la contraseña
                stored_password = result[0] # La contraseña en texto plano de la BD

                # --- Verificación INSEGURA (como pediste) ---
                if stored_password == password:
                    return f"Bienvenido, {username}"
                else:
                    return "Credenciales incorrectas"
                
            else:
                # Usuario no encontrado
                return "Credenciales incorrectas"

        except (Exception, mysql.connector.Error) as error: # 7. Manejo de error de MySQL
            print(f"Error al conectar o consultar la base de datos: {error}")
            return "Error en el servidor"
            
        finally:
            # 8. Cerrar la conexión y el cursor
            if cursor:
                cursor.close()
            if conn:
                conn.close()


application = Application(
    [loginService],
    tns='mi.namespace',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8001, WsgiApplication(application))
    print("Servicio SOAP en http://0.0.0.0:8001")
    server.serve_forever()