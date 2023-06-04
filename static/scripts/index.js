import { handleFastForwardWrapper, handleResetWrapper, handleStartWrapper } from './eventHandlers.js';
import { items } from './demo_data.js';
const form = document.getElementById('weight-form');
const resetButton = document.getElementById('reset');
const ffwdButton = document.getElementById('ffwd');
form.addEventListener('submit', handleStartWrapper);
resetButton.addEventListener('click', handleResetWrapper);
ffwdButton.addEventListener('click', handleFastForwardWrapper);
const itemsDiv = document.getElementById('items');
items.forEach((item, index) => {
    const itemDiv = document.createElement('div');
    itemDiv.className = 'item';
    itemDiv.dataset.itemid = `${index}`;
    const nameDiv = document.createElement('div');
    nameDiv.className = 'item-number';
    nameDiv.textContent = `Item ${index + 1}`;
    const weightDiv = document.createElement('div');
    weightDiv.className = 'item-weight';
    weightDiv.textContent = `${item.weight}`;
    const valueDiv = document.createElement('div');
    valueDiv.className = 'item-value';
    valueDiv.textContent = `${item.value}`;
    itemDiv.appendChild(nameDiv);
    itemDiv.appendChild(weightDiv);
    itemDiv.appendChild(valueDiv);
    if (itemsDiv == null)
        return;
    itemsDiv.appendChild(itemDiv);
});
