import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MatcherComponent } from './matcher.component';

describe('MatcherComponent', () => {
  let component: MatcherComponent;
  let fixture: ComponentFixture<MatcherComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MatcherComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MatcherComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
