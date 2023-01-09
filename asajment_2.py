from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///Books.db', echo = False)
meta = MetaData()

Books = Table(
   'Books', meta, 
   Column('id', Integer, primary_key = True), 
   Column('title', String), 
   Column('year', Integer),
)
meta.create_all(engine)

book_id = input("Unesite ID knjige: ")
book_title = input("Unesite naziv djela: ")
book_year = input("Unesite godinu izdavanja: ")

query = Books.insert().values(id = book_id, title = book_title, year = book_year)

query2 = Books.select()

conn = engine.connect()
r1 = conn.execute(query)
result = conn.execute(query2)

for row in result:
    print("title: {} | year: {}".format(row[1], row[2]))
