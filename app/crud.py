from sqlalchemy.orm import Session
from . import models, schemas


def get_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Project).offset(skip).limit(limit).all()


def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(name=project.name, description=project.description,
                                phase=project.phase, location_lat=project.location.lat, location_lng=project.location.lng)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def delete_project(db: Session, project_id: int):
    db_project = db.query(models.Project).filter(
        models.Project.id == project_id).first()
    db.delete(db_project)
    db.commit()


def update_project(db: Session, project_id: int, project: schemas.ProjectUpdate):
    db_project = db.query(models.Project).filter(
        models.Project.id == project_id).first()
    if db_project:
        db_project.name = project.name
        db_project.description = project.description
        db_project.phase = project.phase
        db_project.location_lat = project.location.lat
        db_project.location_lng = project.location.lng
        db.commit()
        db.refresh(db_project)
    return db_project


def get_sites(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Site).offset(skip).limit(limit).all()


def get_site(db: Session, site_id: int):
    return db.query(models.Site).filter(models.Site.id == site_id).first()


def create_site(db: Session, site: schemas.SiteCreate):
    db_site = models.Site(name=site.name, description=site.description,
                          location_lat=site.location.lat,
                          location_lng=site.location.lng, project_id=site.project_id)
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site


def delete_site(db: Session, site_id: int):
    db_site = db.query(models.Site).filter(models.Site.id == site_id).first()
    db.delete(db_site)
    db.commit()


def update_site(db: Session, site_id: int, site: schemas.SiteUpdate):
    db_site = db.query(models.Site).filter(models.Site.id == site_id).first()
    if db_site:
        db_site.name = site.name
        db_site.description = site.description
        db_site.location_lat = site.location.lat
        db_site.location_lng = site.location.lng
        db_site.project_id = site.project_id
        db.commit()
        db.refresh(db_site)
    return db_site
