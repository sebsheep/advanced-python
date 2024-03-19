from datetime import datetime
from typing import Literal, Iterable, Generator

from pydantic import BaseModel, ValidationError


def f(n: Iterable[str]) -> None:
    for x in n:
        print(n)


def g() -> Generator[str, None, None]:
    yield "John"
    yield "Seb"
    yield "Haron"
    return


# class Meeting(BaseModel):
#     when: datetime
#     where: bytes


# m = Meeting.model_validate({"when": "2020-01-01T12:00", "where": "home"})
# print(m)
# # > when=datetime.datetime(2020, 1, 1, 12, 0) where=b'home'
# try:
#     m = Meeting.model_validate(
#         {"when": "2020-01-01T12:00", "where": "home"}, strict=True
#     )
# except ValidationError as e:
#     print(e)

# m_json = Meeting.model_validate_json(
#     '{"when": "2020-01-01T12:00", "where": "home"}', strict=True
# )
# print(m_json)
# > when=datetime.datetime(2020, 1, 1, 12, 0) where=b'home'


class Player(BaseModel):
    name: str
    score: int
    favorite_color: Literal["red"] | Literal["blue"] | Literal["green"]


"""{
  "players": [{ 
    "name": "Ford",
    "score": 42,
    "favorite_color": "red",
    "from": "Betelgeuse"
  }],
  "games": ["pong", "tetris"]
}"""

Player.model_validate_json(
    """
  { 
    "name": "Ford",
    "score": 42,
    "favorite_color": "red",
    "from": "Betelgeuse"
  
}"""
)
