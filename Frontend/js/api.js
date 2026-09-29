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

async function fetchAlgorithmDataFromBackend(algorithmName, array) {
    const API_URL = '/api/sort';

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