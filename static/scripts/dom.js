export class DOMCell {
    DOMElement;
    constructor(DOMElement) {
        this.DOMElement = DOMElement;
    }
    setValue(value) {
        this.DOMElement.textContent = `${value}`;
    }
    highlight() {
        this.DOMElement.classList.add('active');
    }
    unHighlight() {
        this.DOMElement.classList.remove('active');
    }
}
