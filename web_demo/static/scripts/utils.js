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
export { sleep, waitForNext };
