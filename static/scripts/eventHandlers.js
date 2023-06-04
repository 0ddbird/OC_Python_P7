import { dynamicProgramming } from './algorithm.js';
import { items } from './demo_data.js';
import { state } from './state.js';
import { resetDOMTable } from './dom.js';
async function handleFastForward(e) {
    const ffwdButton = document.getElementById('ffwd');
    const fwdIcon = document.getElementById('fwd-icon');
    const playIcon = document.getElementById('play-icon');
    fwdIcon.classList.toggle('hidden');
    playIcon.classList.toggle('hidden');
    ffwdButton.classList.toggle('pressed');
    state.play = !state.play;
}
async function handleStart(e) {
    e.preventDefault();
    resetDOMTable(state);
    state.inProgress = true;
    const weightInput = document.getElementById('weight-input');
    const maxWeight = parseInt(weightInput.value);
    await dynamicProgramming(items, maxWeight);
}
async function handleReset(e) {
    if (state.resetInProgress)
        return;
    state.resetInProgress = true;
    resetDOMTable(state);
    state.resetInProgress = false;
    const weightInput = document.getElementById('weight-input');
    const maxWeight = parseInt(weightInput.value);
    await dynamicProgramming(items, maxWeight);
}
function handleFastForwardWrapper(e) {
    handleFastForward(e).catch((error) => { console.error('An error occurred in handleFastForward:', error); });
}
const handleStartWrapper = (e) => {
    handleStart(e).catch((error) => { console.error('An error occurred in handleStart:', error); });
};
const handleResetWrapper = (e) => {
    handleReset(e).catch((error) => { console.error('An error occurred in handleReset:', error); });
};
export { handleStartWrapper, handleResetWrapper, handleFastForwardWrapper };
