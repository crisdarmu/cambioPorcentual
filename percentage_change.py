#La formula para hallar el cambio porcentual es la siguiente:
#Cambio porcentual = (cantidad final - cantidad inicial) / Cantidad Inicial * 100%


continue_calc = True #Definimos una variable para darle la opción al usuario de realizar calculos adicionales
change_list = [] #Definimos una lista donde almacenaremos los diferentes porcentajes de cambio calculados

while continue_calc: # Mientras la variable esté en True, se calcularán porcentajes de cambio de dos numeros
    initial = input('Ingrese el valor inicial: ') # Solicitamos el valor inicial
    final = input('Ingrese el valor final: ') # Solicitamos el valor final
    try: # Utilizamos try catch para manejar excepciones (esto lo aprendí leyendo un poco más)
        initial = float(initial) # Hacemos una validación para saber si los valores ingresados se pueden convertir a float
        final = float(final) # si esta validación falla quiere decir que los valores ingresados no son numeros
    except:
        print("Error, solo se permiten numeros, por favor verifica los valores")
        continue # El continue hará que el ciclo retorne al inicio sin ejecutar la lógica que está abajo de él
    #Calculamos el porcentaje de cambio con la formula y lo redondeamos a dos decimanles usando round
    change = round((final - initial) / initial * 100, 2)
    change_item = []  # Definimos una lista para almacenar los valores y luego guardarlos en otra lista
    change_item.append(initial)
    change_item.append(final)
    change_item.append(str(change)+"%")    
    if change > 0:
        print(f'El valor {initial} aumentó un {change}% respecto al valor {final}') # Imprimimos resultado basado en condicionales
        change_item.append('↑')
    if change < 0:
        print(f'El valor {initial} disminuyó un {change}% respecto al valor {final}') # Imprimimos resultado basado en condicionales
        change_item.append('↓')
    if change == 0:
        print(f"No hubo variacion en relación a los valores ingresados") # Imprimimos resultado basado en condicionales
        change_item.append('=')
    change_list.append(change_item) # Ingresamos la lista de valores a la lista principal
    again = input('Desea continuar? s/n: ') #Solicitamos si desea seguir realizando calculos
    if again.lower() != 's':
        continue_calc = False
print('Initial | Final | Change % | Status')
for row in change_list: # Imprimimos todos los valores de los porcentajes de cambio calculados
    print(list(row))