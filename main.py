from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str] = None):
   
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}



@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'} 


@app.get('/blog/{id}')
def show(id:int):
    #fetch blog with id = id
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    #fetch comments of blog with id =  id
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title:str
    body:Optional[str]=None
    published:bool

@app.post('/blog')
def create_blog(request:Blog):
    return {'data':f"The title of the blog is {request.title}"}