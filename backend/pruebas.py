from backend.backend import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    exchange_sort,
    gnome_sort,
    stooge_sort,
    quick_sort,
    merge_sort
)

backend = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    exchange_sort,
    gnome_sort,
    stooge_sort,
    quick_sort,
    merge_sort
]

casos = {
    "Normal": [5, 2, 8, 1, 4],
    "Ordenado": [1, 2, 3, 4, 5],
    "Inverso": [5, 4, 3, 2, 1],
    "Repetidos": [4, 2, 4, 1, 2],
    "Un elemento": [7],
    "Vacío": []
}

print("=" * 55)
print("PRUEBAS DE BACKEND DE ORDENAMIENTO")
print("=" * 55)


for algoritmo in backend:

    print(f"\n{algoritmo.__name__}")
    print("-" * 55)

    for nombre_caso, datos in casos.items():

        #Resultado correcto
        esperado = sorted(datos)

        try:
            resultado = algoritmo(datos)

            obtenido = resultado["resultado"]
            tiempo = resultado["tiempo_ejecucion"]

            #Verificar que el resultado sea correcto
            if obtenido == esperado:
                estado = "CORRECTO"
            else:
                estado = "ERROR"

            print(
                f"{nombre_caso:15} | "
                f"{estado:8} | "
                f"{datos} -> {obtenido} | "
                f"{tiempo:.8f} s"
            )

        except Exception as error:

            print(
                f"{nombre_caso:15} | "
                f"ERROR    | "
                f"{type(error).__name__}: {error}"
            )

print("\n" + "=" * 55)
print("PRUEBAS TERMINADAS")
print("=" * 55)