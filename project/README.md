# PROYECTO FINAL - CURSO PYTHON - CODERHOUSE

# Sobre el Autor

Mi nombre es Daniela Soler Collao y soy estudiante del curso de Python realizado a través de la plataforma de CoderHouse. Este proyecto es para poner en práctica los conocimientos de todo el curso y crear una página web mediante Django con el objetivo de implementarla para un proyecto de emprendimiento personal familiar.

# Descripción del Proyecto

Este proyecto se realiza para crear una página web de asesoría de Feng-Shui, la cual informa acerca de lo que es el Feng-Shui y muestra distintos servicios que este emprendimiento provee: 
- Asesoría Hogar
- Asesoría Laboral
- 4 Pilares
- Paisajismo
A su vez, presenta una tienda con diversos productos relacionados al Feng-Shui, los cuales se utiizan para armonizar el espacio que se necesite según las condiciones del lugar.

El proyecto presenta 8 apps:
- Home: página principal e implementado el login y sign up
- about: muestra el "quienes somos" 
- servicios: da acceso a los distintos servicios que presenta el emprendimiento.
- hogar, empresa, pilares y paisajismo: muestra información de las diferentes asesorias disponibles.
- tienda: muestra los productos a vender, formulario de contacto y carrito de compras.

A continuación se deja un link con acceso a un video explicativo del funcionamiento de la página web:
`https://youtu.be/BBLdm2BTKh8`

# Especificaciones técnicas

Para poder agregar información a la base de datos, se debe entrar con la cuenta de Administrador. Las apps modificables son: Home y tienda. Los datos para acceder desde `http://127.0.0.1:8000/admin/` son:

- Usuario: `admin`
- Contraseña: `1234`

Ejecutar el archivo requirements.txt para tener todas las librerías necesarias a disposición.

**`pip install -r requirements.txt`**

# Errores conocidos

Tras llenar el formulario de registro de forma incorrecta (por ejemplo, escribir la confirmación de la contraseña mal), se envía igual el registro, lo cual se puede visualizar desde el panel de Administración de Django.

No se encuentra implementado el carrito de compras, ya que no se me ocurrió una forma de realizarlo con los conocimientos actuales.

# Futuras mejoras

- Implementar más opciones en la tienda a modo de búsqueda de productos mediante su categoría asignada.
- En el apartado de tienda también se desea agregar una opción para ver los servicios disponibles para añadir directo al carrito de compras.
- Implementar el carrito de compras para que se encuentre full operativo.
- Añadir una API para contacto directo y consultas por whatsapp.
- Las imágenes del Header se desean implementar de forma más sencilla y que cambien para cada subpágina.
- Mejorar el estilo de la página sin ocupar archivos completos de .css para los apartados utilizados (se utilizaron 4 archivos .css en total) y entender qué es lo necesario para reducir y optimizar el código .css
- Utilizar más frecuentemente un template que funcione como redireccionamiento a las páginas necesarias para mayor legibilidad del código.