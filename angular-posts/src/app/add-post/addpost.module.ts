import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AddpostRoutingModule } from './addpost-routing.module';
import { AddPostComponent } from './add-post.component';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  imports: [AddpostRoutingModule, ReactiveFormsModule, CommonModule],
  declarations: [AddPostComponent]
})
export class AddPostModul {}
