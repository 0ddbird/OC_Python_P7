import { dynamicProgramming } from './algorithm.js'
import { items } from './problem_data.js'
import { state } from './state.js'
import { resetDOMTable } from './utils.js'

const handleFastForward = async (e) => {
  const ffwdButton = document.getElementById('ffwd')
  const fwdIcon = document.getElementById('fwd-icon')
  const playIcon = document.getElementById('play-icon')
  fwdIcon.classList.toggle('hidden')
  playIcon.classList.toggle('hidden')
  ffwdButton.classList.toggle('pressed')

  state.play = !state.play
}

async function handleStart(e) {
  e.preventDefault()
  resetDOMTable()
  state.inProgress = true
  const weightInput = document.getElementById('weight-input')
  const maxWeight = parseInt(weightInput.value)
  await dynamicProgramming(items, maxWeight)
}

const handleReset = async (e) => {
  if (state.resetInProgress) return
  state.resetInProgress = true
  resetDOMTable()
  state.resetInProgress = false
  const weightInput = document.getElementById('weight-input')
  const maxWeight = parseInt(weightInput.value)
  await dynamicProgramming(items, maxWeight)
}

export { handleStart, handleReset, handleFastForward }
