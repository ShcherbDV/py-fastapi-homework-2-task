import datetime
from typing import List, Optional

from pydantic import BaseModel


class CountryBase(BaseModel):
    id: int
    code: str
    name: str | None


class LanguageBase(BaseModel):
    id: int
    name: str


class ActorBase(BaseModel):
    id: int
    name: str


class GenreBase(BaseModel):
    id: int
    name: str


class MovieBase(BaseModel):
    name: str
    date: datetime.date
    score: float
    overview: str
    status: str
    budget: float
    revenue: float
    country_id: int
    country: CountryBase
    genres: list[GenreBase]
    actors: list[ActorBase]
    languages: list[LanguageBase]


class MovieDetailSchema(MovieBase):
    id: int

    class Config:
        from_attributes = True


class MovieListResponseSchema(BaseModel):
    id: int
    name: str
    date: datetime.date
    score: float
    overview: str


class MovieListItemSchema(BaseModel):
    movies: List[MovieListResponseSchema]
    prev_page: str | None
    next_page: str | None
    total_pages: int
    total_items: int


class MovieUpdateSchema(BaseModel):
    name: Optional[str] = None
    date: Optional[datetime.date] = None
    score: Optional[float] = None
    overview: Optional[str] = None
    budget: Optional[int] = None
    revenue: Optional[int] = None
    country_id: Optional[int] = None
    country: Optional[CountryBase] = None
    genres: Optional[list[GenreBase]] = None
    actors: Optional[list[ActorBase]] = None
    languages: Optional[list[LanguageBase]] = None

    class Config:
        from_attributes = True


class MovieCreateSchema(BaseModel):
    name: str
    date: datetime.date
    score: float
    overview: str
    status: str
    budget: float
    revenue: float
    country: str
    genres: list[str]
    actors: list[str]
    languages: list[str]

    class Config:
        from_attributes = True
