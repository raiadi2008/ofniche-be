from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class CompetitorBlog(BaseModel):
    name: str
    url: str
    approx_traffic: int
    description: str
    ranking_keywords: List[str] = Field(default_factory=list)


class CountryCPC(BaseModel):
    country_code: str
    cpc_start: float
    cpc_end: float


class CountrySearchVolume(BaseModel):
    country_code: str
    search_volume_start: int
    search_volume_end: int


class Niche(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    id: str = Field(alias="_id", default=None)
    name: str
    description: str
    tags: List[str] = Field(default_factory=list)
    pros: List[str] = Field(default_factory=list)
    cons: List[str] = Field(default_factory=list)
    similar_niches: List[str] = Field(default_factory=list)
    icon: str = None
    competitors: List[CompetitorBlog] = Field(default_factory=list)
    country_cpc: List[CountryCPC] = Field(default_factory=list)
    country_search_volume: List[CountrySearchVolume] = Field(default_factory=list)
