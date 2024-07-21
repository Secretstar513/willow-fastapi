from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud
from ..database import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Site])
def read_sites(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    sites = crud.get_sites(db, skip=skip, limit=limit)
    return [{"id": site.id, "name": site.name, "description": site.description, "location": {"lat": site.location_lat, "lng": site.location_lng}, 'project_id': site.project_id} for site in sites]


@router.get("/{site_id}", response_model=schemas.Site)
def read_site(site_id: int, db: Session = Depends(get_db)):
    db_site = crud.get_site(db, site_id=site_id)
    if db_site is None:
        raise HTTPException(status_code=404, detail="Site not found")
    return db_site


@router.post("/", response_model=schemas.Site)
def create_site_for_project(site: schemas.SiteCreate, db: Session = Depends(get_db)):
    db_site = crud.create_site(db=db, site=site)
    return {"id": db_site.id, "name": db_site.name, "description": db_site.description, "location": {"lat": db_site.location_lat, "lng": db_site.location_lng}, "project_id": db_site.project_id}


@router.put("/{site_id}", response_model=schemas.Site)
def update_site(site_id: int, site:schemas.SiteUpdate, db: Session = Depends(get_db)):
    print(site)
    db_site = crud.update_site(db=db, site_id=site_id, site=site)
    return {"id": db_site.id, "name": db_site.name, "description": db_site.description, "location": {"lat": db_site.location_lat, "lng": db_site.location_lng}, "project_id": db_site.project_id}


@router.delete("/{site_id}")
def delete_site(site_id: int, db: Session = Depends(get_db)):
    crud.delete_site(db=db, site_id=site_id)
    return {'message': "Site deleted successfully"}
