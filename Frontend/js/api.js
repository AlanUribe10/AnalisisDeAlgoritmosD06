/* ==========================================
   SECCIÓN: js/api.js (Conexión con el backend)
   ========================================== */

// Diccionario base solo para etiquetas de complejidad y selectores
const ALGORITHMS_INFO = {
    "Bubble Sort": { complexity: "O(n²)" },
    "Selection Sort": { complexity: "O(n²)" },
    "Insertion Sort": { complexity: "O(n²)" },
    "Exchange Sort": { complexity: "O(n²)" },
    "Gnome Sort": { complexity: "O(n²)" },
    "Merge Sort": { complexity: "O(n log n)" },
    "Quick Sort": { complexity: "O(n log n)" },
    "Stooge Sort": { complexity: "O(n^(log 3 / log 1.5))" }
};

const AVAILABLE_ALGORITHMS = Object.keys(ALGORITHMS_INFO);
const LABELS = ['[A]', '[B]', '[C]', '[D]'];

/**
 * Función encargada de comunicarse con Flask/FastAPI
 * @param {string} algorithmName - Nombre del algoritmo a ejecutar
 * @param {Array} array - Arreglo numérico a ordenar
 * @returns {Object|null} - JSON con la respuesta o null si hay error
 */
async function fetchAlgorithmDataFromBackend(algorithmName, array) {
    
    // CONFIGURACIÓN PARA EL COMPAÑERO DE BACKEND:
    // 1. Asegúrate de que el puerto (5000) coincida con el de tu app Flask/FastAPI.
    // 2. Asegúrate de habilitar CORS en tu servidor backend.
    // 3. El endpoint debe recibir un POST con body: { "algorithm": "...", "array": [...] }
    const API_URL = 'http://localhost:5000/api/sort';

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                algorithm: algorithmName, 
                array: array 
            })
        });

        if (!response.ok) {
            throw new Error(`Error en el servidor: ${response.status}`);
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.error("Error conectando al backend de Python:", error);
        return null;
    }
}
