import { handleFastForwardWrapper, handleResetWrapper, handleStartWrapper } from './eventHandlers.js'
import { populateDOMItems } from './dom.js'

const form = document.getElementById('weight-form') as HTMLFormElement
const resetButton = document.getElementById('reset') as HTMLButtonElement
const ffwdButton = document.getElementById('ffwd') as HTMLButtonElement

form.addEventListener('submit', handleStartWrapper)
resetButton.addEventListener('click', handleResetWrapper)
ffwdButton.addEventListener('click', handleFastForwardWrapper)

populateDOMItems()

