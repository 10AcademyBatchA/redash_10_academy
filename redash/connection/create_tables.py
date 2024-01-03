from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, Float, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from connect_to_postgres import ConnectToPostgres

Base = declarative_base()

class Cities_info(Base):
    __tablename__ = "cities_info"

    cities = Column("cities", String, primary_key=True)
    name = Column("name", String)
    geography = Column("geography", String)
    geography_with_capital = Column("geography_with_capital", String)
    watch_time = Column("watch_time(hours)", Integer)
    average_time_duration = Column("average_time_duration", Float)

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
    view = Column("view", Integer)
    cities = Column(String, ForeignKey("cities_info.cities"))

    def __init__(self, date, view, cities):
        self.date  = date
        self.view = view
        self.cities = cities

conn = ConnectToPostgres()
engine = conn.get_engine()
Base.metadata.create_all(bind=engine)

