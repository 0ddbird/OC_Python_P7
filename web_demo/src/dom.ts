import { items } from './demo_data.js'
import { type Item, type IState } from './models.js'

export class DOMCell {
  constructor (public DOMElement: HTMLDivElement) {}

  setValue (value: number): void {
    this.DOMElement.textContent = `${value}`
  }

  highlight (): void {
    this.DOMElement.classList.add('active')
  }

  unHighlight (): void {
    this.DOMElement.classList.remove('active')
  }
}

function populateDOMItems (): void {
  const itemsDiv = document.getElementById('items')
  items.forEach((item: Item, index) => {
    const itemDiv = document.createElement('div')
    itemDiv.className = 'item'
    itemDiv.dataset.itemid = `${index}`

    const nameDiv = document.createElement('div')
    nameDiv.className = 'item-number'
    nameDiv.textContent = `Item ${index + 1}`

    const weightDiv = document.createElement('div')
    weightDiv.className = 'item-weight'
    weightDiv.textContent = `${item.weight}`

    const valueDiv = document.createElement('div')
    valueDiv.className = 'item-value'
    valueDiv.textContent = `${item.value}`

    itemDiv.appendChild(nameDiv)
    itemDiv.appendChild(weightDiv)
    itemDiv.appendChild(valueDiv)

    itemsDiv?.appendChild(itemDiv)
  })
}

function resetDOMTable (state: IState): void {
  const DOMTable = document.getElementById('table') as HTMLDivElement
  const DOMTableHeader = document.getElementById('table-header') as HTMLDivElement
  DOMTable.innerHTML = ''
  DOMTableHeader.innerHTML = ''
  if (state.currentButton != null && state.currentListener != null) {
    state.currentButton.removeEventListener('click', state.currentListener)
    state.currentListener = null
    state.currentButton = null
  }
}

function createDOMTable (table: any[][], maxWeight: number): void {
  const DOMTable = document.getElementById('table') as HTMLDivElement
  const DOMTableHeader = document.getElementById('table-header') as HTMLDivElement
  DOMTableHeader.style.gridTemplateColumns = `repeat(${maxWeight}, 1fr)`
  DOMTable.style.gridTemplateRows = `repeat(${table.length}, 1fr)`

  for (let i = 0; i < maxWeight; i++) {
    const headerCell = document.createElement('div')
    headerCell.classList.add('header-cell')
    headerCell.textContent = `${i}`
    DOMTableHeader.append(headerCell)
  }
  let arrayIncr = 0

  table.forEach((array) => {
    const DOMArray = document.createElement('div')
    DOMArray.classList.add('sub-array')
    DOMArray.dataset.array = `${arrayIncr}`
    DOMArray.style.gridTemplateColumns = `repeat(${array.length}, 1fr)`
    DOMTable.append(DOMArray)
    let cellIncr = 0
    array.forEach((cell) => {
      const DOMCell = document.createElement('div')
      DOMCell.classList.add('cell')
      DOMCell.dataset.cell = `${cellIncr}`
      cellIncr += 1
      DOMArray.append(DOMCell)
    })
    arrayIncr += 1
  })
}

function selectDOMCell (row: number, cell: number): HTMLDivElement {
  const DOMTable = document.getElementById('table') as HTMLDivElement
  const DOMSubArray = DOMTable.querySelector(
    `[data-array="${row}"]`
  ) as HTMLDivElement
  const DOMCell = DOMSubArray.querySelector(
    `[data-cell="${cell}"]`
  ) as HTMLDivElement
  return DOMCell
}

export { populateDOMItems, createDOMTable, resetDOMTable, selectDOMCell }
