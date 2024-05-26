#sentencia


condicion = True

if condicion == True:
    print("condicion verdadera")
elif condicion == False:
    print("condicionverdadera")
else:
    print("Condicion falsa")

num = int(input('Digite un numero en el rango del 1 al 3 '))
numTexto = ' '
if num == 1:
    numTexto = 'Numero uno'
elif num == 2:
    numTexto= 'Numero dos'
elif num == 3:
    numTexto = 'Numero tres'
else:
    numTexto = 'Has ingresado un numero fuera del rango'
print(f'El numero ingresado es: {num} - {numTexto}')

# Sintaxis simplificada

condicion = True
#if condicion:
#   print('Condicion Verdadera')
#else:
#    print('Condicion Falsa')
print('Condicion Verdadera') if condicion else print('Condicion Falsa')
