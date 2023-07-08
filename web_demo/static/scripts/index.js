import { handleFastForwardWrapper, handleResetWrapper, handleStartWrapper } from './eventHandlers.js';
import { populateDOMItems } from './dom.js';
const form = document.getElementById('weight-form');
const resetButton = document.getElementById('reset');
const ffwdButton = document.getElementById('ffwd');
form.addEventListener('submit', handleStartWrapper);
resetButton.addEventListener('click', handleResetWrapper);
ffwdButton.addEventListener('click', handleFastForwardWrapper);
populateDOMItems();
