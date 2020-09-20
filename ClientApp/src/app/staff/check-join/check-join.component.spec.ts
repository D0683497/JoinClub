import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CheckJoinComponent } from './check-join.component';

describe('CheckJoinComponent', () => {
  let component: CheckJoinComponent;
  let fixture: ComponentFixture<CheckJoinComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CheckJoinComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CheckJoinComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
