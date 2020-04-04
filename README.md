# Proyecto_1
En este proyecto es realizar una pagina web que contenga un login, register, logout, busqueda de libros, ver reseñas de los libros y
calificar dichos libros, y se realizara meadiante Python Flask

Mi proyecto cumple con 4 de los 6 requisitos pedidos, mi pagina contiene la interfaz para registrar y ahi almacena a los usuarios en mi BD 
en elephant, tambien esta la inferzar de logearse y para ello consulta los datos de la BD para validar que los usuarios y contraseñas 
existan y puedan entrar la interfaz del usuario, ya en la anterior interfaz aparece una barra de busqueda para que el usuario introduzca
el ISBN, nombre del autor o del libro y con el boton buscar hace la consulta a la BD y si ahi libros con algo de lo anterior los muestra 
todos los resultados en una tabla y todas estas interfaces se encuentran en la carpeta "templates"

El archivo app es como quien dice el nucleo del proyecto ya que contiene: El codigo para logearse con la base de datos, registrarse y que se guarde en la base de datos, busqueda de los libros que estan en la base de datos, y rutas para la verificación de registro, login, perfil y busqueda.

El archivo config para poder usar la base de datos

Tanto el archivo de login y user podrimos decir que son archivos volatiles porque cuando se logea y registra se escribe codigo en ellos pero una vez que terminas este se borra

Y el archivo importar es para subir los libros a la base de datos
