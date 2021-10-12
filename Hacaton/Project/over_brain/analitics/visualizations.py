from matplotlib import pyplot as plt
from analitics.analis_1 import get_durations_sort, get_artists_top, get_streams_sort, get_songs_top
import json
import numpy as np


def get_sec(time: str):
    min = time.split(':')[0]
    sec = time.split(':')[1]
    return int(min) * 60 + int(sec)


with open('data.json', 'r') as f:
    common_data = json.load(f)

songs = get_songs_top(common_data)


def tracks_durations(songs):
    durations_common = {song['name']: get_sec(song['duration']) for song in songs if song['duration']}
    durations_apple = {song['name']: get_sec(song['duration']) for song in songs if
                       song['duration'] and 'apple' in [list(song.keys())[0] for song in song['services']]}
    durations_youtube = {song['name']: get_sec(song['duration']) for song in songs if
                         song['duration'] and 'youtube' in [list(song.keys())[0] for song in song['services']]}
    durations_spotify = {song['name']: get_sec(song['duration']) for song in songs if
                         song['duration'] and 'spotify' in [list(song.keys())[0] for song in song['services']]}
    durations_yandex = {song['name']: get_sec(song['duration']) for song in songs if
                        song['duration'] and 'yandex' in [list(song.keys())[0] for song in song['services']]}
    durations_deezer = {song['name']: get_sec(song['duration']) for song in songs if
                        song['duration'] and 'deezer' in [list(song.keys())[0] for song in song['services']]}
    # print([song for song in songs if song['service'] == 'deezer'])
    # print(durations_common)

    fig, ax = plt.subplots()
    # ax.plot(range(len(durations_common)), sorted(list(durations_common.values())), '-')
    ax.plot(range(len(durations_apple.values())), sorted(list(durations_apple.values())), '--', label='Apple Music')
    ax.plot(range(len(durations_youtube.values())), sorted(list(durations_youtube.values())), '--', label='Youtube Music')
    ax.plot(range(len(durations_spotify.values())), sorted(list(durations_spotify.values())), '--', label='Spotify')
    ax.plot(range(len(durations_yandex.values())), sorted(list(durations_yandex.values())), '--', label='Yandex')
    ax.plot(range(len(durations_deezer.values())), sorted(list(durations_deezer.values())), '--', label='Deezer')

    # Axes, Name, Legend
    plt.xlabel('Songs counter')
    plt.ylabel('Durations in seconds')

    plt.title("Duration analise for music services")
    plt.legend()
    # plt.savefig('Duration analise for music services.svg')
    plt.show()


###
def top_artists(num=10):
    top_artists = get_artists_top(common_data)[:num]

    # print(top_artists)
    names = [name[0] if name[0][:3] != 'by ' else name[0][3:] for name in top_artists]
    # print(names)
    counts = [count[1] for count in top_artists]
    # print(counts)

    fig, ax = plt.subplots()
    ax.bar(names, counts)
    # Axes, Name, Legend
    plt.xlabel('Artists')
    plt.ylabel('Num songs in charts')
    plt.title('Top artists')
    # plt.savefig('Top artists.svg')

    plt.show()

###
def common_top(songs, num=10):
    common_top = []
    spotify_sc = []
    apple_sc = []
    youtube_sc = []
    deezer_sc = []
    yandex_sc = []

    for song in songs:
        if len(song['services']) > 2:
            common_top.append(song)

    tracks = [song['name'][:8] for song in common_top]
    x = np.arange(len(tracks))
    width = 0.8/(1+5)

    for song in common_top:
        services = {list(song.keys())[0]: list(song.values())[0] for song in song['services']}
        spotify_sc.append(int(services['spotify']) if 'spotify' in services else 0)
        apple_sc.append(int(services['apple']) if 'apple' in services else 0)
        youtube_sc.append(int(services['youtube']) if 'youtube' in services else 0)
        yandex_sc.append(int(services['yandex']) if 'yandex' in services else 0)
        deezer_sc.append(int(services['deezer']) if 'deezer' in services else 0)

    fig, ax = plt.subplots()


    q1 = ax.bar(x+1*width, spotify_sc, width=width, label='Spotify')
    q2 = ax.bar(x+2*width, apple_sc, width=width, label='Apple Music')
    q3 = ax.bar(x+3*width, youtube_sc, width=width, label='Youtube Music')
    q4 = ax.bar(x+4*width, yandex_sc, width=width, label='Yandex Music')
    q5 = ax.bar(x+5*width, deezer_sc, width=width, label='Deezer')
    plt.xlabel("Songs's names")
    plt.ylabel('Rank song')
    plt.xticks(x+5/2*width, tracks)

    ax.bar_label(q1, padding=3)
    ax.bar_label(q2, padding=3)
    ax.bar_label(q3, padding=3)
    ax.bar_label(q4, padding=3)
    ax.bar_label(q5, padding=3)

    plt.title('Top songs in different services')
    plt.legend()
    plt.savefig('Top songs in different services.svg')
    plt.show()

    # print(len(common_top))


# tracks_durations(songs)
top_artists(10)
# common_top(songs)