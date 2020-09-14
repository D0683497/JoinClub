import { Directive, ElementRef, HostListener } from '@angular/core';
import { NgControl } from '@angular/forms';

@Directive({
  selector: 'input[appEmptySetNull]'
})
export class EmptySetNullDirective {

  constructor(private el: ElementRef, private control: NgControl) { }

  @HostListener('input', ['$event.target'])
  onEvent(target: HTMLInputElement): void {
    console.log(target.value);
    // this.control.viewToModelUpdate((target.value === '') ? null : target.value);
    if (this.control.valueChanges != null) {
      this.control.valueChanges.subscribe((value: string) => {
        if (value === '') {
          this.control.viewToModelUpdate(null);
        }
      });
    }
  }

}
