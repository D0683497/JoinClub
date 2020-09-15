import { Directive, EventEmitter, HostListener, Output, Self } from '@angular/core';
import { NgControl } from '@angular/forms';

@Directive({
  selector: 'input[appFirstLetterUpper]'
})
export class FirstLetterUpperDirective {

  @Output() FirstLetterUpper = new EventEmitter<string>();

  constructor(@Self() private ngControl: NgControl) { }

  @HostListener('keyup', ['$event']) onKeyDowns(event: KeyboardEvent): void {
    if (this.ngControl.value?.trim() !== '') {
      const value: string = this.ngControl.value;
      this.ngControl.reset(value.charAt(0).toUpperCase() + value.slice(1));
    }
  }

}
