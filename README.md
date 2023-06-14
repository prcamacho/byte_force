# App de Reserva de Eventos

## Alkemy - Comisión 1 Squad 3

# Índice
* <span><a href="#descripcion">Descripción del Proyecto</a></span>
* <span><a href="#visual"></a></span>
* <span><a href="#modulos">Módulos</a></span>
* <span><a href="#ejecutar">Ejecutar Proyecto</a></span>
* <span><a href="#colaboradores">Colaboradores</a></span>

<h2 id="descripcion">Descripción del Proyecto</h2>
Aplicación web desarrollada en Python con framework Django que permite registrar los servicios que la empresa ofrece, registrar empleados y clientes, poder reservar un servicio para un cliente y visualizar diferentes tipos de listados. También se puede acceder a la información de los servicios a través de un endpoint en donde se podrán consultar todos los servicios disponibles y poder filtrarlos por el id en donde se visualizará el detalle completo del mismo.

<br>
<br>
<br>

<h2 id="ejecutar">Windows</h2>
<h3>Requerimiento Python 3.9 o superior</h3>

python -m venv venv <br />
venv/Scripts/activate <br />
pip install -r requirements.txt <br />
cd src <br />
python manage.py makemigrations <br />
python manage.py migrate <br />
python manage.py runserver <br />

<br>
<br>

<h2 id="modulos">Módulos</h2>
<ul>
<li>API</li>
    <br>


Este módulo proporciona endpoints y funcionalidades para interactuar con la aplicación a través de una interfaz de programación de aplicaciones (API). Aquí se definen las rutas y controladores necesarios para realizar operaciones como registrar servicios, gestionar clientes, empleados y coordinadores.

**Rutas**

- `/api/servicios`: Gestiona los servicios ofrecidos por la empresa.
- `/api/servicios/<int:id>`: Obtiene información detallada de un servicio específico.
- `/api/clientes`: Gestiona los clientes registrados.
- `/api/clientes/<int:id>`: Obtiene información detallada de un cliente específico.
- `/api/empleados`: Gestiona los empleados de la empresa.
- `/api/empleados/<int:id>`: Obtiene información detallada de un empleado específico.
- `/api/coordinadores`: Gestiona los coordinadores de eventos.
- `/api/coordinadores/<int:id>`: Obtiene información detallada de un coordinador específico.

    <br>
    <br>
    <br>
    
<li>Clientes</li>
<br>

Este módulo proporciona endpoints y funcionalidades relacionadas con la gestión de clientes en la aplicación.

**Rutas**

- `/clientes/`: Muestra un listado de clientes.
- `/clientes/nuevo/`: Permite agregar un nuevo cliente.
- `/clientes/desactivar/<int:id>/`: Permite desactivar un cliente específico.
- `/clientes/activar/<int:id>/`: Permite activar un cliente específico.
- `/clientes/listado/`: Muestra un listado de clientes (similar a la ruta raíz).
- `/clientes/modificar/<int:id>/`: Permite modificar los datos de un cliente específico.
    
    <br>
    <br>
    <br>

<li>Coordinadores</li>
<br>


Este módulo proporciona endpoints y funcionalidades relacionadas con la gestión de coordinadores en la aplicación.

**Rutas**

- `/coordinadores/`: Muestra un listado de coordinadores.
- `/coordinadores/activar/<int:id>/`: Permite activar un coordinador específico.
- `/coordinadores/desactivar/<int:id>/`: Permite desactivar un coordinador específico.
- `/coordinadores/listado/`: Muestra un listado de coordinadores (similar a la ruta raíz).
- `/coordinadores/nuevo/`: Permite agregar un nuevo coordinador.
- `/coordinadores/modificar/<int:id>`: Permite modificar los datos de un coordinador específico.

    <br>
    <br>
    <br>

<li>Empleados</li>
<br>



Este módulo proporciona endpoints y funcionalidades relacionadas con la gestión de empleados en la aplicación.

**Rutas**

- `/empleados/`: Muestra un listado de empleados.
- `/empleados/nuevo/`: Permite agregar un nuevo empleado.
- `/empleados/modificar/<int:id>`: Permite modificar los datos de un empleado específico.
- `/empleados/activar/<int:id>`: Permite activar un empleado específico.
- `/empleados/desactivar/<int:pk>`: Permite desactivar un empleado específico.
- `/empleados/listado/`: Muestra un listado de empleados (similar a la ruta raíz).
    
    <br>
    <br>
    <br>

<li>Reservas</li>
    <br>

Este módulo proporciona endpoints y funcionalidades relacionadas con la gestión de reservas en la aplicación.

**Rutas**

- `/reservas/`: Muestra un listado de reservas.
- `/reservas/nuevo/`: Permite agregar una nueva reserva.
- `/reservas/modificar/<int:id>/`: Permite modificar los datos de una reserva específica.
- `/reservas/listado/`: Muestra un listado de reservas (similar a la ruta raíz).
- `/reservas/eliminar/<int:id>/`: Permite eliminar una reserva específica.

    <br>
    <br>
    <br>

<li>Servicios</li>
    <br>

Este módulo proporciona endpoints y funcionalidades relacionadas con la gestión de servicios en la aplicación.

**Rutas**

- `/servicios/`: Muestra un listado de servicios.
- `/servicios/nuevo/`: Permite agregar un nuevo servicio.
- `/servicios/listado/`: Muestra un listado de servicios (similar a la ruta raíz).
- `/servicios/desactivar/<int:pk>`: Permite desactivar un servicio específico.
- `/servicios/activar/<int:pk>`: Permite activar un servicio específico.
- `/servicios/modificar/<int:id>/`: Permite modificar los datos de un servicio específico.

    <br>
    <br>
    <br>
<li>Menu Clientes</li>

Este módulo proporciona endpoints y funcionalidades relacionadas con el menú en la aplicación.

**Rutas**

- `/menu/registro/`: Permite registrar un nuevo cliente.
- `/menu/modificar/<int:id>/`: Permite modificar los datos de un cliente específico.
- `/menu/login`: Permite iniciar sesión como cliente.
- `/menu/logout/`: Permite cerrar sesión como cliente.
- `/menu/`: Muestra las reservas del usuario cliente.

</ul>
<br>
<br>
<br>





<h2 id="colaboradores">Colaboradores</h2>

* Mendez, Eusebio
* Camacho, Pablo
* Zelaya, Fernando
* Chachagua, Daniel
* Paredez, Gustavo