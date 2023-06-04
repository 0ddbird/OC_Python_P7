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
