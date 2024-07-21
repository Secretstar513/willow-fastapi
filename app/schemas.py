from pydantic import BaseModel
from typing import List


class Location(BaseModel):
    lat: str
    lng: str


class SiteBase(BaseModel):
    name: str
    description: str
    location: Location
    project_id: int

class SiteCreate(SiteBase):
    pass


class SiteUpdate(SiteBase):
    pass


class Site(SiteBase):
    id: int
    project_id: int

    class Config:
        from_attributes = True


class ProjectBase(BaseModel):
    name: str
    description: str
    phase: str
    location: Location


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    sites: List[Site] = []

    class Config:
        from_attributes = True
