import { state } from './state.js'

const sleep = async (ms: number): Promise<void> => {
  await new Promise((resolve) => setTimeout(resolve, ms))
}

const waitForNext = async (): Promise<void> => {
  await new Promise<void>((resolve) => {
    function onButtonClick (e: MouseEvent): void {
      state.currentButton?.removeEventListener('click', onButtonClick)
      state.currentButton = null
      state.currentListener = null
      resolve()
    }

    if (state.currentButton != null && state.currentListener != null) {
      state.currentButton.removeEventListener('click', state.currentListener)
    }

    const forwardButton = document.getElementById('fwd') as HTMLButtonElement
    forwardButton.addEventListener('click', onButtonClick)
    state.currentListener = onButtonClick
    state.currentButton = forwardButton
  })
}

export { sleep, waitForNext }
