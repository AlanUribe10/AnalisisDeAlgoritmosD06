import copy
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

# ==========================================
# 1. ALGORITMOS DE ORDENAMIENTO DE BACKEND.PY
# ==========================================

def bubble_sort(arr):
    array = copy.deepcopy(arr)
    pasos = []
    comparaciones = 0
    intercambios = 0
    escrituras = 0
    
    inicio = time.perf_counter()
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparaciones += 1
            pasos.append({"tipo": "comparacion", "indices": [j, j + 1], "arreglo": list(array)})
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                intercambios += 1
                escrituras += 2
                pasos.append({"tipo": "intercambio", "indices": [j, j + 1], "arreglo": list(array)})
    
    tiempo = time.perf_counter() - inicio
    pasos.append({"tipo": "final", "indices": [], "arreglo": list(array)})
    
    return {
        "pasos": pasos,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "escrituras": escrituras,
        "tiempo_ejecucion": tiempo
    }

def selection_sort(arr):
    array = copy.deepcopy(arr)
    pasos = []
    comparaciones = 0
    intercambios = 0
    escrituras = 0
    
    inicio = time.perf_counter()
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            pasos.append({"tipo": "comparacion", "indices": [min_idx, j], "arreglo": list(array)})
            if array[j] < array[min_idx]:
                min_idx = j
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            intercambios += 1
            escrituras += 2
            pasos.append({"tipo": "intercambio", "indices": [i, min_idx], "arreglo": list(array)})
            
    tiempo = time.perf_counter() - inicio
    pasos.append({"tipo": "final", "indices": [], "arreglo": list(array)})
    
    return {
        "pasos": pasos,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "escrituras": escrituras,
        "tiempo_ejecucion": tiempo
    }

def insertion_sort(arr):
    array = copy.deepcopy(arr)
    pasos = []
    comparaciones = 0
    intercambios = 0
    escrituras = 0
    
    inicio = time.perf_counter()
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            pasos.append({"tipo": "comparacion", "indices": [j, j + 1], "arreglo": list(array)})
            if array[j] > key:
                array[j + 1] = array[j]
                escrituras += 1
                intercambios += 1
                pasos.append({"tipo": "escritura", "indices": [j + 1], "arreglo": list(array)})
                j -= 1
            else:
                break
        array[j + 1] = key
        escrituras += 1
        pasos.append({"tipo": "escritura", "indices": [j + 1], "arreglo": list(array)})
        
    tiempo = time.perf_counter() - inicio
    pasos.append({"tipo": "final", "indices": [], "arreglo": list(array)})
    
    return {
        "pasos": pasos,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "escrituras": escrituras,
        "tiempo_ejecucion": tiempo
    }

def exchange_sort(arr):
    array = copy.deepcopy(arr)
    pasos = []
    comparaciones = 0
    intercambios = 0
    escrituras = 0
    
    inicio = time.perf_counter()
    n = len(array)
    for i in range(n - 1):
        for j in range(i + 1, n):
            comparaciones += 1
            pasos.append({"tipo": "comparacion", "indices": [i, j], "arreglo": list(array)})
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                intercambios += 1
                escrituras += 2
                pasos.append({"tipo": "intercambio", "indices": [i, j], "arreglo": list(array)})
                
    tiempo = time.perf_counter() - inicio
    pasos.append({"tipo": "final", "indices": [], "arreglo": list(array)})
    
    return {
        "pasos": pasos,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "escrituras": escrituras,
        "tiempo_ejecucion": tiempo
    }

def gnome_sort(arr):
    array = copy.deepcopy(arr)
    pasos = []
    comparaciones = 0
    intercambios = 0
    escrituras = 0
    
    inicio = time.perf_counter()
    index = 0
    n = len(array)
    while index < n:
        if index == 0:
            index += 1
        comparaciones += 1
        pasos.append({"tipo": "comparacion", "indices": [index - 1, index], "arreglo": list(array)})
        if array[index] >= array[index - 1]:
            index += 1
        else:
            array[index], array[index - 1] = array[index - 1], array[index]
            intercambios += 1
            escrituras += 2
            pasos.append({"tipo": "intercambio", "indices": [index - 1, index], "arreglo": list(array)})
            index -= 1
            
    tiempo = time.perf_counter() - inicio
    pasos.append({"tipo": "final", "indices": [], "arreglo": list(array)})
    
    return {
        "pasos": pasos,
        "comparaciones": comparaciones,
        "intercambios": intercambios,
        "escrituras": escrituras,
        "tiempo_ejecucion": tiempo
    }

def stooge_sort(arr):
    array = copy.deepcopy(arr)
    pasos = []
    stats = {"comp": 0, "swap": 0, "write": 0}
    
    def _stooge(l, h):
        if l >= h:
            return
        stats["comp"] += 1
        pasos.append({"tipo": "comparacion", "indices": [l, h], "arreglo": list(array)})
        if array[l] > array[h]:
            array[l], array[h] = array[h], array[l]
            stats["swap"] += 1
            stats["write"] += 2
            pasos.append({"tipo": "intercambio", "indices": [l, h], "arreglo": list(array)})
        if h - l + 1 > 2:
            t = (h - l + 1) // 3
            _stooge(l, h - t)
            _stooge(l + t, h)
            _stooge(l, h - t)

    inicio = time.perf_counter()
    _stooge(0, len(array) - 1)
    tiempo = time.perf_counter() - inicio
    pasos.append({"tipo": "final", "indices": [], "arreglo": list(array)})
    
    return {
        "pasos": pasos,
        "comparaciones": stats["comp"],
        "intercambios": stats["swap"],
        "escrituras": stats["write"],
        "tiempo_ejecucion": tiempo
    }

def quick_sort(arr):
    array = copy.deepcopy(arr)
    pasos = []
    stats = {"comp": 0, "swap": 0, "write": 0}

    def _quick(low, high):
        if low < high:
            pivot = array[high]
            pasos.append({"tipo": "pivote", "indices": [high], "arreglo": list(array)})
            i = low - 1
            for j in range(low, high):
                stats["comp"] += 1
                pasos.append({"tipo": "comparacion", "indices": [j, high], "arreglo": list(array)})
                if array[j] < pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]
                    stats["swap"] += 1
                    stats["write"] += 2
                    pasos.append({"tipo": "intercambio", "indices": [i, j], "arreglo": list(array)})
            array[i + 1], array[high] = array[high], array[i + 1]
            stats["swap"] += 1
            stats["write"] += 2
            pasos.append({"tipo": "colocado", "indices": [i + 1], "arreglo": list(array)})
            pi = i + 1

            _quick(low, pi - 1)
            _quick(pi + 1, high)

    inicio = time.perf_counter()
    _quick(0, len(array) - 1)
    tiempo = time.perf_counter() - inicio
    pasos.append({"tipo": "final", "indices": [], "arreglo": list(array)})

    return {
        "pasos": pasos,
        "comparaciones": stats["comp"],
        "intercambios": stats["swap"],
        "escrituras": stats["write"],
        "tiempo_ejecucion": tiempo
    }

def merge_sort(arr):
    array = copy.deepcopy(arr)
    pasos = []
    stats = {"comp": 0, "swap": 0, "write": 0}

    def _merge_sort(l, r):
        if l < r:
            m = (l + r) // 2
            _merge_sort(l, m)
            _merge_sort(m + 1, r)
            
            left = array[l:m + 1]
            right = array[m + 1:r + 1]
            
            i = j = 0
            k = l
            while i < len(left) and j < len(right):
                stats["comp"] += 1
                pasos.append({"tipo": "comparacion", "indices": [l + i, m + 1 + j], "arreglo": list(array)})
                if left[i] <= right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                stats["write"] += 1
                pasos.append({"tipo": "escritura", "indices": [k], "arreglo": list(array)})
                k += 1
                
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
                stats["write"] += 1
                pasos.append({"tipo": "escritura", "indices": [k - 1], "arreglo": list(array)})
                
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
                stats["write"] += 1
                pasos.append({"tipo": "escritura", "indices": [k - 1], "arreglo": list(array)})

    inicio = time.perf_counter()
    _merge_sort(0, len(array) - 1)
    tiempo = time.perf_counter() - inicio
    pasos.append({"tipo": "final", "indices": [], "arreglo": list(array)})

    return {
        "pasos": pasos,
        "comparaciones": stats["comp"],
        "intercambios": stats["swap"],
        "escrituras": stats["write"],
        "tiempo_ejecucion": tiempo
    }


# ==========================================
# 2. SERVIDOR FLASK DE APP.PY
# ==========================================

app = Flask(__name__)
CORS(app)

ALGORITMOS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Exchange Sort": exchange_sort,
    "Gnome Sort": gnome_sort,
    "Stooge Sort": stooge_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort
}

TRADUCCION_ACCION = {
    "comparacion": "compare",
    "intercambio": "swap",
    "escritura": "write",
    "pivote": "pivot",
    "colocado": "pivot",
    "final": "done"
}

@app.route('/api/sort', methods=['POST'])
def sort_array():
    data = request.get_json()
    
    if not data or 'algorithm' not in data or 'array' not in data:
        return jsonify({"error": "Datos inválidos. Se requiere 'algorithm' y 'array'"}), 400

    nombre_algoritmo = data['algorithm']
    arreglo_original = data['array']

    if nombre_algoritmo not in ALGORITMOS:
        return jsonify({"error": f"Algoritmo '{nombre_algoritmo}' no soportado."}), 400

    funcion_sort = ALGORITMOS[nombre_algoritmo]
    resultado_raw = funcion_sort(arreglo_original)

    pasos_adaptados = []
    for paso in resultado_raw.get("pasos", []):
        pasos_adaptados.append({
            "action": TRADUCCION_ACCION.get(paso.get("tipo"), "compare"),
            "indices": paso.get("indices", []),
            "array": paso.get("arreglo", [])
        })

    respuesta = {
        "steps": pasos_adaptados,
        "statistics": {
            "comparisons": resultado_raw.get("comparaciones", 0),
            "swaps": resultado_raw.get("intercambios", 0),
            "writes": resultado_raw.get("escrituras", 0),
            "time": float(f"{resultado_raw.get('tiempo_ejecucion', 0):.4f}")
        }
    }

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5005, debug=True)