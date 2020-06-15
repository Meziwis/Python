n_1 = int(input('Ingrese un número entero:'))
n_2 = int(input('Ingrese un segundo número entero:'))
if n_2==n_1**2:
    print('<El segundo es el cuadrado exacto del primero')
elif n_2<n_1**2:
    print('El segundo es menor que el cuadrado del primero')
else:
    print('El segundo es mayor que el cuadrado del primero')
