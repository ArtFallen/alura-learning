""" Operadores lógicos

AND

    TABLA DE VERDAD

    verdad + verdad = verdad
    verdad + false = false
    false + false = false
    """


numero = 13

if numero >= 12 and numero == 13:
    print('Condición verdadera')
else:
    print('Condición falsa')

"""
OR

    TABLA DE VERDAD

    false + false = false
    verdad + false = verdad
    verdad + verdad = verdad
 """

numero = 13

if numero == 12 or numero > 13:
    print('Condición verdadera')
else:
    print('Condición falsa')


