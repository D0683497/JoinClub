import { FormGroup } from '@angular/forms';

// https://jasonwatmore.com/post/2018/11/07/angular-7-reactive-forms-validation-example

export function MustMatch(controlName: string, matchingControlName: string): (formGroup: FormGroup) => void {
  return (formGroup: FormGroup) => {
      const control = formGroup.controls[controlName];
      const matchingControl = formGroup.controls[matchingControlName];

      if (matchingControl.errors && !matchingControl.errors.mustMatch) {
          return;
      }

      if (control.value !== matchingControl.value) {
          matchingControl.setErrors({ mustMatch: true });
      } else {
          matchingControl.setErrors(null);
      }
  }
}
