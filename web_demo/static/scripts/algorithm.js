import { sleep, waitForNext } from './utils.js';
import { state } from './state.js';
import { createDOMTable, DOMCell, selectDOMCell } from './dom.js';
export async function dynamicProgramming(items, capacity) {
    const table = Array(items.length + 1)
        .fill(0)
        .map(() => Array(capacity + 1).fill(0));
    createDOMTable(table, capacity);
    for (let i = 1; i <= items.length; i++) {
        for (let w = 1; w <= capacity; w++) {
            const cellDOMAddress = selectDOMCell(i, w);
            const Cell = new DOMCell(cellDOMAddress);
            await sleep(50);
            Cell.highlight();
            if (items[i - 1].weight <= w) {
                table[i][w] = Math.max(table[i - 1][w], items[i - 1].value + table[i - 1][w - items[i - 1].weight]);
            }
            else {
                table[i][w] = table[i - 1][w];
            }
            Cell.setValue(table[i][w]);
            await sleep(50);
            Cell.unHighlight();
            if (!state.play)
                await waitForNext();
        }
    }
    let result = table[items.length][capacity];
    let w = capacity;
    const combination = [];
    for (let i = items.length; i > 0 && result > 0; i--) {
        if (result !== table[i - 1][w]) {
            combination.push(items[i - 1]);
            result = result - items[i - 1].value;
            w = w - items[i - 1].weight;
        }
    }
}
