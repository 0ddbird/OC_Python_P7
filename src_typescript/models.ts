class Item {
  constructor (public weight: number, public value: number) {}
}

interface State {
  currentButton: HTMLButtonElement | null
  currentListener: ((e: MouseEvent) => void) | null
  inProgress: boolean
  resetInProgress: boolean
  play: boolean
}

export { Item, type State }
