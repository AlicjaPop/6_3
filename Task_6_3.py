from sqlalchemy import create_engine, MetaData, Integer, Float, String, Date, Table, Column

engine = create_engine('sqlite:///C:/Users/user/OneDrive/Desktop/Kodilla/6_3/Task_6_3.dtabase.db', echo=True)

meta = MetaData()

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
   Column('date', Date),
   Column('precip', Float),
   Column('tobs', Integer),   
)

meta.create_all(engine)
print(engine.table_names())