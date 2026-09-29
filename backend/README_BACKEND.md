# Guía de integración Frontend ⇄ Backend (ChronoSort)

Este documento explica lo que necesita el backend en Python (Flask o FastAPI) para funcionar con la interfaz gráfica.

## Estructura del frontend

```
frontend/
├── index.html          # Estructura principal e importación de scripts/estilos
├── css/
│   └── styles.css      # Diseño visual y paleta retro-futurista
└── js/
    ├── api.js          # Conexión exclusiva con el backend  ← ÚNICO archivo que toca el backend
    ├── animation.js    # Renderizado de barras y colores
    └── app.js          # UI, eventos, botones y ciclo principal
```

Orden de carga (estricto) en `index.html`: `api.js` → `animation.js` → `app.js`.

> Para probar, basta con abrir `index.html` en el navegador. También puede servirse con
> `python -m http.server 8080` dentro de la carpeta `frontend/`.

---

## Paso 1: Configurar CORS (obligatorio)

El frontend se abre en un origen (por ejemplo `http://localhost:8080` o `file://`) y el servidor corre en otro puerto (`http://localhost:5000`). Sin CORS, el navegador bloquea las peticiones.

### Flask

```bash
pip install flask flask-cors
```

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # habilita CORS para todas las rutas
```

### FastAPI

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # en producción, restringir al origen del frontend
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Paso 2: Endpoint `POST /api/sort`

La API debe estar montada en **`POST /api/sort`**, en el puerto **5000**.
Si se usa otra ruta o puerto, cambiar la constante `API_URL` en **`js/api.js` (línea 32)**, dentro de la función `fetchAlgorithmDataFromBackend()`:

```js
const API_URL = 'http://localhost:5000/api/sort';
```

### Request (JSON)

El frontend hace **una petición por cada algoritmo seleccionado** (hasta 4), siempre con el mismo arreglo base:

```json
{
  "algorithm": "Bubble Sort",
  "array": [45, 12, 89, 5]
}
```

Nombres exactos válidos para `algorithm` (respetar mayúsculas y espacios):

`"Bubble Sort"`, `"Selection Sort"`, `"Insertion Sort"`, `"Exchange Sort"`, `"Gnome Sort"`, `"Merge Sort"`, `"Quick Sort"`, `"Stooge Sort"`

### Response (JSON)

Debe devolver el arreglo original, el diccionario de estadísticas y la lista de pasos. **Los nombres de las claves deben ser exactamente estos** (son los que lee `js/app.js`):

```json
{
  "algorithm": "Bubble Sort",
  "original_array": [45, 12, 89, 5],
  "statistics": {
    "comparisons": 6,
    "swaps": 4,
    "writes": 0,
    "time": 0.0012
  },
  "steps": [
    { "action": "compare", "indices": [0, 1], "array": [45, 12, 89, 5] },
    { "action": "swap",    "indices": [0, 1], "array": [12, 45, 89, 5] },
    { "action": "done",    "indices": [3],    "array": [12, 45, 5, 89] }
  ]
}
```

**Claves obligatorias que el frontend consume:**

| Clave                     | Tipo     | Uso en el frontend                                                       |
|---------------------------|----------|--------------------------------------------------------------------------|
| `steps`                   | `object[]` | Lista de pasos a animar (`steps.length` se muestra como "N / total")   |
| `statistics.comparisons`  | `int`    | Contador final y tabla de resultados                                     |
| `statistics.swaps`        | `int`    | Contador final y tabla de resultados                                     |
| `statistics.writes`       | `int`    | Contador final y tabla de resultados                                     |
| `statistics.time`         | `number` | Tiempo en **segundos**; se muestra como `${time}s` en la tabla           |

`algorithm` y `original_array` son informativos: el frontend actualmente no los lee, pero conviene incluirlos.

**Cada objeto de `steps` contiene:**

| Campo     | Tipo     | Descripción                                                                  |
|-----------|----------|------------------------------------------------------------------------------|
| `array`   | `int[]`  | Estado **completo** del arreglo después de ese paso                           |
| `indices` | `int[]`  | Posiciones involucradas en el paso (las que se resaltan)                      |
| `action`  | `string` | Uno de: `compare`, `swap`, `write`, `pivot`, `done`                           |

Colores en pantalla según `action`: `compare` → `.color-compare`, `swap` → `.color-swap`, `write` → `.color-write`, `pivot` → `.color-pivot`, `done` → `.color-done`.

Notas:
- Un paso con `action: "done"` marca **permanentemente** sus `indices` como ordenados (verde). Conviene emitirlos a medida que cada posición queda en su lugar final.
- Mientras se anima, el frontend cuenta por su cuenta los `compare`, `swap` y `write` de los pasos; al terminar, muestra los valores de `statistics`. Ambos deberían coincidir.

### Manejo de errores

Si el servidor responde con un código distinto de 2xx, o no responde, el frontend muestra **"ERROR DE CONEXIÓN"** en el panel del algoritmo y deja el detalle en la consola del navegador (F12).

---

## Ejemplo mínimo

### Flask

```python
@app.route("/api/sort", methods=["POST"])
def sort():
    body = request.get_json()
    algorithm, array = body["algorithm"], body["array"]
    return jsonify(run_algorithm(algorithm, array))  # devuelve el JSON descrito arriba
```

### FastAPI

```python
from pydantic import BaseModel

class SortRequest(BaseModel):
    algorithm: str
    array: list[int]

@app.post("/api/sort")
def sort(req: SortRequest):
    return run_algorithm(req.algorithm, req.array)
```

## Checklist

- [ ] CORS habilitado
- [ ] `POST /api/sort` en el puerto 5000 (o `API_URL` actualizado en `js/api.js`)
- [ ] Los 8 nombres de algoritmo reconocidos exactamente como arriba
- [ ] La respuesta incluye `steps` y `statistics` (`comparisons`, `swaps`, `writes`, `time`)
- [ ] Cada `step` incluye `array`, `indices` y `action`
- [ ] Se probó con arreglos de 5 a 100 elementos (el slider del frontend lo permite)
