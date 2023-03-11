import csv
from sqlalchemy import create_engine, MetaData, Integer, Float, String, Table, Column

engine = create_engine('sqlite:///C:/Users/user/OneDrive/Desktop/Kodilla/6_3/Task_6_3_database.db', echo=True)

database="C:/Users/user/OneDrive/Desktop/Kodilla/6_3/Task_6_3_database.db"

meta = MetaData()

# Tables
stations = Table(
   'stations', meta,
   Column('id', Integer, primary_key=True),
   Column('station', String),
   Column('latitude', Float),
   Column('longitude', Float),
   Column('elevation', Float),
   Column('name', String),
   Column('country', String),
   Column('state', String),
)

measures = Table(
   'measures', meta,
   Column('id', Integer, primary_key=True),
   Column('station', String),
   Column('date', String),
   Column('precip', Float),
   Column('tobs', Integer),   
)

meta.create_all(engine)

# Tables fill-out
stations_records="C:/Users/user/Downloads/clean_stations.csv"
table_stations = Table(stations, meta, autoload=True, autoload_with=engine)
measures_records="C:/Users/user/Downloads/clean_measure.csv"
table_measures = Table(measures, meta, autoload=True, autoload_with=engine)

with open(stations_records, 'r') as f:
    csv_reader = csv.reader(f)
    headers = next(csv_reader)
    data = [dict(zip(headers, row)) for row in csv_reader]

with engine.connect() as conn:
    conn.execute(table_stations.insert(), data)

with open(measures_records, 'r') as f:
    csv_reader = csv.reader(f)
    headers = next(csv_reader)
    data = [dict(zip(headers, row)) for row in csv_reader]

with engine.connect() as conn:
    conn.execute(table_measures.insert(), data)