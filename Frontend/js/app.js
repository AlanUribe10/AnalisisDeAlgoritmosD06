/* ==========================================
   SECCIÓN: js/app.js
   ========================================== */

const state = {
    baseArray: [],
    arraySize: 20,
    speed: 50, 
    status: 'idle', 
    selectedAlgorithms: [], 
    instances: [], 
    maxAlgorithms: 4
};

const DOM = {
    selectorsContainer: document.getElementById('selectors-container'),
    btnAddAlgo: document.getElementById('btn-add-algo'),
    sliderSize: document.getElementById('array-size'),
    labelSize: document.getElementById('size-val'),
    sliderSpeed: document.getElementById('anim-speed'),
    labelSpeed: document.getElementById('speed-val'),
    btnGenerate: document.getElementById('btn-generate'),
    btnStart: document.getElementById('btn-start'),
    btnPause: document.getElementById('btn-pause'),
    btnReset: document.getElementById('btn-reset'),
    gridAnimations: document.getElementById('animations-grid'),
    resultsBody: document.getElementById('results-tbody')
};

function generateRandomArray(size) {
    const arr = [];
    for (let i = 0; i < size; i++) {
        arr.push(Math.floor(Math.random() * 100) + 1);
    }
    return arr;
}

function getDelay() {
    const minDelay = 10;
    const maxDelay = 800;
    const percent = (100 - state.speed) / 100;
    return Math.floor(minDelay + percent * (maxDelay - minDelay));
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function initApp() {
    state.baseArray = generateRandomArray(state.arraySize);
    addAlgorithmSelector("Bubble Sort"); 
    addAlgorithmSelector("Merge Sort");  
    updateUI();
}

function addAlgorithmSelector(defaultAlgo = AVAILABLE_ALGORITHMS[0]) {
    if (state.selectedAlgorithms.length >= state.maxAlgorithms) return;
    const id = `selector-${Date.now()}`;
    state.selectedAlgorithms.push({ id, name: defaultAlgo });
    renderSelectors();
    resetSystem(); 
}

function removeAlgorithmSelector(idToRemove) {
    if (state.selectedAlgorithms.length <= 1) return; 
    state.selectedAlgorithms = state.selectedAlgorithms.filter(s => s.id !== idToRemove);
    renderSelectors();
    resetSystem();
}

function renderSelectors() {
    DOM.selectorsContainer.innerHTML = '';
    state.selectedAlgorithms.forEach((selector, index) => {
        const label = LABELS[index];
        const div = document.createElement('div');
        div.className = "flex items-center gap-2 bg-[#1a1a1a] p-1 border border-[#333]";
        
        const spanLabel = document.createElement('span');
        spanLabel.className = "text-[#ff8c00] font-bold px-2";
        spanLabel.innerText = label;
        div.appendChild(spanLabel);
        
        const select = document.createElement('select');
        select.className = "flex-grow bg-transparent text-[#fff] outline-none text-xs border-none cursor-pointer";
        
        AVAILABLE_ALGORITHMS.forEach(algo => {
            const option = document.createElement('option');
            option.value = algo;
            option.innerText = algo;
            if (algo === selector.name) option.selected = true;
            select.appendChild(option);
        });

        select.addEventListener('change', (e) => {
            selector.name = e.target.value;
            resetSystem();
        });

        div.appendChild(select);

        if (state.selectedAlgorithms.length > 1) {
            const btnDel = document.createElement('button');
            btnDel.innerHTML = '×';
            btnDel.className = "w-6 h-6 flex items-center justify-center text-[#ff3333] border border-[#ff3333] hover:bg-[#ff3333] hover:text-white transition text-lg leading-none";
            btnDel.onclick = () => removeAlgorithmSelector(selector.id);
            div.appendChild(btnDel);
        }

        DOM.selectorsContainer.appendChild(div);
    });

    DOM.btnAddAlgo.style.display = state.selectedAlgorithms.length >= state.maxAlgorithms ? 'none' : 'block';
    
    const numAlgos = state.selectedAlgorithms.length;
    DOM.gridAnimations.className = `grid gap-4 ${numAlgos > 1 ? 'xl:grid-cols-2' : 'grid-cols-1'}`;
}

function buildAnimationPanels() {
    DOM.gridAnimations.innerHTML = '';
    
    state.selectedAlgorithms.forEach((selector) => {
        const info = ALGORITHMS_INFO[selector.name];
        const panel = document.createElement('div');
        panel.className = "cyber-panel flex flex-col";
        
        panel.innerHTML = `
            <div class="flex flex-col p-4 pb-0">
                <div class="flex justify-between items-start mb-2">
                    <div>
                        <h3 class="text-xl font-bold text-[#fff]">${selector.name}</h3>
                        <span class="text-[10px] text-[#ff8c00] border border-[#ff8c00] px-1 rounded-sm">${info.complexity}</span>
                    </div>
                    <div class="text-right text-[10px] text-[#888] flex flex-col gap-[2px]">
                        <div class="flex justify-between gap-6"><span>Comparaciones:</span> <span id="comp-${selector.id}" class="text-[#ff8c00] font-bold">000</span></div>
                        <div class="flex justify-between gap-6"><span>Intercambios:</span> <span id="swap-${selector.id}" class="text-[#ff8c00] font-bold">000</span></div>
                        <div class="flex justify-between gap-6"><span>Escrituras:</span> <span id="write-${selector.id}" class="text-[#ff8c00] font-bold">000</span></div>
                    </div>
                </div>
                
                <div class="flex justify-between items-center text-[9px] border-b border-t border-[#333] py-1 mt-2">
                    <div>STATUS: <span id="status-${selector.id}" class="text-[#ff8c00]">INITIALIZED</span></div>
                    <div>PASO: <span id="step-${selector.id}">0 / ?</span></div>
                </div>
            </div>
            
            <div class="p-4 pt-2">
                <div id="bars-${selector.id}" class="bar-container w-full h-[200px]"></div>
            </div>
        `;
        
        DOM.gridAnimations.appendChild(panel);
        renderBarsInitial(selector.id, state.baseArray);
    });
}

DOM.sliderSize.addEventListener('input', (e) => {
    DOM.labelSize.innerText = e.target.value;
    state.arraySize = parseInt(e.target.value);
    state.baseArray = generateRandomArray(state.arraySize);
    resetSystem();
});

DOM.sliderSpeed.addEventListener('input', (e) => {
    state.speed = parseInt(e.target.value);
    DOM.labelSpeed.innerText = `${state.speed}%`;
});

DOM.btnGenerate.addEventListener('click', () => {
    state.baseArray = generateRandomArray(state.arraySize);
    resetSystem();
});

DOM.btnAddAlgo.addEventListener('click', () => {
    addAlgorithmSelector();
});

DOM.btnReset.addEventListener('click', () => {
    resetSystem();
});

DOM.btnPause.addEventListener('click', () => {
    if (state.status === 'playing') {
        state.status = 'paused';
        updateButtons();
        state.instances.forEach(inst => {
            if(!inst.finished) {
                document.getElementById(`status-${inst.id}`).innerText = "PAUSED";
                document.getElementById(`status-${inst.id}`).className = "text-[#ff3333]";
            }
        });
    }
});

DOM.btnStart.addEventListener('click', async () => {
    if (state.status === 'playing') return;
    
    if (state.status === 'idle') {
        state.status = 'playing';
        updateButtons();
        DOM.resultsBody.innerHTML = '<tr><td colspan="6" class="px-4 py-4 text-center text-[#ff8c00] animate-pulse">ESPERANDO RESPUESTA DEL SERVIDOR...</td></tr>';
        
        state.instances = [];
        let hasErrors = false;
        
        for (let i=0; i<state.selectedAlgorithms.length; i++) {
            let selector = state.selectedAlgorithms[i];
            document.getElementById(`status-${selector.id}`).innerText = "AWAITING BACKEND...";
            document.getElementById(`status-${selector.id}`).className = "text-[#33ccff] animate-pulse";

            // Llamada al backend
            const responseData = await fetchAlgorithmDataFromBackend(selector.name, state.baseArray);
            
            if(responseData) {
                state.instances.push({
                    id: selector.id,
                    name: selector.name,
                    label: LABELS[i],
                    data: responseData,
                    currentStepIndex: 0,
                    maxVal: Math.max(...state.baseArray),
                    doneIndices: new Set(),
                    finished: false
                });
                document.getElementById(`step-${selector.id}`).innerText = `0 / ${responseData.steps.length}`;
                document.getElementById(`status-${selector.id}`).innerText = "PROCESSING...";
            } else {
                // Manejo de error si el servidor no responde
                document.getElementById(`status-${selector.id}`).innerText = "ERROR DE CONEXIÓN";
                document.getElementById(`status-${selector.id}`).className = "text-[#ff3333]";
                hasErrors = true;
            }
        }
        
        if(hasErrors && state.instances.length === 0) {
            DOM.resultsBody.innerHTML = '<tr><td colspan="6" class="px-4 py-4 text-center text-[#ff3333]">NO SE PUDO CONECTAR AL SERVIDOR BACKEND (VER CONSOLA).</td></tr>';
            state.status = 'idle';
            updateButtons();
            return;
        }

        DOM.resultsBody.innerHTML = '';
        runAnimations();

    } else if (state.status === 'paused') {
        state.status = 'playing';
        updateButtons();
        
        state.instances.forEach(inst => {
            if(!inst.finished) {
                document.getElementById(`status-${inst.id}`).innerText = "PROCESSING...";
                document.getElementById(`status-${inst.id}`).className = "text-[#33ccff] animate-pulse";
            }
        });
        
        runAnimations();
    }
});

function updateButtons() {
    DOM.btnStart.disabled = (state.status === 'playing');
    DOM.btnPause.disabled = (state.status !== 'playing');
    DOM.btnGenerate.disabled = (state.status !== 'idle');
    DOM.sliderSize.disabled = (state.status !== 'idle');
}

function resetSystem() {
    state.status = 'idle';
    state.instances = [];
    updateButtons();
    buildAnimationPanels();
    DOM.resultsBody.innerHTML = '<tr><td colspan="6" class="px-4 py-6 text-center text-[#555] italic">INICIE LA SECUENCIA PARA OBTENER TELEMETRÍA DEL SERVIDOR.</td></tr>';
}

function updateUI() {
    renderSelectors();
    buildAnimationPanels();
    updateButtons();
}

async function runAnimations() {
    let allFinished = false;

    while (state.status === 'playing' && !allFinished) {
        let anyActive = false;

        for (let instance of state.instances) {
            if (instance.currentStepIndex < instance.data.steps.length) {
                anyActive = true;
                const stepData = instance.data.steps[instance.currentStepIndex];
                
                if(stepData.action === 'done' && stepData.indices) {
                    stepData.indices.forEach(idx => instance.doneIndices.add(idx));
                }

                let currentComps = parseInt(document.getElementById(`comp-${instance.id}`).innerText);
                let currentSwaps = parseInt(document.getElementById(`swap-${instance.id}`).innerText);
                let currentWrites = parseInt(document.getElementById(`write-${instance.id}`).innerText);
                
                if(stepData.action === 'compare') currentComps++;
                if(stepData.action === 'swap') currentSwaps++;
                if(stepData.action === 'write') currentWrites++;

                const stepStr = `${instance.currentStepIndex + 1} / ${instance.data.steps.length}`;
                
                updateStatsUI(instance.id, currentComps, currentSwaps, currentWrites, stepStr);
                renderStep(instance.id, stepData, instance.maxVal, instance.doneIndices);
                
                instance.currentStepIndex++;
            } else if (!instance.finished) {
                instance.finished = true;
                renderFinished(instance.id);
                
                updateStatsUI(instance.id, 
                    instance.data.statistics.comparisons, 
                    instance.data.statistics.swaps, 
                    instance.data.statistics.writes,
                    `${instance.data.steps.length} / ${instance.data.steps.length}`
                );
                
                addResultRow(instance);
            }
        }

        allFinished = !anyActive;

        if (allFinished) {
            state.status = 'finished';
            updateButtons();
        } else {
            await sleep(getDelay());
        }
    }
}

function addResultRow(instance) {
    const stats = instance.data.statistics;
    const info = ALGORITHMS_INFO[instance.name];
    
    const tr = document.createElement('tr');
    tr.innerHTML = `
        <td class="px-4 py-2 text-[#fff]">
            <span class="text-[#ff8c00] font-bold mr-2">${instance.label}</span>${instance.name}
        </td>
        <td class="px-4 py-2">${stats.comparisons}</td>
        <td class="px-4 py-2">${stats.swaps}</td>
        <td class="px-4 py-2">${stats.writes}</td>
        <td class="px-4 py-2 text-[#33ccff]">${stats.time}s</td>
        <td class="px-4 py-2">
            <span class="border border-[#555] px-2 py-0.5 text-[10px] text-[#888]">${info.complexity}</span>
        </td>
    `;
    DOM.resultsBody.appendChild(tr);
}

window.onload = initApp;
