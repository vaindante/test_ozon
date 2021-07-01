from pprint import pprint
from typing import List

from pydantic import BaseModel
from requests import get


class Post(BaseModel):
    id: int = None
    title: str = ''
    body: str = ''
    userId: int = ''

    def __hash__(self):
        return self.id, self.title


class Posts(BaseModel):
    __root__: List[Post]


result = get('https://jsonplaceholder.typicode.com/posts').json()

posts = Posts.parse_obj(result)

print()
sort_post = {post.userId: post.dict() for post in sorted(posts.__root__, key=lambda x: len(x.title))}

posts = Posts.parse_obj(list(sort_post.values()))
pprint(posts)


