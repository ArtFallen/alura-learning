""" Un bucle es una estructura de control que permite repetir 
un bloque de código varias veces. En Python, 
existen varios tipos de bucles, como el bucle for 
y el bucle while.

se usan para iterar sobre una secuencia 
(como una lista, una tupla, un diccionario, un conjunto o una cadena) 
o para ejecutar un bloque de código un número específico 
de veces.

se usan de la siguiente forma:
for variable in secuencia:
    # bloque de código a ejecutar
while condición:
    # bloque de código a ejecutar
"""

""" Ana está desarrollando un programa que necesita 
procesar una lista de 5 nombres de clientes para generar 
informes mensuales. Para ello, necesita escribir un 
programa que recorra la lista de nombres y muestre cada 
cliente.

clientes = ["Juan", "Maria", "Carlos", "Ana", "Beatriz"]

Ayuda a Ana a decidir entre usar un lazo for o while. 
Escribe el programa usando el lazo que creas más adecuado 
para esta tarea y explica por qué elegiste ese lazo.
"""

clientes = ["Juan", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)

""" ndré está probando una nueva función en el backend 
de Buscante que procesa datos en un bucle. 
Durante las pruebas, se dio cuenta de que el sistema 
dejó de responder y sospecha que el problema está en un 
bucle infinito.

contador = 0

while contador < 10:
    print("Procesando datos...")

¿Cuál es el problema del código de André y cómo resolverlo?

El contador no se incrementa dentro del bucle, 
lo que hace que la condición siempre sea verdadera 
y el bucle se ejecute infinitamente.
"""

""" Marcos está desarrollando un programa para mostrar 
un mensaje de bienvenida repetidamente en la consola, 
como parte de una campaña de marketing de su plataforma 
llamada Buscante. Quiere asegurarse de que el mensaje 
se muestre 5 veces.

Ayuda a Marcos a escribir un programa que muestre el 
mensaje: "¡Bienvenido a Buscante!" el número exacto 
de veces que necesita.
"""

for i in range(5):
    print("¡Bienvenido a Buscante!")

""" Estás recibiendo una lista de valores que 
representan los productos de tu tienda virtual y te 
gustaría calcular la suma total de esos productos 
para entender el desempeño financiero semanal.

valores = [10, 20, 30, 40, 50]
Crea un programa para implementar la suma.
"""

valores = [10, 20, 30, 40, 50]
suma_total = 0
for valor in valores:
    suma_total += valor
print("La suma total de los productos es:", suma_total)

"""  na está desarrollando su portafolio para exhibir 
los proyectos de Python que ha completado. Ella organizó 
una lista con el nombre de cada proyecto, pero se dio 
cuenta de que algunos elementos pueden estar ausentes, 
apareciendo como None:

proyectos = ["sitio web", "juego", "análisis de datos", 
None, "aplicativo móvil"]

Crea un programa que ayude a Ana a recorrer la lista de 
proyectos y muestre los nombres de los proyectos válidos. Si encuentra un elemento None, el programa debe mostrar el mensaje: "Proyecto ausente".
"""

proyectos = ["sitio web", "juego", "análisis de datos", None, "aplicativo móvil"]
for proyecto in proyectos:
    if proyecto is not None:
        print(proyecto)
    else:
        print("Proyecto ausente")

""" José está desarrollando una funcionalidad en el 
sistema de Buscante para interrumpir la búsqueda tan 
pronto como se encuentre un libro específico. La lista 
de libros ya registrados en el sistema es la siguiente:

libros = ["1984", "Cien años de soledad", "El Principito", "El Hobbit", "Orgullo y Prejuicio"]

Ayuda a José a crear un programa que recorra la lista 
y muestre el mensaje "Libro encontrado: <nombre del libro>" 
tan pronto como se encuentre el libro "El Hobbit". 
Después de encontrar el libro, el programa debe detener 
inmediatamente la búsqueda, sin verificar los libros 
restantes.
"""

libros = ["1984", "Cien años de soledad", "El Principito", "El Hobbit", "Orgullo y Prejuicio"]
for libro in libros:    
    if libro == "El Hobbit":
        print("Libro encontrado:", libro)
        break

""" Estás desarrollando un sistema de control de 
inventario para Buscante. Uno de los requisitos es 
verificar la cantidad de ejemplares de un libro en 
inventario y continuar vendiendo hasta que el inventario 
se agote. Siempre que se realiza una venta, el sistema 
debe informar al usuario y actualizar la cantidad 
disponible.

Crea un programa que simule las ventas de un libro con 
el inventario inicial de 5 ejemplares. El programa debe 
mostrar el mensaje "¡Venta realizada! Inventario 
restante: <cantidad>" con cada venta y, al final, 
mostrar el mensaje "Inventario agotado".
"""

inventario = 5
while inventario > 0:
    print("¡Venta realizada! Inventario restante:", inventario - 1)
    inventario -= 1
else:
    print("Inventario agotado")

""" Aline está implementando una funcionalidad que muestra 
mensajes personalizados para los clientes durante una 
promoción especial de su nueva librería. El sistema debe 
mostrar un mensaje de cuenta regresiva personalizado para 
cada número de 10 a 1, y al final mostrar el mensaje: 
"¡Aprovecha la promoción ahora!".

Crea un programa que utilice un bucle for para mostrar 
los siguientes mensajes:

Para números pares, muestra: 
"Faltan solo <número> segundos - ¡No pierdas esta oportunidad!".
Para números impares, muestra: 
"La cuenta continúa: <número> segundos restantes.".
Al final de la cuenta, muestra el mensaje: 
"¡Aprovecha la promoción ahora!". 
"""

for i in range(10, 0, -1):
    if i % 2 == 0:
        print(f"Faltan solo {i} segundos - ¡No pierdas esta oportunidad!")
    else:
        print(f"La cuenta continúa: {i} segundos restantes.")
else:
    print("¡Aprovecha la promoción ahora!")

""" Ana está implementando un sistema de filtrado de libros 
en Buscante. La funcionalidad debe recorrer una lista de 
libros y mostrar el nombre de cada libro disponible en 
stock. Sin embargo, si el libro está agotado, debe ser 
ignorado durante la iteración.

libros = [
    {"nombre": "1984", "stock": 5},
    {"nombre": "Dom Casmurro", "stock": 0},
    {"nombre": "El Principito", "stock": 3},
    {"nombre": "El Hobbit", "stock": 0},
    {"nombre": "Orgullo y Prejuicio", "stock": 2}
]

Crea un programa que ayude a Ana a mostrar solamente los 
libros que tienen stock disponible, en el formato: 
"Libro disponible: <nombre del libro>".
"""

libros = [
    {"nombre": "1984", "stock": 5},
    {"nombre": "Dom Casmurro", "stock": 0},
    {"nombre": "El Principito", "stock": 3},
    {"nombre": "El Hobbit", "stock": 0},
    {"nombre": "Orgullo y Prejuicio", "stock": 2}
]
for libro in libros:
    if libro["stock"] > 0:
        print("Libro disponible:", libro["nombre"])

"""  João está desarrollando un sistema de registro para 
un sitio de lectura. Necesita asegurarse de que los usuarios 
ingresen un nombre de usuario y una contraseña válidos. 
Las reglas son las siguientes:

El nombre de usuario debe tener al menos 5 caracteres.
La contraseña debe tener al menos 8 caracteres.
João quiere que el sistema siga solicitando la información 
hasta que ambas condiciones se cumplan. 
Cuando el usuario ingresa datos válidos, el programa debe 
mostrar el mensaje: "¡Registro realizado con éxito!".

Crea un programa que implemente esta lógica usando un 
bucle while.
"""

while True:
    nombre_usuario = input("Digite su nombre de usuario: ")
    contraseña = input("Digite su contraseña: ")
    
    if len(nombre_usuario) >= 5 and len(contraseña) >= 8:
        print("¡Registro realizado con éxito!")
        break
    elif len(nombre_usuario) < 5:
        print("El nombre de usuario debe tener al menos 5 caracteres.")
    elif len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
