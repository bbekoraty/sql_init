from pydantic import BaseModel
from typing import Optional,List, Dict, Any

# class JobBase(BaseModel):
#     title: str
#     description: str | None = None

# class JobCreate(JobBase):
#     pass

# #reading with api models
# class Job(JobBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True

    
class JobBase(BaseModel):
    project: str
    hotspot_type: str
    max_temp: float
    string_tag: str
    priority: int
    
class JobCreate(JobBase):
    pass
    
class Job(JobBase):
    id: int

    class Config:
        orm_mode = True

class Properties(BaseModel):
    url: str
    var: str
    project: str
    Device: str
    Device_id: str
    IFOV: str
    MFOV: str
    ACC: str
    Date: str
    Time: str
    tag: str
    x: float
    y: float
    xmax: float
    ymax: float
    hotspot_type: str
    priority: int
    maxTemperature: float
    minTemperature: float
    maxIndex: List[int]
    minIndex: List[int]
    pv_brand: str
    normal_temp: float
    pv_min: str
    cell_size: str

class Geometry(BaseModel):
    type: str
    coordinates: List[str]

class Feature(BaseModel):
    type: str
    properties: Properties
    geometry: Geometry

class FeatureCollection(BaseModel):
    type: str
    features: List[Feature]

class ManBase(BaseModel):
    id: int
    name: str
    surname: str
    nickname: str
    header: str
    department: str
    position: str
    tell: str
    email: str
    status: str

class ManCreate(ManBase):
    pass

class ManResponse(ManBase):

    class Config:
        orm_mode = True 

        
class AssignBase(BaseModel):
    job_id: int
    project: str
    hotspot_type: str
    max_temp: str
    string_tag: str
    priority: int
    header: str = ''
    worker: str = ''
    status: str = ''

class AssignCreate(AssignBase):
    pass

#reading with api models
class AssignResponse(AssignBase):
    class Config:
        orm_mode = True 