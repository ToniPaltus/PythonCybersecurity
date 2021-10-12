from parsers.apple import get_apple_chart
from parsers.youtube import get_youtube_chart
from parsers.spotify import get_spotify_chart
from parsers.yandex import get_yandex_chart
from parsers.deezer import get_deezer_chart
from analitics.analis_1 import get_songs_top, get_artists_top, get_durations_sort, get_streams_sort


import json


def main():
    apple = get_apple_chart()
    youtube = get_youtube_chart()
    spotify = get_spotify_chart()
    yandex = get_yandex_chart()
    deezer = get_deezer_chart()
    common_data = apple+youtube+spotify+yandex+deezer
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(common_data, file)
    # exit()
    # with open('data.json', 'r') as f:
    #     common_data = json.load(f)
    # print(len(apple), apple[3])
    # print(len(youtube), youtube[4])
    # print(len(spotify), spotify[2])
    print(len(common_data))
    top = get_songs_top(common_data)
    # print(top[:10])
    art_top = get_artists_top(common_data)
    # print(art_top[:10])

    # # for i, song in enumerate(top, 1):
    # #     print(i, song)
    # #
    # with open('ready_to_django.json', 'w') as file:
    #     json.dump(top, file)
    # print(top)
    duration = get_durations_sort(common_data)
    # print(duration[-10:])

    streams = get_streams_sort(common_data)
    # print(streams[-10:])
    # print(common_data)
    # get_artists_top(common_data)


if __name__ == '__main__':
    main()
