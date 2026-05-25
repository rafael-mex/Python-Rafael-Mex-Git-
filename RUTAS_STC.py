#Programa creado por Mex Lozano Rafael Emilio
#Este programa permite al usuario crear rutas con las estaciones del metro de la CDMX.

#Se importa de la biblioteca "Líneas_metro.py" la función "verificador_estaciones" junto con las variables de todas las líneas. 
from Lineas_metro import (verificador_estaciones, linea_1,linea_2,linea_3,linea_4,linea_5,linea_6,linea_7,linea_8,linea_9,linea_A,linea_B,linea_12)

#Se trae este argumento de la función "verificador_estaciones" que aquí será una variable que definirá a todas las líneas en este programa.
lista_estaciones = linea_1 + linea_2 + linea_3 + linea_4 + linea_5 + linea_6 + linea_7 + linea_8 + linea_9 + linea_A + linea_B + linea_12 

print(""" "RUTAS STC"
      Hola, bienvenido a este creador de rutas del Sistema de Transporte Colectivo Metro, aquí podrás crear tu ruta personalizada con las estaciones que tú quieras, ya sea para transbordar o para finalizar tu recorrido, solo sigue las instrucciones y disfruta tu viaje\n""")

print(""" Instrucciones
      ° Escribe el nombre de la estación tal cual aparece en el mapa de la Movilidad Integrada, cuida que este escrito correctamente. Si la estación es de transbordo escribe a lado de su nombre la línea de correspondencia, por ejemplo: Pantitlán L1
      ° Empieza con la estación con la que inicias tu recorrido, posteriormente escribirás unicamamente las estaciones en donde descenderas, ya sea para transbordar o para finalizar tu recorrido. 
      ° Unicamente tienes 10 espacios para nombrar tus estaciones, no es necesario nombrar toda la línea, unicamente las estaciones que son clave en tu recorrido.
      ° Si ya acabaste de escribir las estaciones de tu ruta solo presiona "Enter" para continuar\n""")

#Se implementa un bucle en cada uno de los 10 espacios que se rompe si el usuario escribe correctamente el nombre de la estación, sino este continuará para que pueda reintentar escribirla correctamente.
#Espacio 1
while True:
    estacion_1 = str(input("E1="))
    if verificador_estaciones(estacion_1,lista_estaciones):
        break 
    else:
        print("Estación no reconocida, inténtelo de nuevo")
#Espacio 2.
while True:
    estacion_2 = str(input("E2="))
    if verificador_estaciones(estacion_2,lista_estaciones): 
        break
    else:
        print("Estación no reconocida, inténtelo de nuevo")
#Espacio 3.
while True:
    estacion_3 = str(input("E3="))
    if verificador_estaciones(estacion_3,lista_estaciones) or estacion_3 == "" :
        break
    else:
        print("Estación no reconocida, inténtelo de nuevo")
#Espacio 4.
while True:
    estacion_4 = str(input("E4="))
    if verificador_estaciones(estacion_4,lista_estaciones) or estacion_4 == "":
        break
    else:
        print("Estación no reconocida, inténtelo de nuevo")
#Espacio 5.
while True:
    estacion_5 = str(input("E5="))
    if verificador_estaciones(estacion_5,lista_estaciones) or estacion_5 == "": 
        break
    else:
        print("Estación no reconocida, inténtelo de nuevo")
#Espacio 6.
while True:
    estacion_6 = str(input("E6="))
    if verificador_estaciones(estacion_6,lista_estaciones) or estacion_6 == "": 
        break
    else:
        print("Estación no reconocida, inténtelo de nuevo")
#Espacio 7.
while True:
    estacion_7 = str(input("E7="))
    if verificador_estaciones(estacion_7,lista_estaciones) or estacion_7 == "": 
        break
    else:
        print("Estación no reconocida, inténtelo de nuevo")
#Espacio 8.
while True:
    estacion_8 = str(input("E8="))
    if verificador_estaciones(estacion_8,lista_estaciones) or estacion_8 == "": 
        break
    else:
        print("Estación no reconocida, inténtelo de nuevo")
#Espacio 9.
while True:
    estacion_9 = str(input("E9="))
    if verificador_estaciones(estacion_9,lista_estaciones) or estacion_9 == "": 
        break
    else:
        print("Estación no reconocida, inténtelo de nuevo")
#Espacio 10.
while True:
    estacion_10 = str(input("E10="))
    if verificador_estaciones(estacion_10,lista_estaciones) or estacion_10 == "": 
        break
    else:
        print("Estación no reconocida, inténtelo de nuevo")

print("""
      Creaste tu ruta exitosamente""")
print(f'''Ruta registrada:

{estacion_1}
{estacion_2}
{estacion_3}''')
#A partir del espacio 4, si el usuario no puso ninguna estación el programa lo verificara y saltara al espacio que continua y asi sucesivamente hasta que termine de confirmarlos a todos, si el usuario si coloco una estación entonces el programa lo mostrará.

if estacion_4 == "":
    pass
else:
    print(f"{estacion_4}")
if estacion_5 == "":
    pass
else:
    print(f"{estacion_5}")
    
if estacion_6 == "":
    pass
else:
    print(f"{estacion_6}")
if estacion_7 == "":
    pass
else:
    print(f"{estacion_7}")
if estacion_8 == "":
    pass
else:
    print(f"{estacion_8}")
if estacion_9 == "":
    pass
else:
    print(f"{estacion_9}")
if estacion_10 == "":
    pass
else:
    print(f"{estacion_10}")

print("""
    Programa creado por Mex Lozano Rafael Emilio""")




