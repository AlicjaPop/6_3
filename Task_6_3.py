import csv
from sqlalchemy import create_engine, MetaData, Integer, Float, String, Table, Column, ForeignKey

engine = create_engine('sqlite:///C:/Users/user/OneDrive/Desktop/Kodilla/6_3/Task_6_3_database.db', echo=False)

database="C:/Users/user/OneDrive/Desktop/Kodilla/6_3/Task_6_3_database.db"

meta = MetaData()

# Tables creation
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
   Column('station', String, ForeignKey("stations.station"), nullable=False ),
   Column('date', String),
   Column('precip', Float),
   Column('tobs', Integer),   
)

meta.create_all(engine)

conn=engine.connect()

# Tables fill-out
stations_records="C:/Users/user/Downloads/clean_stations.csv"
measures_records="C:/Users/user/Downloads/clean_measure.csv"

with open(stations_records, 'r') as f:
    csv_reader = csv.reader(f)
    headers = next(csv_reader)
    records = [dict(zip(headers, row)) for row in csv_reader]
    conn.execute(stations.insert(), records)

with open(measures_records, 'r') as f:
    csv_reader = csv.reader(f)
    headers = next(csv_reader)
    records = [dict(zip(headers, row)) for row in csv_reader]
    conn.execute(measures.insert(), records)

# Example from the excercise
print(conn.execute("SELECT * FROM stations LIMIT 5").fetchall())




# Closing connection
conn.close()