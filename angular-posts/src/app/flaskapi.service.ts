import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Post } from './models/post';

@Injectable({
  providedIn: 'root',
})
export class FlaskapiService {
  constructor(private httpClient: HttpClient) {}

  public server: string = 'http://localhost:5000/api/'; //main route of our server
  public getPosts() {
    return this.httpClient.get<Post>(this.server + 'posts');
  }

  public getPost(postId: string) {
    return this.httpClient.get<Post>(this.server + 'post/${postId}');
  }

  public addPost(postObj: Post, image: any) {
    console.log(postObj);
  }
}
