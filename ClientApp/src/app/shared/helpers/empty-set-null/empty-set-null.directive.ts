import { Directive, EventEmitter, HostListener, Output, Self } from '@angular/core';
import { NgControl } from '@angular/forms';

@Directive({
  selector: 'input[appEmptySetNull]'
})
export class EmptySetNullDirective {

  @Output() EmptyToNull = new EventEmitter<string>();

  constructor(@Self() private ngControl: NgControl) { }

  @HostListener('keyup', ['$event']) onKeyDowns(event: KeyboardEvent): void {
    if (this.ngControl.value?.trim() === '') {
      this.ngControl.reset(null);
    }
  }

}
