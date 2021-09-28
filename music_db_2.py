from sqlalchemy import create_engine
from pprint import pprint

engine = create_engine("postgresql://user:pass@localhost:5432/base")
connection = engine.connect()

artists = [
    {'title': 'Pink Floyd', 'artist_id': 1}, {'title': 'Daft Punk', 'artist_id': 2},
    {'title': 'Dire Straits', 'artist_id': 3}, {'title': 'MGMT', 'artist_id': 4},
    {'title': 'The Doors', 'artist_id': 5}, {'title': 'Depeche Mode', 'artist_id': 6},
    {'title': 'The Weeknd', 'artist_id': 7}, {'title': 'Fleetwood Mac', 'artist_id': 8},
    {'title': 'Rammstein', 'artist_id': 9}, {'title': 'Led Zeppelin', 'artist_id': 10}
]

albums = [
    {'album_id': 1, 'release_year': 2013, 'title': 'Random Access Memories'},
    {'album_id': 2, 'release_year': 1985, 'title': 'Brothers In Arms'},
    {'album_id': 3, 'release_year': 2018, 'title': 'Little Dark Age'},
    {'album_id': 4, 'release_year': 1973, 'title': 'The Dark Side Of The Moon'},
    {'album_id': 5, 'release_year': 2020, 'title': 'After Hours'},
    {'album_id': 6, 'release_year': 1971, 'title': 'L.A. Woman'},
    {'album_id': 7, 'release_year': 1971, 'title': 'Led Zeppelin IV'},
    {'album_id': 8, 'release_year': 2004, 'title': 'REISE, REISE'},
    {'album_id': 9, 'release_year': 1977, 'title': 'Rumours'},
    {'album_id': 10, 'release_year': 1990, 'title': 'Violator'}
]

artist_album = [
    {'album_id': 1, 'artist_id': 2},
    {'album_id': 2, 'artist_id': 3},
    {'album_id': 3, 'artist_id': 4},
    {'album_id': 4, 'artist_id': 1},
    {'album_id': 5, 'artist_id': 7},
    {'album_id': 6, 'artist_id': 5},
    {'album_id': 7, 'artist_id': 10},
    {'album_id': 8, 'artist_id': 9},
    {'album_id': 9, 'artist_id': 8},
    {'album_id': 10, 'artist_id': 6}
]

genres = [
    {'title': 'Progressive Rock', 'genre_id': 1}, {'title': 'Rock', 'genre_id': 2},
    {'title': 'Industrial Metal', 'genre_id': 3}, {'title': 'Electronic', 'genre_id': 4},
    {'title': 'Heavy Metal', 'genre_id': 5}, {'title': 'R&B', 'genre_id': 6}
]

artist_genre = [
    {'artist_id': 1, 'genre_id': 1},
    {'artist_id': 2, 'genre_id': 4},
    {'artist_id': 3, 'genre_id': 2},
    {'artist_id': 4, 'genre_id': 4},
    {'artist_id': 4, 'genre_id': 2},
    {'artist_id': 5, 'genre_id': 2},
    {'artist_id': 6, 'genre_id': 4},
    {'artist_id': 7, 'genre_id': 6},
    {'artist_id': 7, 'genre_id': 4},
    {'artist_id': 8, 'genre_id': 2},
    {'artist_id': 9, 'genre_id': 3},
    {'artist_id': 10, 'genre_id': 5}
]

tracks = [
    {'album_id': 1, 'duration': 269, 'title': 'Instant Crush', 'track_id': 1},
    {'album_id': 1, 'duration': 217, 'title': 'Giorgio by Moroder', 'track_id': 2},
    {'album_id': 2, 'duration': 403, 'title': 'Money For Nothing', 'track_id': 3},
    {'album_id': 2, 'duration': 263, 'title': 'Brothers In Arms', 'track_id': 4},
    {'album_id': 3, 'duration': 467, 'title': 'When You Die', 'track_id': 5},
    {'album_id': 3, 'duration': 200, 'title': 'One Thing Left to Try', 'track_id': 6},
    {'album_id': 4, 'duration': 141, 'title': 'Time', 'track_id': 7},
    {'album_id': 4, 'duration': 415, 'title': 'Brain Damage', 'track_id': 8},
    {'album_id': 5, 'duration': 285, 'title': 'Blinding Lights', 'track_id': 9},
    {'album_id': 5, 'duration': 316, 'title': 'Heartless', 'track_id': 10},
    {'album_id': 6, 'duration': 269, 'title': 'Love Her Madly', 'track_id': 11},
    {'album_id': 6, 'duration': 264, 'title': 'Riders on the Storm', 'track_id': 12},
    {'album_id': 7, 'duration': 436, 'title': 'My Black Dog', 'track_id': 13},
    {'album_id': 7, 'duration': 473, 'title': 'Stairway to Heaven', 'track_id': 14},
    {'album_id': 8, 'duration': 258, 'title': 'MEIN TEIL', 'track_id': 15},
    {'album_id': 8, 'duration': 275, 'title': 'MOSKAU', 'track_id': 16},
    {'album_id': 9, 'duration': 399, 'title': 'Never Going Back Again', 'track_id': 17},
    {'album_id': 9, 'duration': 371, 'title': 'The Chain', 'track_id': 18},
    {'album_id': 10, 'duration': 138, 'title': 'Personal Jesus', 'track_id': 19},
]

mixtapes = [
    {'mixtape_id': 1, 'release_year': 2014, 'title': 'Rock Road Trip'},
    {'mixtape_id': 2, 'release_year': 2010, 'title': 'House Motivation'},
    {'mixtape_id': 3, 'release_year': 2017, 'title': 'Good Vibes'},
    {'mixtape_id': 4, 'release_year': 2011, 'title': '80s Party Hits'},
    {'mixtape_id': 5, 'release_year': 2020, 'title': '10s Dance'},
    {'mixtape_id': 6, 'release_year': 2018, 'title': 'Rock & Chill'},
    {'mixtape_id': 7, 'release_year': 2011, 'title': 'Deezer Sessions'},
    {'mixtape_id': 8, 'release_year': 2016, 'title': 'Best Electronic Of All Time'}
]

track_mixtape = [
    {'mixtape_id': 1, 'track_id': 5},
    {'mixtape_id': 2, 'track_id': 7},
    {'mixtape_id': 2, 'track_id': 11},
    {'mixtape_id': 2, 'track_id': 12},
    {'mixtape_id': 3, 'track_id': 1},
    {'mixtape_id': 4, 'track_id': 15},
    {'mixtape_id': 1, 'track_id': 17},
    {'mixtape_id': 5, 'track_id': 5},
    {'mixtape_id': 1, 'track_id': 13},
    {'mixtape_id': 5, 'track_id': 3},
    {'mixtape_id': 5, 'track_id': 6},
    {'mixtape_id': 6, 'track_id': 19},
    {'mixtape_id': 7, 'track_id': 4},
    {'mixtape_id': 7, 'track_id': 15},
    {'mixtape_id': 8, 'track_id': 3}
]


def create():
    connection.execute("CREATE TABLE artist("
                       "artist_id SERIAL PRIMARY KEY, "
                       "title VARCHAR(30) NOT NULL);"

                       "CREATE TABLE album("
                       "album_id SERIAL PRIMARY KEY, "
                       "title VARCHAR(40) NOT NULL, "
                       "release_year INTEGER NOT NULL CHECK(release_year>1900));"

                       "CREATE TABLE artist_album("
                       "artist_id INTEGER REFERENCES artist(artist_id), "
                       "album_id INTEGER REFERENCES album(album_id), "
                       "CONSTRAINT artist_album_pk PRIMARY KEY(artist_id, album_id));"

                       "CREATE TABLE genre("
                       "genre_id SERIAL PRIMARY KEY, "
                       "title VARCHAR(20) NOT NULL UNIQUE);"

                       "CREATE TABLE artist_genre("
                       "artist_id INTEGER REFERENCES artist(artist_id), "
                       "genre_id INTEGER REFERENCES genre(genre_id), "
                       "CONSTRAINT artist_genre_pk PRIMARY KEY(artist_id, genre_id));"

                       "CREATE TABLE track("
                       "track_id SERIAL PRIMARY KEY, "
                       "title VARCHAR(40) NOT NULL, "
                       "duration INTEGER NOT NULL, "
                       "album_id INTEGER REFERENCES album(album_id));"

                       "CREATE TABLE mixtape("
                       "mixtape_id SERIAL PRIMARY KEY, "
                       "title VARCHAR(40) NOT NULL, "
                       "release_year INTEGER NOT NULL);"

                       "CREATE TABLE track_mixtape("
                       "track_id INTEGER REFERENCES track(track_id), "
                       "mixtape_id INTEGER REFERENCES mixtape(mixtape_id), "
                       "CONSTRAINT track_mixtape_pk PRIMARY KEY(track_id, mixtape_id));"
                       )


def insert():
    for artist in artists:
        connection.execute(f"INSERT INTO artist (artist_id, title) "
                           f"VALUES ({artist['artist_id']}, '{artist['title']}');")

    for album in albums:
        connection.execute(f"INSERT INTO album (album_id, title, release_year) "
                           f"VALUES ({album['album_id']}, '{album['title']}', {album['release_year']});")

    for art_alb in artist_album:
        connection.execute(f"INSERT INTO artist_album (artist_id, album_id) "
                           f"VALUES ({art_alb['artist_id']}, {art_alb['album_id']});")

    for genre in genres:
        connection.execute(f"INSERT INTO genre (genre_id, title) "
                           f"VALUES ({genre['genre_id']}, '{genre['title']}');")

    for art_gen in artist_genre:
        connection.execute(f"INSERT INTO artist_genre (artist_id, genre_id) "
                           f"VALUES ({art_gen['artist_id']}, {art_gen['genre_id']});")

    for track in tracks:
        connection.execute(f"INSERT INTO track (track_id, title, duration, album_id) "
                           f"VALUES ({track['track_id']}, '{track['title']}', {track['duration']}, "
                           f"{track['album_id']});")

    for mixtape in mixtapes:
        connection.execute(f"INSERT INTO mixtape (mixtape_id, title, release_year) "
                           f"VALUES ({mixtape['mixtape_id']}, '{mixtape['title']}', {mixtape['release_year']});")

    for trk_mix in track_mixtape:
        connection.execute(f"INSERT INTO track_mixtape (track_id, mixtape_id) "
                           f"VALUES ({trk_mix['track_id']}, {trk_mix['mixtape_id']});")


def select():
    result = connection.execute(
        "SELECT g.title, COUNT(ag.artist_id) "
        "FROM artist_genre ag "
        "JOIN genre g ON g.genre_id = ag.genre_id "
        "GROUP BY g.title;"
    ).fetchall()
    pprint(result)

    result = connection.execute(
        "SELECT COUNT(t.track_id) "
        "FROM album a "
        "JOIN track t ON t.album_id = a.album_id "
        "WHERE a.release_year BETWEEN 2019 AND 2020;"
    ).fetchall()
    pprint(result)

    result = connection.execute(
        "SELECT a.title, ROUND(AVG(t.duration)) "
        "FROM album a "
        "JOIN track t ON t.album_id = a.album_id "
        "GROUP BY a.title;"
    ).fetchall()
    pprint(result)

    result = connection.execute(
        "SELECT a.title "
        "FROM artist a "
        "WHERE a.title NOT IN "
        "(SELECT a.title FROM artist a "
        "JOIN artist_album aa ON aa.artist_id = a.artist_id "
        "JOIN album al ON al.album_id = aa.album_id "
        "WHERE al.release_year = 2020);"
    ).fetchall()
    pprint(result)

    result = connection.execute(
        "SELECT m.title "
        "FROM mixtape m "
        "JOIN track_mixtape tm ON tm.mixtape_id = m.mixtape_id "
        "JOIN track t ON t.track_id = tm.track_id "
        "JOIN album al ON al.album_id = t.album_id "
        "JOIN artist_album aa ON aa.album_id = al.album_id "
        "JOIN artist a ON a.artist_id = aa.artist_id "
        "WHERE a.title = 'Daft Punk';"
    ).fetchall()
    pprint(result)

    result = connection.execute(
        "SELECT a.title FROM album al "
        "JOIN artist_album aa ON aa.album_id = al.album_id "
        "JOIN artist a ON a.artist_id = aa.artist_id "
        "JOIN artist_genre ag ON ag.artist_id = a.artist_id "
        "JOIN genre g ON g.genre_id = ag.genre_id "
        "GROUP BY a.title "
        "HAVING COUNT(ag.artist_id) > 1;"
    ).fetchall()
    pprint(result)

    result = connection.execute(
        "SELECT t.title "
        "FROM track t "
        "WHERE t.title NOT IN "
        "(SELECT t.title FROM track t "
        "JOIN track_mixtape tm ON tm.track_id = t.track_id "
        "JOIN mixtape m ON m.mixtape_id = tm.mixtape_id);"
    ).fetchall()
    pprint(result)

    result = connection.execute(
        "SELECT a.title "
        "FROM artist a "
        "JOIN artist_album aa ON aa.artist_id = a.artist_id "
        "JOIN album al ON al.album_id = aa.album_id "
        "JOIN track t ON t.album_id = al.album_id "
        "WHERE t.duration = "
        "(SELECT MIN(t.duration) FROM track t);"
    ).fetchall()
    pprint(result)

    result = connection.execute(
        "SELECT al.title "
        "FROM album al "
        "JOIN track t ON t.album_id = al.album_id "
        "GROUP BY al.title "
        "HAVING COUNT(t.title) = "
        "(SELECT MIN(x.cnt) "
        "FROM (SELECT al.title, COUNT(t.title) as cnt FROM album al "
        "JOIN track t ON t.album_id = al.album_id "
        "GROUP BY al.title)x);"
    ).fetchall()
    pprint(result)


create()
insert()
select()
