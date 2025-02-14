#!/usr/bin/python3

import random, sys

def seguir() -> str:
    '''
        Devuelve una cadena aleatoria
        para continuar un laberinto.
    '''
    posibles_paredes = ['|', '-', '\n', '|_ ', '_ ', ' _|', ' ', '-|']

    return random.choice(posibles_paredes)

def trazar(longitud:int) -> str:
    '''
        Devuelve un laberinto con una
        cantidad definida de caracteres.
    '''
    laberinto = random.choice(['=', '||'])
    # Voy agregando camino, cuando encuentro '=' o '||' corto ya que es la salida
    for caracter in range(longitud):
       
        traza = seguir()

        if (traza != '=') and (traza != '||'):
            # Sumo mas al camino si es correcto
            laberinto += traza * random.randint(1, 6)

            laberinto += seguir() * random.randint(3, 6)

        else:
            # Creo salida

            laberinto += seguir() * random.randint(1, 10)

            laberinto += seguir() * random.randint(1, 3)

            laberinto += random.choice(['||', '='])
            # Cierro en caso de encontrar un indicador de salida en traza
            break
    # Devuelvo el resultado de todo el laberinto
    return laberinto

# Prueba unitarias y de integracion
for prueba in [seguir(), trazar(random.randint(12, 60))]:
    print('%s\n' % prueba)
    # Escribo resultado si es conveniente
    opcion = input('\nDesea guardar resultado ¿sí o no? ').lower()
    # Veo si la persona guardará o no el archivo según que seleccione
    if (opcion == 'sí') or (opcion == 'si'):
        # La persona elige el nombre de archivo con su extension donde estarán los resultados
        nombre = sys.argv[1].lower()

        archivo = open(nombre, 'a')
        # Escribo de forma aditiva cada resultado al archivo
        archivo.write(prueba + '\n')
        # Libero memoria para reducir memory leaks
        archivo.close()
    else:
        # No se guardaran en algun archivo los resultados
        print('\tNO SE GUARDARÁ NINGÚN RESULTADO\n')
