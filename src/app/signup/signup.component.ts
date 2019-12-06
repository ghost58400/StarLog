import { Component, OnInit} from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
declare var $: any;


const url = "http://localhost/signup";

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})

export class SignupComponent implements OnInit {

  form: FormGroup;

  constructor(private formBuilder: FormBuilder) {
    // create our form group with all the inputs we will be using in the template
    this.form = this.formBuilder.group({
      nom: ['', [Validators.required]],
      prenom: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      naissance: ['', Validators.required],
      codepostal: ['', Validators.required]
    });
  }

  ngOnInit(){
  }
  submit() {
    if (this.form.valid) {
      console.log(this.form.value);
      $.ajax({
        url : 'send',
        type : 'POST', // Le type de la requête HTTP, ici devenu POST
        data : JSON.stringify(this.form.value),
        dataType : 'html'
     });
    }
  }

}
