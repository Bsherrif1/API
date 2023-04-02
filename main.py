from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {"message": "Learn fastapi"}

@app.get('/blog')
# def about(limit, published:bool):
def about(limit=10, published:bool=True, sort: Optional[str]=None):
    """Setting the default value for query parameters"""
    if published:
        return {'data': f'{limit} blogs published to the db'}
    else:
        return {'data': f'{limit} blogs'}

@app.get('/blog/str')
def blog_str():
    return {"blog": "Blog/str comes before blog/{id}, due to the concept of dynamic routing."}

@app.get('/blog/{id}')
def blog(id:int):
    """Path Parameters"""
    return {"blog":id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {"data": {"1", "2"}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data': f'Blog titled {blog.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)