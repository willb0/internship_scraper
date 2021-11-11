from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, index=True)
    link = Column(String, unique=True)
