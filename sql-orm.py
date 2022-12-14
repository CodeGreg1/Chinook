from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///chinook")
base = declarative_base()


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)



Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)

# artists = session.query(Artist)
# for artist in artists:
#    print(artist.ArtistId, artist.Name, sep=" | ")
#Q2   print(artist.Name)
#Q3
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")
#Q4
# artist = session.query(Artist).filter_by(ArtistId =51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

#Q5
# albums = session.query(Album).filter_by(ArtistId = 51)
# for album in albums:
#     print(album.AlbumId, album.Title, sep=" | ")

#Q6

tracks = session.query(Track).filter_by(AlbumId =36)
for track in tracks:
    print(track.TrackId, track.Name, sep=" | ") 
#         track.AlbumId, 
#        track.MediaTypeId, 
#        track.GenreId,
#        track.Composer,
#        track.Milliseconds,
#        track.Bytes,
#        track.UnitPrice,
#        sep=" | ")