from parsers.apple import get_apple_chart
from parsers.youtube import get_youtube_chart
from parsers.spotify import get_spotify_chart
from analitics.analis_1 import get_songs_top, get_artists_top


import json


def main():
    # apple = get_apple_chart()
    # youtube = get_youtube_chart()
    # spotify = get_spotify_chart()
    # common_data = apple+youtube+spotify
    # with open('data.json', 'w') as file:
    #     json.dump(common_data, file)
    # exit()
    with open('data.json', 'r') as f:
        common_data = json.load(f)
    # print(len(apple), apple[3])
    # print(len(youtube), youtube[4])
    # print(len(spotify), spotify[2])
    # top = get_songs_top(common_data)
    # print(top)
    # # for i, song in enumerate(top, 1):
    # #     print(i, song)
    # #
    # with open('ready_to_django.json', 'w') as file:
    #     json.dump(top, file)
    # print(top)
    # get_durations_top(common_data)
    # print(common_data)
    # get_artists_top(common_data)


if __name__ == '__main__':
    main()
