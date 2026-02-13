""" Operadores comparación

    == igual
    != diferente
    >  más grande
    >= más grande o igual
    < más pequeno
    <= más pequeño o igual

 """

numero = 15

if numero <= 15:
    print('Condición verdadera', numero)
else:
    print('Condición falsa')

numero = 11

if numero != 12:
    print("más grande")
else:
    print("más pequeño")

""" Crea un programa que reciba el número de ventas de 
los dos productos y muestre un mensaje indicando cuál 
de ellos vendió más. Si las cantidades son iguales, 
muestra un mensaje diciendo que hubo un empate.
"""

manzanas = input("Digite la cantidad de manzanas vendidas: ")
platanos = input("Digite la cantidad de plátanos vendidos: ")

if manzanas == platanos:
    print("hubo un empate!")
elif manzanas > platanos:
    print("Las manzanas tuvieron más ventas")
else:
    print("Los plátanos tuvieron más ventas")

""" Lucas trabaja en TI y necesita garantizar que la 
temperatura de una sala de servidores no supere los 25°C. 
Quiere un programa que reciba la temperatura actual 
como entrada y, si es necesario, muestre un mensaje de 
alerta.

"""

temperatura = input("Digite la temperatura actual: ")
if temperatura > 25:
    print("¡Alerta! Temperatura por encima del limite permitido.")

""" Escribe un programa que reciba el número de días de 
tres actividades y muestre el tiempo total del proyecto. 
Si algún valor es negativo, muestra un mensaje informando 
el error.
"""

actividad_a = input("Informe los días de la actividad A: ")
actividad_b = input("Informe los días de la actividad B: ")
actividad_c = input("Informe los días de la actividad C: ")

if int(actividad_a) < 0 or int(actividad_b) < 0 or int(actividad_c) < 0:
    print("Error: Los días no pueden ser negativos.")
else:
    total = int(actividad_a) + int(actividad_b) + int(actividad_c)
    print(f"El tiempo total del proyecto es de {total} días.")

""" El programa debe recibir el peso y la altura de una 
persona y mostrar el valor del IMC, además de indicar si 
está por debajo del peso, con peso normal o por encima 
del peso. Crea un programa que reciba el peso (en kg) y 
la altura (en metros) y calcule el IMC usando la fórmula: 
IMC = peso / (altura ** 2)
Luego, muestra el valor del IMC y un mensaje indicando 
si está por debajo del peso (IMC < 18.5), 
peso normal (18.5 <= IMC < 25) 
o por encima del peso (IMC >= 25).
"""

peso = float(input("Digite su peso (kg): "))
altura = float(input("Digite su altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Su IMC es {imc:.2f}, está por debajo del peso normal.")
elif 18.5 <= imc < 25:
    print(f"Su IMC es {imc:.2f}, tiene un peso normal.")
else:
    print(f"Su IMC es {imc:.2f}, está por encima del peso normal.")

""" Crea un programa que reciba los ingresos mensuales 
y la cantidad de hijos de una persona, y diga si tiene 
derecho al beneficio. Para eso, la persona debe cumplir 
las siguientes condiciones:

Tener ingresos menores o iguales a $2,000.
Tener al menos un hijo o hija.
"""

ingresos = float(input("Digite sus ingresos mensuales: "))
hijos = int(input("Digite la cantidad de hijos: "))
if ingresos <= 2000 and hijos >= 1:
    print("Tiene derecho al beneficio.")

""" Una empresa evalúa a sus empleados con base 
en dos criterios:

- Puntuación de desempeño (de 0 a 10)
- Años trabajados
Reglas:

Si la puntuación es mayor o igual a 7:
Si trabajó más de 5 años: "Elegible para ascenso"
Si trabajó 5 años o menos: "Buen desempeño, sigue así"
Si la puntuación es menor a 7: "Necesita mejorar"

Crea un programa que reciba la puntuación y los años trabajados, y muestre el mensaje adecuado.
"""

puntuacion = float(input("Digite la puntuación de desempeño (0-10): "))
anos_trabajados = int(input("Digite los años trabajados: "))
if puntuacion >= 7:
    if anos_trabajados > 5:
        print("Elegible para ascenso")
    else:
        print("Buen desempeño, sigue así")
else:
    print("Necesita mejorar")

""" Estás desarrollando un pequeño juego. 
El usuario ingresa un número entero y el programa 
debe evaluar lo siguiente:

Si el número es divisible por 3 y 5, muestra: "¡Número mágico!"
Si solo es divisible por 3, muestra: "Divisible por 3"
Si solo es divisible por 5, muestra: "Divisible por 5"
Si no es divisible por ninguno, muestra: "No es un número mágico"
"""

numero = int(input("Digite un número entero: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("¡Número mágico!")
elif numero % 3 == 0:
    print("Divisible por 3")
elif numero % 5 == 0:
    print("Divisible por 5")
else:
    print("No es un número mágico")

""" Una escuela otorga becas según tres criterios:

Ingreso familiar mensual.
Promedio del estudiante.
Asistencia (en porcentaje).
Reglas:

Si el ingreso es menor a $1,500 y 
el promedio es mayor a 8.0 y 
la asistencia es al menos 90% → "Beca completa"

Si el ingreso es menor a $2,500 y 
promedio mayor a 7.0 y 
asistencia al menos 85% → "Media beca"

En otros casos → "No elegible para beca"
"""

ingreso = float(input("Digite el ingreso familiar mensual: "))
promedio = float(input("Digite el promedio del estudiante: "))
asistencia = float(input("Digite la asistencia (en porcentaje): "))
if ingreso < 1500 and promedio > 8.0 and asistencia >= 90:
    print("Beca completa")
elif ingreso < 2500 and promedio > 7.0 and asistencia >= 85:
    print("Media beca")
else:
    print("No elegible para beca")

""" Un sistema de transporte cobra según la edad 
del pasajero y la distancia recorrida:

Menores de 6 años: Viajan gratis.

De 6 a 18 años:
Hasta 20 km: $1.50
Más de 20 km: $2.50

Mayores de 18:
Hasta 20 km: $2.50
Más de 20 km: $4.00

Crea un programa que reciba la edad y distancia, y muestre el valor a pagar.
"""
edad = int(input("Digite la edad del pasajero: "))
distancia = float(input("Digite la distancia recorrida (en km): "))

if edad < 6:
    print("Viajan gratis.")
elif 6 <= edad <= 18:
    if distancia <= 20:
        print("El valor a pagar es $1.50.")
    else:
        print("El valor a pagar es $2.50.")
else:
    if distancia <= 20:
        print("El valor a pagar es $2.50.")
    else:
        print("El valor a pagar es $4.00.")

""" Una empresa evalúa su trimestre con base en:

Ingresos totales
Gastos totales
Número de nuevos clientes
Clasificación:

Si ingresos - gastos > $10,000 y 
más de 50 nuevos clientes → "Trimestre Excelente"
Si ingresos - gastos > $5,000 y 
al menos 20 clientes → "Trimestre Bueno"
Si ingresos - gastos > 0 → "Trimestre Regular"
Si ingresos - gastos ≤ 0 → "Trimestre Deficitario"
"""

ingresos = float(input("Digite los ingresos totales: "))
gastos = float(input("Digite los gastos totales: "))
nuevos_clientes = int(input("Digite el número de nuevos clientes: "))
balance = ingresos - gastos
if balance > 10000 and nuevos_clientes > 50:
    print("Trimestre Excelente")
elif balance > 5000 and nuevos_clientes >= 20:
    print("Trimestre Bueno")
elif balance > 0:
    print("Trimestre Regular")
else:
    print("Trimestre Deficitario")