"""
Analitics:
-songs top (rank)
-artists top (rank)
-duration (max, min, avg)
-streams (max, min, avg)
"""


from parsers import settings
servs = settings.services


def get_songs_top(songs, services=servs):
    songs_upd = {}
    for song in songs:
        name = song['name']
        if song['service'] in services:

            if name in songs_upd:
                songs_upd[name]['rank'] += int(song['rank'])
                songs_upd[name]['services'].append({song['service']: song['rank']})
                if song['duration']:
                    songs_upd[name]['duration'] = song['duration']
                if song['streams']:
                    songs_upd[name]['streams'] = song['streams']
                if song['album']:
                    songs_upd[name]['album'] = song['album']
            else:
                songs_upd[name] = song
                songs_upd[name]['rank'] = int(song['rank'])
                songs_upd[name]['services'] = [{song['service']: song['rank']}]

    # print(len(songs_upd))
    for name, info in songs_upd.items():
        songs_upd[name]['rank'] /= len(songs_upd[name]['services'])
    songs_upd = list(songs_upd.values())
    songs_upd.sort(key=lambda song: song['rank'])
    return songs_upd


def get_artists_top(songs, services=servs):
    artists = {}
    for song in songs:
        if song['service'] in services:
            for artist in song['artists']:
                if len(artist) > 2:
                    if artist in artists:
                        artists[artist] += 1
                    else:
                        artists[artist] = 1
    artists = list(artists.items())
    artists.sort(key=lambda artist: artist[1], reverse=True)
    # print(len(artists))
    # print(artists)
    return artists


def get_durations_sort(songs, services=servs):
    songs_upd = [song for song in songs if song['service'] in services]
    songs_upd.sort(key=lambda song: song['duration'] if song['duration'] else '0')
    return songs_upd


def get_streams_sort(songs, services=servs):
    songs = [song for song in songs if song['service'] in services]
    for song in songs:
        if song['streams'] != None:
            my_str = str(song['streams']).replace(',', '')
            song['streams'] = int(my_str)

    new_time_list = sorted(songs, key=lambda k: k['streams'] if k['streams'] != None else False)

    return new_time_list


