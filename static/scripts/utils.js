import { state } from './state.js';
const sleep = async (ms) => {
    await new Promise((resolve) => setTimeout(resolve, ms));
};
const waitForNext = async () => {
    await new Promise((resolve) => {
        function onButtonClick(e) {
            state.currentButton?.removeEventListener('click', onButtonClick);
            state.currentButton = null;
            state.currentListener = null;
            resolve();
        }
        if (state.currentButton != null && state.currentListener != null) {
            state.currentButton.removeEventListener('click', state.currentListener);
        }
        const forwardButton = document.getElementById('fwd');
        forwardButton.addEventListener('click', onButtonClick);
        state.currentListener = onButtonClick;
        state.currentButton = forwardButton;
    });
};
function resetDOMTable(state) {
    const DOMTable = document.getElementById('table');
    DOMTable.innerHTML = '';
    if (state.currentButton != null && state.currentListener != null) {
        state.currentButton.removeEventListener('click', state.currentListener);
        state.currentListener = null;
        state.currentButton = null;
    }
}
function createDOMTable(table, maxWeight) {
    const DOMTable = document.getElementById('table');
    const DOMTableHeader = document.getElementById('table-header');
    DOMTableHeader.style.gridTemplateColumns = `repeat(${maxWeight}, 1fr)`;
    DOMTable.style.gridTemplateRows = `repeat(${table.length}, 1fr)`;
    for (let i = 0; i < maxWeight; i++) {
        const headerCell = document.createElement('div');
        headerCell.classList.add('header-cell');
        headerCell.textContent = `${i}`;
        DOMTableHeader.append(headerCell);
    }
    let arrayIncr = 0;
    table.forEach((array) => {
        const DOMArray = document.createElement('div');
        DOMArray.classList.add('sub-array');
        DOMArray.dataset.array = `${arrayIncr}`;
        DOMArray.style.gridTemplateColumns = `repeat(${array.length}, 1fr)`;
        DOMTable.append(DOMArray);
        let cellIncr = 0;
        array.forEach((cell) => {
            const DOMCell = document.createElement('div');
            DOMCell.classList.add('cell');
            DOMCell.dataset.cell = `${cellIncr}`;
            cellIncr += 1;
            DOMArray.append(DOMCell);
        });
        arrayIncr += 1;
    });
}
export { sleep, waitForNext, createDOMTable, resetDOMTable };
