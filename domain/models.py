from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    # items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="items")
    
class Job(Base):
    __tablename__ = "maintenance"
    
    id = Column(Integer, primary_key=True, index=True)
    project = Column(String, nullable=False)
    hotspot_type = Column(String, nullable=False)
    max_temp = Column(String, nullable=False)
    string_tag = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    
    assigns = relationship("Assign", back_populates="job")


class Man(Base):
    __tablename__ = "man"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    header = Column(String, nullable=False)
    department = Column(String, nullable=False)
    position = Column(String, nullable=False)
    tell = Column(String, nullable=False)
    email = Column(String, nullable=False)
    status = Column(String, nullable=False)

class Assign(Base):
    __tablename__ = "assign"
    
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey('maintenance.id'), nullable=False)
    project = Column(String, nullable=False)
    hotspot_type = Column(String, nullable=False)
    max_temp = Column(String, nullable=False)
    string_tag = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    header = Column(String)
    worker = Column(String)
    status = Column(String)
    
    job = relationship("Job", back_populates="assigns")


