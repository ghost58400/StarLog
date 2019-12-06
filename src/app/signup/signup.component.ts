import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, NgForm } from '@angular/forms';
import {ApiService} from "../api.service";
import {Router} from "@angular/router";


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})

export class SignupComponent {

  form: FormGroup;

  constructor(private formBuilder: FormBuilder, private api: ApiService,private router: Router,) {
    // create our form group with all the inputs we will be using in the template

    this.form = this.formBuilder.group({
      nom: ['', [Validators.required]],
      prenom: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      naissance: ['', Validators.required],
      codepostal: ['', Validators.required],
      description: ['', Validators.required],
      jaide: [false],
      aled: [false]
    });
  }

  submit(form: NgForm) {
    if (this.form.valid) {
      this.api.signUp(form).subscribe(
        res => {
          this.router.navigate(['/matcher']);
        },
        err => {
          console.log(err);
        }
      );
    }
  }

}
