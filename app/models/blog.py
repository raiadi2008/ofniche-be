from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class BlogSection(BaseModel):
    section_type: str
    heading: str = None
    paragraphs: List[str] = Field(default_factory=list)
    list_items: List[str] = Field(default_factory=list)
    image: str = None
    sub_heading: str = None


class Blog(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    id: str = Field(alias="_id", default=None)
    title: str
    excerpt: str
    header_image: str
    sections: List[BlogSection] = Field(default_factory=list)
