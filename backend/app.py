from flask import Flask, request, jsonify
from flask_cors import CORS
import backend

app = Flask(__name__)
CORS(app)  # Permite que el frontend (JS) se comunique sin bloqueos CORS

# Mapeo de nombres que vienen del Frontend a las funciones de backend.py
ALGORITMOS = {
    "Bubble Sort": backend.bubble_sort,
    "Selection Sort": backend.selection_sort,
    "Insertion Sort": backend.insertion_sort,
    "Exchange Sort": backend.exchange_sort,
    "Gnome Sort": backend.gnome_sort,
    "Stooge Sort": backend.stooge_sort,
    "Quick Sort": backend.quick_sort,
    "Merge Sort": backend.merge_sort
}

# Traducción de los tipos de pasos del backend de Python a lo que espera tu JavaScript
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

    # 1. Ejecutar el algoritmo correspondiente desde backend.py
    funcion_sort = ALGORITMOS[nombre_algoritmo]
    resultado_raw = funcion_sort(arreglo_original)

    # 2. Mapear y adaptar los pasos al formato esperado por el frontend JS
    pasos_adaptados = []
    for paso in resultado_raw.get("pasos", []):
        pasos_adaptados.append({
            "action": TRADUCCION_ACCION.get(paso.get("tipo"), "compare"),
            "indices": paso.get("indices", []),
            "array": paso.get("arreglo", [])
        })

    # 3. Mapear y adaptar las estadísticas
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
    # El servidor escuchará en http://localhost:5005
    app.run(host='127.0.0.1', port=5005, debug=True)