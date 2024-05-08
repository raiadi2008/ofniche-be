from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class PlatformRatings(BaseModel):
    platform: str
    rating: float


class Tool(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    id: str = Field(alias="_id", default=None)
    name: str
    description: str
    pros: List[str] = Field(default_factory=list)
    cons: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)
    logo: str = None
    url: str
    platform_ratings: List[PlatformRatings] = Field(default_factory=list)
