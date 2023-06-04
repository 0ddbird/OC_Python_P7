import { createDOMTable, sleep, waitForNext } from './utils.js'
import { state } from './state.js'

function getBestCombinationItems(items, keep, maxWeight) {
  const includedItems = []
  for (let i = items.length - 1; i >= 0; i--) {
    if (maxWeight === 0) {
      break
    }
    const currentRow = keep[i]
    if (currentRow[maxWeight] === 1) {
      includedItems.push(items[i])
      maxWeight -= items[i].weight
    }
  }
  includedItems.reverse()
  return includedItems
}

export async function dynamicProgramming(items, maxWeight) {
  const n = items.length
  const table = Array.from(Array(n), () => new Array(maxWeight + 1).fill(0))
  const keep = Array.from(Array(n), () => new Array(maxWeight + 1).fill(0))

  createDOMTable(table, maxWeight)

  for (let i = 0; i < n; i++) {
    for (let currMaxWeight = 0; currMaxWeight <= maxWeight; currMaxWeight++) {
      console.log(`[${i}][${i}]`)
      const DOMTable = document.getElementById('table')
      const DOMSubArray = DOMTable.querySelector(`[data-array="${i}"]`)
      const DOMCell = DOMSubArray.querySelector(
        `[data-cell="${currMaxWeight}"]`
      )
      await sleep(50)
      if (!state.play) await waitForNext()
      DOMCell.classList.add('active')

      if (i === 0 || currMaxWeight === 0) {
        DOMCell.textContent = '0'
        await sleep(200)
        DOMCell.classList.remove('active')
        continue
      }
      const item = items[i]
      const prevRow = table[i - 1]
      const currentRow = table[i]
      if (item.weight > currMaxWeight) {
        currentRow[currMaxWeight] = prevRow[currMaxWeight]
        DOMCell.textContent = prevRow[currMaxWeight]
        const DOMPrevRow = DOMTable.querySelector(`[data-array="${i - 1}"]`)
        const DOMPrevCell = DOMPrevRow.querySelector(
          `[data-cell="${currMaxWeight}"]`
        )
        DOMPrevCell.classList.add('prev-selected')
        if (!state.play) await waitForNext()
        DOMPrevCell.classList.remove('prev-selected')
      } else {
        const valueWithItem = item.value + prevRow[currMaxWeight - item.weight]
        const valueWithoutItem = prevRow[currMaxWeight]
        currentRow[currMaxWeight] = Math.max(valueWithItem, valueWithoutItem)
        DOMCell.textContent = currentRow[currMaxWeight]
        keep[i][currMaxWeight] = valueWithItem > valueWithoutItem ? 1 : 0
      }
      await sleep(50)
      DOMCell.classList.remove('active')
    }
  }
  return getBestCombinationItems(items, keep, maxWeight)
}
