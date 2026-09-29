from time import perf_counter

#Bubble Sort
def bubble_sort(datos):
    inicio_tiempo = perf_counter()
    arreglo = datos.copy()

    pasos = []
    comparaciones = 0
    intercambios = 0

    n = len(arreglo)

    for i in range(n - 1):
        hubo_intercambio = False

        for j in range(n - 1 - i):

            #Comparacion
            comparaciones += 1

            pasos.append({
                "tipo": "comparacion",
                "indices": [j, j + 1],
                "arreglo": arreglo.copy()
            })

            #Intercambio
            if arreglo[j] > arreglo[j + 1]:

                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

                intercambios += 1
                hubo_intercambio = True

                pasos.append({
                    "tipo": "intercambio",
                    "indices": [j, j + 1],
                    "arreglo": arreglo.copy()
                })

        if not hubo_intercambio:
            break

    pasos.append({
        "tipo": "final",
        "indices": [],
        "arreglo": arreglo.copy()
    })

    fin_tiempo = perf_counter()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo

    return {
        "algoritmo": "Bubble Sort",
        "complejidad": "O(n²)",
        "resultado": arreglo,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "tiempo_ejecucion": tiempo_ejecucion,
        "pasos": pasos
    }


#Selection Sort
def selection_sort(datos):
    inicio_tiempo = perf_counter()
    arreglo = datos.copy()

    pasos = []
    comparaciones = 0
    intercambios = 0

    n = len(arreglo)

    for i in range(n - 1):

        indice_menor = i

        for j in range(i + 1, n):

            #Comparacion
            comparaciones += 1

            pasos.append({
                "tipo": "comparacion",
                "indices": [indice_menor, j],
                "arreglo": arreglo.copy()
            })

            #Guardar la posición del elemento menor
            if arreglo[j] < arreglo[indice_menor]:
                indice_menor = j

        #Intercambio
        if indice_menor != i:

            arreglo[i], arreglo[indice_menor] = \
                arreglo[indice_menor], arreglo[i]

            intercambios += 1

            pasos.append({
                "tipo": "intercambio",
                "indices": [i, indice_menor],
                "arreglo": arreglo.copy()
            })

    pasos.append({
        "tipo": "final",
        "indices": [],
        "arreglo": arreglo.copy()
    })

    fin_tiempo = perf_counter()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo

    return {
        "algoritmo": "Selection Sort",
        "complejidad": "O(n²)",
        "resultado": arreglo,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "tiempo_ejecucion": tiempo_ejecucion,
        "pasos": pasos
    }


#Insertion Sort
def insertion_sort(datos):
    inicio_tiempo = perf_counter()
    arreglo = datos.copy()

    pasos = []
    comparaciones = 0
    intercambios = 0

    n = len(arreglo)

    for i in range(1, n):

        #Mover elemento a la izquierda hasta posición correcta
        j = i
        while j > 0:

            #Comparacion
            comparaciones += 1

            pasos.append({
                "tipo": "comparacion",
                "indices": [j - 1, j],
                "arreglo": arreglo.copy()
            })

            #Orden correcto, posicion encontrada
            if arreglo[j - 1] <= arreglo[j]:
                break

            #Intercambio
            arreglo[j - 1], arreglo[j] = arreglo[j], arreglo[j - 1]

            intercambios += 1

            pasos.append({
                "tipo": "intercambio",
                "indices": [j - 1, j],
                "arreglo": arreglo.copy()
            })

            j -= 1

    pasos.append({
        "tipo": "final",
        "indices": [],
        "arreglo": arreglo.copy()
    })

    fin_tiempo = perf_counter()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo

    return {
        "algoritmo": "Insertion Sort",
        "complejidad": "O(n²)",
        "resultado": arreglo,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "tiempo_ejecucion": tiempo_ejecucion,
        "pasos": pasos
    }


#Exchange Sort
def exchange_sort(datos):
    inicio_tiempo = perf_counter()
    arreglo = datos.copy()

    pasos = []
    comparaciones = 0
    intercambios = 0

    n = len(arreglo)

    for i in range(n - 1):

        for j in range(i + 1, n):

            #Comparacion
            comparaciones += 1

            pasos.append({
                "tipo": "comparacion",
                "indices": [i, j],
                "arreglo": arreglo.copy()
            })

            #Intercambio
            if arreglo[i] > arreglo[j]:

                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

                intercambios += 1

                pasos.append({
                    "tipo": "intercambio",
                    "indices": [i, j],
                    "arreglo": arreglo.copy()
                })

    pasos.append({
        "tipo": "final",
        "indices": [],
        "arreglo": arreglo.copy()
    })

    fin_tiempo = perf_counter()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo

    return {
        "algoritmo": "Exchange Sort",
        "complejidad": "O(n²)",
        "resultado": arreglo,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "tiempo_ejecucion": tiempo_ejecucion,
        "pasos": pasos
    }


#Gnome Sort
def gnome_sort(datos):
    inicio_tiempo = perf_counter()
    arreglo = datos.copy()

    pasos = []
    comparaciones = 0
    intercambios = 0

    n = len(arreglo)
    indice = 1

    while indice < n:

        #Comparacion
        comparaciones += 1

        pasos.append({
            "tipo": "comparacion",
            "indices": [indice - 1, indice],
            "arreglo": arreglo.copy()
        })

        #Si estan en orden, se avanza
        if arreglo[indice - 1] <= arreglo[indice]:
            indice += 1

        else:
            #Intercambio
            arreglo[indice - 1], arreglo[indice] = \
                arreglo[indice], arreglo[indice - 1]

            intercambios += 1

            pasos.append({
                "tipo": "intercambio",
                "indices": [indice - 1, indice],
                "arreglo": arreglo.copy()
            })

            #Retroceder para comprobar el elemento anterior
            indice -= 1

            #Evitar salir del arreglo
            if indice == 0:
                indice = 1

    pasos.append({
        "tipo": "final",
        "indices": [],
        "arreglo": arreglo.copy()
    })

    fin_tiempo = perf_counter()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo

    return {
        "algoritmo": "Gnome Sort",
        "complejidad": "O(n²)",
        "resultado": arreglo,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "tiempo_ejecucion": tiempo_ejecucion,
        "pasos": pasos
    }


#Stooge Sort
def stooge_sort(datos):
    inicio_tiempo = perf_counter()
    arreglo = datos.copy()

    pasos = []
    comparaciones = 0
    intercambios = 0

    def ordenar(inicio, fin):
        nonlocal comparaciones, intercambios

        if inicio >= fin:
            return

        #Comparacion
        comparaciones += 1

        pasos.append({
            "tipo": "comparacion",
            "indices": [inicio, fin],
            "arreglo": arreglo.copy()
        })

        #Comparar primer y ultimo elemento
        if arreglo[inicio] > arreglo[fin]:

            arreglo[inicio], arreglo[fin] = \
                arreglo[fin], arreglo[inicio]

            intercambios += 1

            pasos.append({
                "tipo": "intercambio",
                "indices": [inicio, fin],
                "arreglo": arreglo.copy()
            })

        #minimo 3 elementos
        if fin - inicio + 1 > 2:

            tercio = (fin - inicio + 1) // 3

            #Ordenar primeros
            ordenar(inicio, fin - tercio)

            #Ordenar últimos
            ordenar(inicio + tercio, fin)

            ordenar(inicio, fin - tercio)

    ordenar(0, len(arreglo) - 1)

    pasos.append({
        "tipo": "final",
        "indices": [],
        "arreglo": arreglo.copy()
    })

    fin_tiempo = perf_counter()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo

    return {
        "algoritmo": "Stooge Sort",
        "complejidad": "O(n^2.71)",
        "resultado": arreglo,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "tiempo_ejecucion": tiempo_ejecucion,
        "pasos": pasos
    }


#Quick Sort
def quick_sort(datos):
    inicio_tiempo = perf_counter()
    arreglo = datos.copy()

    pasos = []
    comparaciones = 0
    intercambios = 0

    def particion(inicio, fin):
        nonlocal comparaciones, intercambios

        #Ultimo elemento pivote
        pivote = arreglo[fin]

        #Registrar elemento pivote
        pasos.append({
            "tipo": "pivote",
            "indices": [fin],
            "arreglo": arreglo.copy()
        })

        i = inicio - 1

        #Comparar elementos con el pivote
        for j in range(inicio, fin):

            comparaciones += 1

            pasos.append({
                "tipo": "comparacion",
                "indices": [j, fin],
                "arreglo": arreglo.copy()
            })

            #Elemento menor o igual al pivote, colocar en izquierda
            if arreglo[j] <= pivote:
                i += 1

                #No registrar intercambios innecesarios
                if i != j:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

                    intercambios += 1

                    pasos.append({
                        "tipo": "intercambio",
                        "indices": [i, j],
                        "arreglo": arreglo.copy()
                    })

        #Colocar pivote en su posición definitiva
        posicion_pivote = i + 1

        if posicion_pivote != fin:
            arreglo[posicion_pivote], arreglo[fin] = \
                arreglo[fin], arreglo[posicion_pivote]

            intercambios += 1

            pasos.append({
                "tipo": "intercambio",
                "indices": [posicion_pivote, fin],
                "arreglo": arreglo.copy()
            })

        #Indicar que pivote quedo colocado
        pasos.append({
            "tipo": "colocado",
            "indices": [posicion_pivote],
            "arreglo": arreglo.copy()
        })

        return posicion_pivote

    def ordenar(inicio, fin):
        if inicio < fin:

            posicion_pivote = particion(inicio, fin)

            #Ordenar parte izquierda
            ordenar(inicio, posicion_pivote - 1)

            #Ordenarparte derecha
            ordenar(posicion_pivote + 1, fin)

    ordenar(0, len(arreglo) - 1)

    pasos.append({
        "tipo": "final",
        "indices": [],
        "arreglo": arreglo.copy()
    })

    fin_tiempo = perf_counter()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo

    return {
        "algoritmo": "Quick Sort",
        "complejidad": "O(n log n)",
        "resultado": arreglo,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "tiempo_ejecucion": tiempo_ejecucion,
        "pasos": pasos
    }


#Merge Sort
def merge_sort(datos):
    inicio_tiempo = perf_counter()
    arreglo = datos.copy()

    pasos = []
    comparaciones = 0
    escrituras = 0

    def mezclar(inicio, medio, fin):
        nonlocal comparaciones, escrituras

        #Crear copias
        izquierda = arreglo[inicio:medio + 1]
        derecha = arreglo[medio + 1:fin + 1]

        i = 0
        j = 0
        k = inicio

        #Comparar elementos
        while i < len(izquierda) and j < len(derecha):

            comparaciones += 1

            #Pociones a comparar en el arreglo original
            indice_izquierda = inicio + i
            indice_derecha = medio + 1 + j

            pasos.append({
                "tipo": "comparacion",
                "indices": [indice_izquierda, indice_derecha],
                "arreglo": arreglo.copy()
            })

            if izquierda[i] <= derecha[j]:
                arreglo[k] = izquierda[i]
                i += 1
            else:
                arreglo[k] = derecha[j]
                j += 1

            escrituras += 1

            pasos.append({
                "tipo": "escritura",
                "indices": [k],
                "arreglo": arreglo.copy()
            })

            k += 1

        #Copiar elementos restantes izquierda
        while i < len(izquierda):

            arreglo[k] = izquierda[i]
            i += 1

            escrituras += 1

            pasos.append({
                "tipo": "escritura",
                "indices": [k],
                "arreglo": arreglo.copy()
            })

            k += 1

        #Copiar elementos restantes derecha
        while j < len(derecha):

            arreglo[k] = derecha[j]
            j += 1

            escrituras += 1

            pasos.append({
                "tipo": "escritura",
                "indices": [k],
                "arreglo": arreglo.copy()
            })

            k += 1

    def ordenar(inicio, fin):
        if inicio < fin:

            medio = (inicio + fin) // 2

            #Dividir recursivamente
            ordenar(inicio, medio)
            ordenar(medio + 1, fin)

            #Mezclar las mitades ordenadas
            mezclar(inicio, medio, fin)

    ordenar(0, len(arreglo) - 1)

    pasos.append({
        "tipo": "final",
        "indices": [],
        "arreglo": arreglo.copy()
    })

    fin_tiempo = perf_counter()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    
    return {
        "algoritmo": "Merge Sort",
        "complejidad": "O(n log n)",
        "resultado": arreglo,
        "comparaciones": comparaciones,
        "intercambios": 0,
        "escrituras": escrituras,
        "tiempo_ejecucion": tiempo_ejecucion,
        "pasos": pasos
    }
