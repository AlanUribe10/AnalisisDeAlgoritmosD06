# AnalisisDeAlgoritmosD06
Repositorio en equipo para el comparador de algoritmos

# ChronoSort // Comparador de Algoritmos de Ordenamiento

Aplicación web educativa para **visualizar, ejecutar y comparar ocho algoritmos de ordenamiento**, con animación paso a paso y métricas calculadas por un servidor en Python.

**Aplicación en línea:** https://chronosortanalisisdealgoritmosd06.vercel.app/

---

## Integrantes

**Equipo:** Los Big-O
**Institución:** CUCEI — Ingeniería en Computación
**Materia:** Análisis de Algoritmos
**Profesor:** Jorge Ernesto López Arce Delgado
**Sección:** D06

| Integrante | Usuario de GitHub |
|---|---|
| Aldo Damián Gutiérrez Medina | Coffee2Donuts |
| Alan Arturo Uribe Pérez | AlanUribe10 |
| Karol Nungaray Escobedo |  |

---

## Descripción

ChronoSort es una interfaz web con estética retro-futurista que permite elegir hasta **cuatro algoritmos de ordenamiento** y ejecutarlos **al mismo tiempo sobre el mismo arreglo**, cada uno en su propio panel de animación. Cada elemento del arreglo se dibuja como una barra vertical cuya altura equivale a su valor, y el color de la barra indica qué está haciendo el algoritmo en ese momento (comparar, intercambiar, escribir, pivote u ordenado).

La aplicación está dividida en dos partes:

- **Frontend (navegador):** HTML, CSS y JavaScript. Genera el arreglo aleatorio, pide al servidor la ejecución de cada algoritmo y reproduce la animación.
- **Backend (Python + Flask):** implementa los algoritmos. Por cada ejecución devuelve, en formato JSON, la lista completa de pasos y las estadísticas (comparaciones, intercambios, escrituras y tiempo).

El navegador **no ordena nada por su cuenta**: solo dibuja los pasos que recibe. Esto separa la lógica de los algoritmos de la visualización.

## Objetivo

Desarrollar una herramienta interactiva que permita **entender cómo funciona cada algoritmo de ordenamiento y comparar su comportamiento**, observando la diferencia práctica entre los algoritmos de complejidad O(n²), los de O(n log n) y Stooge Sort, mediante animaciones y métricas medidas por el servidor.

---

## Algoritmos implementados

| Algoritmo | Complejidad (caso promedio) | Idea general |
|---|---|---|
| Bubble Sort | O(n²) | Compara elementos adyacentes e intercambia los desordenados; en cada pasada el mayor "sube" al final. |
| Selection Sort | O(n²) | Busca el mínimo del tramo restante y lo intercambia a su posición. Hace a lo sumo n−1 intercambios. |
| Insertion Sort | O(n²) | Toma cada elemento y lo desplaza hacia la izquierda hasta su lugar dentro de la parte ya ordenada. |
| Exchange Sort | O(n²) | Compara cada posición `i` con todas las posteriores `j` e intercambia si están desordenadas. |
| Gnome Sort | O(n²) | Con un solo índice: si el par está en orden avanza; si no, intercambia y retrocede. |
| Merge Sort | O(n log n) | Divide el arreglo en mitades recursivamente y las mezcla ordenadas usando arreglos auxiliares. |
| Quick Sort | O(n log n) | Elige el último elemento como pivote, separa menores y mayores y ordena cada lado recursivamente. |
| Stooge Sort | O(n^2.71) | Recursivo: ordena los primeros 2/3, los últimos 2/3 y de nuevo los primeros 2/3. Muy lento. |

**Métricas que se calculan para cada ejecución**

| Métrica | Qué cuenta |
|---|---|
| Comparaciones | Veces que se comparan dos elementos. |
| Intercambios | Veces que se intercambian dos posiciones. Merge Sort no intercambia, por lo que muestra 0. |
| Escrituras | Veces que se escribe un valor en el arreglo (un intercambio cuenta como 2 escrituras; Merge Sort cuenta cada valor copiado desde los arreglos auxiliares). |
| Tiempo backend | Segundos medidos en Python con `time.perf_counter()`. |

> El Quick Sort implementado usa el último elemento como pivote, por lo que su peor caso (arreglo ya ordenado) es O(n²). La complejidad mostrada corresponde al caso promedio.

---

## Tecnologías utilizadas

**Frontend**
- HTML5 y CSS3
- JavaScript (sin frameworks)
- Tailwind CSS (por CDN) para las clases de utilidad
- Google Fonts (Share Tech Mono)

**Backend**
- Python 3
- Flask (servidor web y endpoint `POST /api/sort`)
- Flask-CORS

**Herramientas y despliegue**
- Git y GitHub (ramas y GitHub Projects)
- Vercel (publicación del frontend y del backend)
- Visual Studio Code

### Estructura del repositorio

```
.
├── Frontend/
│   ├── index.html          # Estructura de la página
│   ├── css/styles.css      # Estilos y paleta retro-futurista
│   └── js/
│       ├── api.js          # Única conexión con el backend (fetch a /api/sort)
│       ├── animation.js    # Dibujo de barras y colores
│       └── app.js          # Estado, eventos, botones y ciclo de animación
├── api/
│   └── index.py            # Versión desplegada: algoritmos + servidor Flask
├── backend/                # Versión de desarrollo y pruebas del backend
│   ├── backend.py          # Funciones de los algoritmos
│   ├── app.py              # Servidor Flask
│   ├── pruebas.py          # Pruebas de los 8 algoritmos con 6 casos
│   └── README_BACKEND.md   # Contrato entre frontend y backend
├── requirements.txt        # Dependencias de Python
└── vercel.json             # Configuración de despliegue
```

### Contrato de la API

**Petición** — `POST /api/sort`

```json
{ "algorithm": "Bubble Sort", "array": [45, 12, 89, 5] }
```

**Respuesta**

```json
{
  "steps": [
    { "action": "compare", "indices": [0, 1], "array": [45, 12, 89, 5] },
    { "action": "swap",    "indices": [0, 1], "array": [12, 45, 89, 5] }
  ],
  "statistics": { "comparisons": 6, "swaps": 4, "writes": 8, "time": 0.0001 }
}
```

Cada paso trae el **arreglo completo** en ese instante. Las acciones posibles son `compare`, `swap`, `write`, `pivot` y `done`.

---

## Cómo ejecutar el proyecto

### Requisitos

- Python 3.9 o superior
- Git
- Un navegador web moderno
- Conexión a internet (Tailwind y la fuente se cargan desde CDN)

### Opción 1: usar la versión publicada

Abrir https://chronosortanalisisdealgoritmosd06.vercel.app/ — no requiere instalación.

### Opción 2: ejecutar en la computadora

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/AlanUribe10/AnalisisDeAlgoritmosD06.git
   cd AnalisisDeAlgoritmosD06
   ```

2. **Crear un entorno virtual e instalar dependencias**
   ```bash
   python -m venv venv
   venv\Scripts\activate          # Windows
   # source venv/bin/activate     # macOS / Linux
   pip install -r requirements.txt
   ```

3. **Iniciar el backend** (queda escuchando en `http://127.0.0.1:5005`)
   ```bash
   python api/index.py
   ```

4. **Apuntar el frontend al servidor local.** En producción, `Frontend/js/api.js` usa la ruta relativa `/api/sort`. Para pruebas locales, cambiar temporalmente esa línea a:
   ```js
   const API_URL = 'http://127.0.0.1:5005/api/sort';
   ```
   *(No subir este cambio al repositorio.)*

5. **Servir el frontend** en otra terminal:
   ```bash
   python -m http.server 8080 --directory Frontend
   ```
   y abrir http://localhost:8080.

### Ejecutar las pruebas del backend

Desde la raíz del repositorio:

```bash
python -m backend.pruebas
```

Prueba los 8 algoritmos con seis casos (arreglo normal, ordenado, inverso, con repetidos, de un elemento y vacío) y compara cada resultado contra `sorted()`.

---

## Uso de la aplicación

1. **Elegir algoritmos.** En *Algoritmos a comparar* selecciona el algoritmo de cada selector (A, B, ...). Con **+ Agregar algoritmo** se añaden hasta cuatro; el botón **×** elimina uno.
2. **Ajustar el tamaño del arreglo [N].** El deslizador va de 5 a 100 elementos. *Con Stooge Sort se recomienda un valor pequeño (30 o menos): con arreglos grandes genera cientos de miles de pasos y la respuesta del servidor es muy pesada.*
3. **Ajustar la velocidad** de la animación (1 % a 100 %).
4. **Generar arreglo** crea un nuevo arreglo aleatorio (valores de 1 a 100). Solo está disponible cuando no hay una ejecución en curso.
5. **Iniciar.** El navegador pide al servidor los pasos de cada algoritmo y comienza la animación. Todos los algoritmos avanzan al mismo tiempo sobre el mismo arreglo.
6. **Pausar / Reanudar.** Pausar detiene la animación; **Iniciar** la continúa desde donde quedó.
7. **Reiniciar** limpia las animaciones y la tabla para empezar de nuevo.

**Colores de las barras**

| Color | Significado |
|---|---|
| Gris | Sin procesar |
| Amarillo | Comparando |
| Rojo | Intercambio |
| Azul | Escritura / mezcla (Merge Sort) |
| Naranja | Pivote (Quick Sort) |
| Verde | Ordenado |

**Resultados.** Durante la ejecución, cada panel muestra sus contadores en vivo (comparaciones, intercambios, escrituras) y el paso actual (`PASO: n / total`). Al terminar cada algoritmo, se agrega una fila a la tabla **Resultados comparativos** con las métricas finales, el tiempo medido por el backend y la complejidad teórica.

---

## Deployment

La aplicación está publicada en **Vercel**, conectada al repositorio de GitHub:

- **URL pública:** https://chronosortanalisisdealgoritmosd06.vercel.app/
- El frontend (`Frontend/`) se sirve como sitio estático.
- El backend se ejecuta como función de Python a partir de `api/index.py`.
- `vercel.json` redirige las rutas `/api/*` a `api/index.py` y el resto de las rutas a `Frontend/`. Por eso el frontend y el backend comparten dominio y `api.js` usa la ruta relativa `/api/sort`.
- Vercel instala las dependencias listadas en `requirements.txt` (`flask` y `flask-cors`).
- Los cambios que se suben a la rama `main` se despliegan automáticamente.

---

## Organización del equipo

**Repositorio:** https://github.com/AlanUribe10/AnalisisDeAlgoritmosD06
**Tablero de trabajo (GitHub Projects):** https://github.com/users/AlanUribe10/projects/1/views/1

### Distribución de tareas (según el primer entregable)

| # | Tarea | Responsable(s) |
|---|---|---|
| 1 | Redacción del documento | Damián |
| 2 | Diseño de la interfaz | Alan, Karol y Damián |
| 3 | Creación del repositorio | Alan |
| 4 | Programación de la interfaz | Karol |
| 5 | Función para generar datos aleatorios | Alan |
| 6 | Algoritmos de fuerza bruta | Alan y Damián |
| 7 | Algoritmos avanzados | Alan y Damián |
| 8 | Programación de las comparaciones | Damián |
| 9 | Fase de pruebas | Karol y Alan|
| 10 | Obtener la URL pública | Alan |
| 11 | Documentación final en README | Damián |

### Ramas del repositorio

| Rama | Uso |
|---|---|
| `frontend` | Desarrollo de la interfaz gráfica |
| `backend` | Desarrollo de los algoritmos y las pruebas |
| `integracion` | Unión de frontend y backend |
| `main` | Versión estable que se despliega en Vercel |

---

## Uso de IA

**Herramientas utilizadas**

| Herramienta | Uso |
|---|---|
| Claude (Anthropic) | Apoyo en el frontend y backend|
| Gemini (Canvas) | Apoyo en el frontend|
| ChatGPT |
---

## Aprendizajes y conclusiones

**Aprendizajes técnicos**

- **Separar lógica y visualización.** Como el backend devuelve una foto del arreglo por cada paso, el frontend no necesita conocer cómo funciona cada algoritmo; solo dibuja lo que recibe. El costo es el tamaño de la respuesta.
- **El contrato entre frontend y backend debe ser exacto.** Los nombres de las claves (`steps`, `statistics`, `action`, `indices`, `array`) y de los algoritmos tienen que coincidir en ambos lados; el backend traduce sus tipos de paso en español a las acciones en inglés que espera el frontend.
- **Despliegue.** Al servir frontend y backend desde el mismo dominio en Vercel se evitó depender de un puerto distinto, aunque en local sigue haciendo falta habilitar CORS.
- **Medir tiempos pequeños es difícil.** Con arreglos chicos los algoritmos tardan microsegundos; el resultado se ve afectado por el redondeo, por el ruido de cada ejecución y por el costo de registrar los pasos para la animación. Las comparaciones de tiempo son más confiables con arreglos grandes.

**Conclusiones sobre los algoritmos**

- Los algoritmos de O(n log n) (Merge Sort y Quick Sort) necesitan muchísimos menos pasos que los de O(n²): con N = 100, Bubble Sort genera del orden de 7,000 pasos frente a poco más de 1,000 de Merge Sort y Quick Sort.
- Los algoritmos O(n²) no son iguales entre sí. Selection Sort realiza pocos intercambios, mientras que Exchange Sort y Bubble Sort realizan muchos.
- Merge Sort no intercambia: copia valores a arreglos auxiliares, por eso se cuentan **escrituras** en lugar de intercambios.
- Stooge Sort, con complejidad cercana a O(n^2.71), es poco práctico: en pruebas locales con N = 100 generó más de 250,000 pasos y una respuesta de decenas de megabytes. Por eso se recomienda usarlo con arreglos pequeños.
- La complejidad teórica describe el crecimiento del trabajo, pero el tiempo real también depende de los datos (por ejemplo, el pivote de Quick Sort) y de la implementación.

**Trabajo en equipo**

- El uso de ramas separadas (`frontend`, `backend`, `integracion`, `main`) permitió trabajar en paralelo y unir los resultados al final.
