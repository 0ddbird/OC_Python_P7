class Item {
  constructor (public weight: number, public value: number) {}
}

interface IState {
  currentButton: HTMLButtonElement | null
  currentListener: ((e: MouseEvent) => void) | null
  inProgress: boolean
  resetInProgress: boolean
  play: boolean
}

export { Item, type IState }
