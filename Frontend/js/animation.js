/* ==========================================
   SECCIÓN: js/animation.js
   ========================================== */

function renderBarsInitial(containerId, array) {
    const container = document.getElementById(`bars-${containerId}`);
    if(!container) return;
    container.innerHTML = '';
    
    const maxVal = Math.max(...array);
    const labelRow = document.createElement('div');
    labelRow.className = "absolute top-2 w-full flex justify-around px-4 text-[9px] text-[#555] pointer-events-none hidden md:flex";
    const step = Math.ceil(array.length / 10);
    
    array.forEach((val, idx) => {
        const bar = document.createElement('div');
        bar.classList.add('array-bar', 'color-unprocessed');
        const heightPercent = (val / maxVal) * 90; 
        bar.style.height = `${Math.max(5, heightPercent)}%`; 
        bar.id = `bar-${containerId}-${idx}`;
        container.appendChild(bar);
        
        if (idx % step === 0) {
             const lbl = document.createElement('span');
             lbl.innerText = val;
             labelRow.appendChild(lbl);
        }
    });
    container.appendChild(labelRow);
}

function renderStep(containerId, stepData, maxVal, doneIndices) {
    const container = document.getElementById(`bars-${containerId}`);
    if(!container) return;
    
    stepData.array.forEach((val, idx) => {
        const bar = document.getElementById(`bar-${containerId}-${idx}`);
        if(bar) {
            bar.style.height = `${Math.max(5, (val / maxVal) * 90)}%`;
            bar.className = 'array-bar'; 
            if (doneIndices.has(idx)) {
                bar.classList.add('color-done');
            } else {
                bar.classList.add('color-unprocessed');
            }
        }
    });

    if (stepData.indices && stepData.indices.length > 0) {
        stepData.indices.forEach(idx => {
            const bar = document.getElementById(`bar-${containerId}-${idx}`);
            if(bar) {
                bar.className = 'array-bar'; 
                switch(stepData.action) {
                    case 'compare': bar.classList.add('color-compare'); break;
                    case 'swap': bar.classList.add('color-swap'); break;
                    case 'write': bar.classList.add('color-write'); break;
                    case 'pivot': bar.classList.add('color-pivot'); break;
                    case 'done': bar.classList.add('color-done'); break;
                }
            }
        });
    }
}

function renderFinished(containerId) {
    const container = document.getElementById(`bars-${containerId}`);
    if(!container) return;
    const bars = container.querySelectorAll('.array-bar');
    bars.forEach(bar => {
        bar.className = 'array-bar color-done';
    });
    document.getElementById(`status-${containerId}`).innerText = "COMPLETED";
    document.getElementById(`status-${containerId}`).className = "text-[#00cc66]";
}

function updateStatsUI(containerId, comps, swaps, writes, stepInfo) {
    document.getElementById(`comp-${containerId}`).innerText = comps.toString().padStart(3, '0');
    document.getElementById(`swap-${containerId}`).innerText = swaps.toString().padStart(3, '0');
    document.getElementById(`write-${containerId}`).innerText = writes.toString().padStart(3, '0');
    if(stepInfo) {
         document.getElementById(`step-${containerId}`).innerText = stepInfo;
    }
}
