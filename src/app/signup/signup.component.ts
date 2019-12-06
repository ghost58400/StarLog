import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, NgForm } from '@angular/forms';
import {ApiService} from "../api.service";
import {Router} from "@angular/router";
import { UploadService } from  '../upload.service';


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})

export class SignupComponent {

  form: FormGroup;
  error: string;
  userId: number = 1;
  uploadResponse = { status: '', message: '', filePath: '' };

  constructor(private formBuilder: FormBuilder, private api: ApiService,private router: Router, private uploadService: UploadService) {
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
      aled: [false],
      pdp: [null]
    });
  }

  onFileChange(event) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      this.form.get('pdp').setValue(file);
    }
  }

  submit(form: NgForm) {
    if (this.form.valid) {
      const formData = new FormData();
      formData.append('file', this.form.get('pdp').value);

      this.uploadService.upload(formData, this.form.get('email').value).subscribe(
        (res) => this.uploadResponse = res,
        (err) => this.error = err
      );
      console.log(this.form.value);
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
