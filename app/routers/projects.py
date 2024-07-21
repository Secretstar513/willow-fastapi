from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud
from ..database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.create_project(db, project=project)
    return {"id": db_project.id, "name": db_project.name, "description": db_project.description, "phase": db_project.phase, "location": {"lat": db_project.location_lat, "lng": db_project.location_lng}}


@router.get("/", response_model=List[schemas.Project])
def read_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    projects = crud.get_projects(db, skip=skip, limit=limit)
    return [{"id": project.id, "name": project.name, "description": project.description, "phase": project.phase, "location": {"lat": project.location_lat, "lng": project.location_lng}, "sites": [{"id": site.id, "name": site.name, "description": site.description, "location": {"lat": site.location_lat, "lng": site.location_lng}, 'project_id': site.project_id} for site in project.sites]} for project in projects]


@router.get("/{project_id}", response_model=schemas.Project)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.put("/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, project: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    db_project = crud.update_project(
        db=db, project_id=project_id, project=project)
    return {"id": db_project.id, "name": db_project.name, "description": db_project.description, "phase": db_project.phase, "location": {"lat": db_project.location_lat, "lng": db_project.location_lng}}


@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    crud.delete_project(db=db, project_id=project_id)
    return {'message': "Project deleted successfully"}
