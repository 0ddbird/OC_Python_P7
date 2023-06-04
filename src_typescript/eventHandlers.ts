import { dynamicProgramming } from './algorithm.js'
import { items } from './demo_data.js'
import { state } from './state.js'
import { resetDOMTable } from './dom.js'

async function handleFastForward (e: MouseEvent): Promise<void> {
  const ffwdButton = document.getElementById('ffwd') as HTMLButtonElement
  const fwdIcon = document.getElementById('fwd-icon') as HTMLButtonElement
  const playIcon = document.getElementById('play-icon') as HTMLButtonElement
  fwdIcon.classList.toggle('hidden')
  playIcon.classList.toggle('hidden')
  ffwdButton.classList.toggle('pressed')

  state.play = !state.play
}

async function handleStart (e: SubmitEvent): Promise<void> {
  e.preventDefault()
  resetDOMTable(state)
  state.inProgress = true
  const weightInput = document.getElementById('weight-input') as HTMLInputElement
  const maxWeight = parseInt(weightInput.value)
  await dynamicProgramming(items, maxWeight)
}

async function handleReset (e: MouseEvent): Promise<void> {
  if (state.resetInProgress) return
  state.resetInProgress = true
  resetDOMTable(state)
  state.resetInProgress = false
  const weightInput = document.getElementById(
    'weight-input'
  ) as HTMLInputElement
  const maxWeight = parseInt(weightInput.value)
  await dynamicProgramming(items, maxWeight)
}

function handleFastForwardWrapper (e: MouseEvent): void {
  handleFastForward(e).catch((error) => { console.error('An error occurred in handleFastForward:', error) })
}

const handleStartWrapper = (e: SubmitEvent): void => {
  handleStart(e).catch((error) => { console.error('An error occurred in handleStart:', error) })
}

const handleResetWrapper = (e: MouseEvent): void => {
  handleReset(e).catch((error) => { console.error('An error occurred in handleReset:', error) })
}

export { handleStartWrapper, handleResetWrapper, handleFastForwardWrapper }
