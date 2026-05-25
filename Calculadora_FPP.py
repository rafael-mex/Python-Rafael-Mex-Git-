#Programa hecho por Mex Lozano Rafael Emilio 
#Calculadora que puede sumar, restar, multiplicar y dividir dos números flotantes; calcular la potencia de dos números y diferenciar números pares e impares

#Se importa la función "sleep" del módulo "time" para anadir pausas entre las funciones de el programa, logrando que este no se vea "efímero" o muy rápido cada que el usuario realice algo. 
from time import sleep 

#Se crean las operaciones como funciones para facilitar la programación de cada opción de la calculadora.
#Función "operación_suma"
def operacion_suma():
    sumando1= float(input("Ingresa el primer número= "))
    sumando2= float(input("Ingresa el segundo número= "))
    op_suma = sumando1 + sumando2
    print(f"{sumando1} + {sumando2} = {op_suma}",end="")
    return operacion_suma

#Función "operación_resta"
def operacion_resta():
    resta1= float(input("Ingresa el primer número= "))
    resta2= float(input("Ingresa el segundo número= "))
    op_resta = resta1 - resta2
    print(f"{resta1} - {resta2} = {op_resta}",end="")
    return operacion_resta 

#Función "operación_multiplicacion"
def operacion_multiplicacion():
    mult1= float(input("Ingresa el primer número= "))
    mult2= float(input("Ingresa el segundo número= "))
    op_multi = mult1 * mult2
    print(f"{mult1} x {mult2} = {op_multi}",end="")
    return operacion_multiplicacion

#Función "operación_division"
def operacion_division():
    div1= float(input("Ingresa el númerador= "))
    div2= float(input("Ingresa el denominador= "))
    op_division = div1 / div2
    print(f"{div1} / {div2} = {op_division}",end="")
    return operacion_multiplicacion

#Función "operación_potencia" 
def operacion_potencia():
    pot1= float(input("Ingresa la base= "))
    pot2= float(input("Ingresa el exponente= "))
    op_potencia = pot1 ** pot2
    print(f"{pot1} ^ {pot2} = {op_potencia}",end="")
    return operacion_potencia

#Se crea el menú interactivo que le permite al usuario seleccionar que operación elige hacer. A partir de aqui el código se encuentra adentro de un bucle.
#Menú------
while True:
    opcion_usuario = int(input(''' 
-"Calculadora Interactiva"-
1) Suma de dos flotantes
2) Resta de dos flotantes
3) Multiplación de dos flotantes
4) Divisón de dos flotantes
5) Potencia de dos números 
6) Diferenciador de un número par e impar
0) Salir del programa  
Seleccione una opción= ''')) 

#Opción 0 - Salir del programa ------
    if opcion_usuario == 0 :
        print("Saliste del programa")
        sleep(0.07)
        break

#Opción 1 - Suma ------
    elif opcion_usuario == 1:
        operacion_suma()
        pass

#Opción 2 - Resta------
    elif opcion_usuario == 2 :
        operacion_resta()
        pass

#Opción 3 - Multiplicación------
    elif opcion_usuario == 3 :
        operacion_multiplicacion()
        pass

#Opción 4 - Divisón------
    elif opcion_usuario == 4 :
        operacion_division()
        pass

#Opción 5 - Potencia------
    elif opcion_usuario == 5 :
        operacion_potencia()
        pass
    
#Opción 6 - Diferenciador------
    elif opcion_usuario == 6:
        numero_x = int(input("Ingrese un número entero= "))
        if numero_x % 2 == 0:
            print(f"El número {numero_x} es par")
            pass
        else:
            print(f"El número {numero_x} es impar")
            pass
    else:
        print("Opción inválida. Intente de nuevo")
        sleep(1)
        continue
    
    sleep(1)

#Se le pregunta al usuario si quiere re-ingresar a la calculadora y se le dan dos opciones "s/n", si elige "s" entonces volverá a la calculadora, si elige "n" saldrá del programa y si pone alguna otra opción se le regresará automaticamente al programa. 

    elección_usuario = str(input("""
¿Deseas volver a ingresar a la calculadora? (s/n)= """))
    if elección_usuario == "s" :
        continue 
    elif elección_usuario == "n":
        print("Saliendo de la calculadora...") , sleep(2)
        break 
    else:
        print("Entrada inválida. Se te regresará al menú de opciones"), sleep(1)

#Se crea una línea de texto en el que se menciona que yo creé el programa, esta línea se encuentra fuera del bucle para que solo se muestre si se sale del programa         
print("""

-Programa hecho por Mex Lozano Rafael Emilio\n""")

    



    