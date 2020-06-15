from datetime import datetime
edad_1 = input('Ingrese edad a comparar 1: (YYYY-MM-DD)')
edad_2 = input('Ingrese edad a comparar 2: (YYYY-MM-DD)')
edad_1 = datetime.strptime(edad_1, '%Y-%m-%d')
edad_2 = datetime.strptime(edad_2, '%Y-%m-%d')
if edad_1 > edad_2:
    print('La segunda persona es más joven')
elif edad_1 < edad_2:
    print('La primera persona es más joven')
else:
    print('Las personas tienen la misma edad')
