from pymongo import MongoClient

client = MongoClient()

db=client.test

name = input("Unesite naziv filma: ")
year = input("Unesite godinu premijere: ")
genre = input("Unesite zanr: ") 

filmovi = db.filmovi

film_details = {
    'name': name,
    'year': year,
    'genre': genre
}

filmovi.insert_one(film_details)
 
result = filmovi.find()
 
for r in result:
    print("Film: {} | Godina premijere: {} | Zanr: {}".format(r['name'],r['year'], r['genre']))
