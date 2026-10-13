# MiniCore de Ventas – Arquitectura MVC con Flask

**Proyecto de Ingeniería Web | Semana 4 – MVC Semestres Pasados**

## 1. Descripción del proyecto

MiniCore de Ventas es una aplicación web desarrollada con Python y el framework Flask, utilizando la arquitectura Modelo-Vista-Controlador (MVC).

Su objetivo principal es consultar las ventas realizadas por diferentes vendedores, calcular automáticamente las comisiones correspondientes y permitir la búsqueda de resultados mediante un rango de fechas.

El proyecto se basa en un ejercicio de semestres anteriores, el cual fue implementado, configurado, probado localmente y desplegado en la nube utilizando Render.

## 2. Objetivo

Aplicar los conocimientos de arquitectura MVC mediante la implementación de una aplicación web funcional, utilizando Flask, SQLAlchemy, SQLite, HTML, CSS y JavaScript.

Se busca comprender la separación entre modelos, vistas y controladores, la comunicación con la base de datos y el despliegue de una aplicación web en un servidor remoto.

## 3. Tecnologías utilizadas

| Tecnología | Función |
|---|---|
| Python | Lenguaje de programación principal |
| Flask | Framework de desarrollo web |
| SQLAlchemy | Gestión de modelos y consultas a la base de datos |
| SQLite | Almacenamiento de vendedores, ventas y reglas |
| HTML y Jinja2 | Estructura y presentación de las vistas |
| CSS | Diseño visual de la interfaz |
| JavaScript | Validación de fechas del formulario |
| Git y GitHub | Control de versiones y almacenamiento del código |
| Gunicorn | Servidor WSGI para producción |
| Render | Plataforma de despliegue en la nube |
| VS Code | Entorno de desarrollo |

## 4. Arquitectura MVC

La aplicación utiliza una estructura basada en Modelo-Vista-Controlador para separar las responsabilidades del sistema.

### Modelo (Model)

Los modelos representan las entidades de la base de datos y permiten realizar consultas utilizando SQLAlchemy.

- `vendedor.py`: define los vendedores y su relación con las ventas.
- `venta.py`: almacena el monto, fecha y vendedor asociado a cada venta.
- `regla.py`: define los montos mínimos y porcentajes aplicables a las comisiones.

### Vista (View)

La vista es la parte de la aplicación con la que interactúa el usuario.

- `base.html`: plantilla principal con la estructura HTML.
- `index.html`: formulario de fechas y tabla de resultados.
- `style.css`: estilos visuales de la aplicación.

Las plantillas utilizan Jinja2 para mostrar los resultados enviados desde Flask.

### Controlador (Controller)

El archivo `controllers/venta_controller.py` contiene la lógica principal del MiniCore.

Sus responsabilidades son:

1. Recibir las fechas ingresadas por el usuario.
2. Consultar los vendedores registrados.
3. Obtener las ventas correspondientes al rango seleccionado.
4. Sumar los montos de ventas por vendedor.
5. Seleccionar la regla de comisión correspondiente.
6. Calcular el valor de la comisión.
7. Enviar los resultados a la vista HTML.

## 5. Funcionamiento del MiniCore

El MiniCore principal consiste en el cálculo automático de comisiones de vendedores según sus ventas acumuladas.

### Proceso de cálculo

1. El usuario ingresa una fecha inicial y una fecha final.
2. El sistema recibe los datos a través del formulario.
3. El controlador consulta las ventas registradas dentro del período seleccionado.
4. Se calcula el total vendido por cada vendedor.
5. Se consultan las reglas de comisión, ordenadas de mayor a menor monto mínimo.
6. Se selecciona la primera regla cuyo monto mínimo sea alcanzado por el total vendido.
7. Se multiplica el total de ventas por el porcentaje establecido.
8. Finalmente, se presenta una tabla con los resultados.

**Fórmula utilizada:**

Comisión = Total de ventas × Porcentaje de comisión

**Ejemplo:**

Un vendedor registra ventas acumuladas por $800 y se le aplica una comisión del 10 %.

Comisión = $800 × 0,10 = $80

La aplicación mostrará el nombre del vendedor, el total vendido, el porcentaje asignado y la comisión calculada.

## 6. Base de datos

Se utiliza SQLite como sistema de gestión de base de datos.

El proyecto cuenta con tres tablas principales:

**Vendedores**
- `id`: identificador único.
- `nombre`: nombre del vendedor.

**Ventas**
- `id`: identificador único.
- `fecha_venta`: fecha de la transacción.
- `vendedor_id`: referencia al vendedor.
- `cuota_monto`: monto de la venta.

**Reglas**
- `id`: identificador único.
- `monto_minimo`: valor mínimo para aplicar la regla.
- `porcentaje_comision`: porcentaje correspondiente.

La relación entre vendedores y ventas es de uno a muchos (1:N), ya que un vendedor puede registrar varias ventas.

Las reglas de comisión se consultan para determinar qué porcentaje se aplica a cada total de ventas.

El archivo `data.sql` contiene las instrucciones para crear las tablas e insertar los registros iniciales de prueba.

## 7. ¿Cómo se implementó el proyecto?

### Etapa 1. Obtención del repositorio

Se utilizó como base un proyecto MiniCore desarrollado en un semestre anterior.

Se realizó un Fork del repositorio original hacia una cuenta propia de GitHub y posteriormente se clonó en el computador para trabajar desde Visual Studio Code.

### Etapa 2. Preparación del entorno

Se instaló Python y se comprobó el funcionamiento de pip.

Posteriormente, se creó un entorno virtual llamado `venv` para administrar las dependencias del proyecto.

Se instalaron las librerías mediante el archivo `requirements.txt`.

### Etapa 3. Configuración de la base de datos

Se revisó el archivo `app.py` y se identificó una diferencia entre la ruta de conexión de SQLAlchemy y la ruta de creación del archivo SQLite.

Para corregirlo, se modificó la configuración utilizando `pathlib.Path`, obteniendo una ruta absoluta basada en la ubicación de `app.py`.

De esta manera, la aplicación utiliza el mismo archivo `db.sqlite3` tanto para inicializar la base de datos como para consultar la información.

También se conservó la inicialización automática de la base de datos mediante las instrucciones SQL de `data.sql`.

### Etapa 4. Ejecución local

Se inició el servidor de Flask mediante el comando:

`python app.py`

La aplicación fue abierta desde el navegador utilizando la dirección:

`http://127.0.0.1:5000/`

Se comprobó que la interfaz cargara y mostrara la información registrada.

### Etapa 5. Pruebas funcionales

Se realizaron pruebas con los filtros de fechas de mayo, junio y julio de 2025.

Se verificó el funcionamiento de:

- Visualización de vendedores.
- Consulta de ventas.
- Filtro por fechas.
- Cálculo automático de comisiones.
- Presentación de los resultados en la tabla.

### Etapa 6. Control de versiones

Se configuró `.gitignore` para excluir archivos locales e innecesarios, como el entorno virtual, archivos temporales y la base de datos SQLite.

Posteriormente, se registraron los cambios mediante Git y se subieron al repositorio personal de GitHub.

### Etapa 7. Despliegue en Render

Se creó un servicio web en Render conectado al repositorio de GitHub.

La configuración utilizada fue:

- **Language:** Python 3
- **Branch:** main
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Plan:** Free

Render descargó el proyecto, instaló las dependencias y ejecutó la aplicación mediante Gunicorn.

El despliegue finalizó correctamente, con estado `Live` y respuestas HTTP 200.

Se comprobó que la aplicación estuviera disponible públicamente en internet y que los filtros funcionaran.

## 8. Instalación local

Para ejecutar el proyecto en Windows:

**1. Clonar el repositorio**

```bash
git clone https://github.com/NaimC06/MiniCore-Ventas.git
cd MiniCore-Ventas
```

**2. Crear el entorno virtual**

```bash
python -m venv venv
```

**3. Activar el entorno virtual en PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

**4. Instalar las dependencias**

```bash
python -m pip install -r requirements.txt
```

**5. Ejecutar la aplicación**

```bash
python app.py
```

**6. Abrir en el navegador**

http://127.0.0.1:5000/

Si la base de datos no existe, la aplicación intenta crearla utilizando los datos iniciales definidos en `data.sql`.

## 9. Despliegue en la nube

La aplicación se encuentra publicada en Render.

**Aplicación web:**

https://minicore-ventas-4old.onrender.com/

**Repositorio GitHub:**

https://github.com/NaimC06/MiniCore-Ventas

En la modalidad gratuita de Render, la instancia puede suspenderse por inactividad y demorar en responder a la primera solicitud.

SQLite utiliza almacenamiento local, que no es persistente entre determinados reinicios o despliegues de Render. En esta implementación, la aplicación puede recrear los datos iniciales de ejemplo. Para un entorno de producción que necesite conservar nuevas transacciones, sería recomendable utilizar una base de datos persistente.

## 10. Resultados y conclusiones

Se logró implementar y ejecutar una aplicación web basada en MVC, comprendiendo la separación entre los componentes del sistema.

El ejercicio permitió aplicar conceptos de programación backend, bases de datos, formularios HTML, cálculos de negocio y despliegue en la nube.

Además, se reforzó el uso de GitHub para el control de versiones y Render para la publicación de aplicaciones Python.

**Resultado final:** una aplicación MiniCore funcional, con cálculo de comisiones, consultas por fechas y acceso desde una dirección pública en internet.

## 11. Referencias y créditos

Este trabajo es una adaptación académica de un proyecto desarrollado en un semestre anterior, utilizado como referencia para la actividad MVC de Ingeniería Web.

**Repositorio original:**

https://github.com/JimmyAlbarrac1n/MiniCore_Ventas

**Video de referencia:**

https://www.youtube.com/watch?v=IMt2Gwjr4sE

**Implementación y configuración realizada por:**

Naim Cabrera – Ingeniería en Software, UDLA.