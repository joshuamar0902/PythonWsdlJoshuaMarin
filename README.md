# Proyecto: Web Service SOAP con Python y MySQL

Este es un proyecto simple que demuestra cómo crear un servicio web SOAP en Python usando la librería `spyne`. El servicio se conecta a una base de datos MySQL para validar las credenciales de un usuario.

El repositorio de este proyecto es: `https://github.com/joshuamar0902/PythonWsdlJoshuaMarin.git`

---

## ⚙️ Tecnologías Usadas

* **Python 3.8**
* **Spyne**: Para crear el servidor SOAP y el WSDL.
* **MySQL**: Como base de datos para almacenar usuarios.
* **mysql-connector-python**: El driver para conectar Python con MySQL.
* **Postman**: Para probar el servicio.

---

## 🚀 Cómo Empezar

### 1. Requisitos Previos

* Tener Python 3.8 (o superior) instalado.
* Tener un servidor MySQL (como XAMPP o MySQL Workbench) corriendo.

### 2. Instalación

1.  Clona el repositorio:
    ```bash
    git clone [https://github.com/joshuamar0902/PythonWsdlJoshuaMarin.git](https://github.com/joshuamar0902/PythonWsdlJoshuaMarin.git)
    cd PythonWsdlJoshuaMarin
    ```
2.  Crea y activa un entorno virtual (recomendado):
    ```bash
    # En Windows
    python -m venv venv
    venv\Scripts\activate
    ```
3.  Instala las dependencias:
    ```bash
    pip install spyne mysql-connector-python
    ```

### 3. Configuración de la Base de Datos

Antes de ejecutar el script, debes tener tu base de datos lista.

1.  Crea una base de datos (puedes llamarla `mi_proyecto_soap` o como la llames en tu script).
2.  Crea la tabla `usuarios` e inserta un usuario de prueba.

Puedes usar este script SQL en MySQL Workbench:

```sql
CREATE DATABASE mi_proyecto_soap;
USE mi_proyecto_soap;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);
