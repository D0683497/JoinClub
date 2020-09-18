import { Directive, EventEmitter, HostListener, Output, Self } from '@angular/core';
import { NgControl } from '@angular/forms';

@Directive({
  selector: 'input[appFirstLetterUpper]'
})
export class FirstLetterUpperDirective {

  @Output() FirstLetterUpper = new EventEmitter<string>();

  constructor(@Self() private ngControl: NgControl) { }

  @HostListener('keyup', ['$event']) onKeyDowns(event: KeyboardEvent): void {
    const value: string = this.ngControl.value;
    if (value != null) {
      this.ngControl.reset(value.charAt(0).toUpperCase() + value.slice(1));
    }
  }

}
