import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()
# Query 1
# cursor.execute('SELECT * FROM "Artist"')
# Query 2
# cursor.execute('SELECT "Name" FROM "Artist"')
# Query 3
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [128])
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Led Zeppelin"])



results = cursor.fetchall()

connection.close()

for result in results:
    print(result)

