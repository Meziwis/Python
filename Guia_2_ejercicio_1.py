var_A = input('Variable A')
var_B = input('Variable B')

try:
    var_A = int(var_A)
    var_B = int(var_B)
    if var_A<var_B:
        print('mas pequeño')
    elif var_A>var_B:
        print('mas grande')
    else:
        print('igual')
except ValueError:
    print('String involucrado')
