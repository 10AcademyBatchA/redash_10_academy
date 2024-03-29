from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, Float, Date, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from connect_to_postgres import ConnectToPostgres

Base = declarative_base()

class Cities_info(Base):
    __tablename__ = "cities_info"

    cities = Column("cities", String, primary_key=True)
    name = Column("name", String)
    geography = Column("geography", String)
    geography_with_capital = Column("geography_with_capital", String)
    watch_time = Column("watch_time_in_hours", Integer)
    average_time_duration = Column("average_time_duration", String)

    def __init__(self, cities, name, geography, geography_with_capital, watch_time, average_time_duration):
        self.cities = cities
        self.name = name
        self.geography = geography
        self.geography_with_capital = geography_with_capital
        self.watch_time = watch_time
        self.average_time_duration = average_time_duration

class Cities_chart(Base):
    __tablename__ = "cities_chart"

    id = Column("id", Integer, primary_key=True)
    date = Column("date", Date)
    views = Column("views", Integer)
    cities = Column(String, ForeignKey("cities_info.cities"))

    def __init__(self, id, date, view, cities):
        self.id = id
        self.date  = date
        self.view = view
        self.cities = cities

class Content_type_info(Base):
    __tablename__ = "content_type_info"

    id = Column("id", Integer, primary_key=True)
    content_type = Column("content_type", String)
    watch_time = Column("watch_time_in_hours", Integer)
    average_time_duration = Column("average_time_duration", String)

    def __init__(self, id, content_type, watch_time, average_time_duration):
        id = self.id
        self.content_type = content_type
        self.watch_time = watch_time
        self.average_time_duration = average_time_duration

class Content_type_chart(Base):
    __tablename__ = "content_type_chart"

    id = Column("id", Integer, primary_key=True)
    date = Column("date", Date)
    views = Column("views", Integer)
    content_types = Column(Integer, ForeignKey("content_type_info.id"))

    def __init__(self, id, date, view, content_types):
        self.id = id
        self.date  = date
        self.view = view
        self.content_types = content_types

class Device_type_info(Base):
    __tablename__ = "device_type_info"

    id = Column("id", Integer, primary_key=True)
    device_type = Column("device_type", String)
    watch_time = Column("watch_time_in_hours", Integer)
    average_time_duration = Column("average_time_duration", String)

    def __init__(self, id, content_type, watch_time, average_time_duration):
        id = self.id
        self.device_type = device_type
        self.watch_time = watch_time
        self.average_time_duration = average_time_duration
class Device_type_chart(Base):
    __tablename__ = "device_type_chart"

    id = Column("id", Integer, primary_key=True)
    date = Column("date", Date)
    views = Column("views", Integer)
    device_types = Column(Integer, ForeignKey("device_type_info.id"))

    def __init__(self, id, date, view, content_types):
        self.id = id
        self.date  = date
        self.view = view
        self.device_types = device_types

conn = ConnectToPostgres()
engine = conn.get_engine()
Base.metadata.create_all(bind=engine, checkfirst=True)

