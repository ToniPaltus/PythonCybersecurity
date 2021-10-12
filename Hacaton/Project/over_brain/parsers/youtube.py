from bs4 import BeautifulSoup as BS
from html_loader import load_html


def get_youtube_chart():
    youtube = list()
    url = 'https://music.youtube.com/playlist?list=PL4fGSI1pDJn5kI81J1fYWK5eZRl1zJ5kM'

    response = load_html(url, length=3_700_000, timeout=20)
    soup = BS(response, 'lxml')
    songs_list = soup.find('div', class_='style-scope ytmusic-playlist-shelf-renderer')
    songs = songs_list.find_all('ytmusic-responsive-list-item-renderer',
                                class_='style-scope ytmusic-playlist-shelf-renderer')
    for song in songs:
        rank = song.find('yt-formatted-string',
                         class_='custom-index style-scope ytmusic-custom-index-column-renderer').text
        name = song.find('a', class_='yt-simple-endpoint style-scope yt-formatted-string').text
        artists_list = song.find('div',
                                 class_='secondary-flex-columns style-scope ytmusic-responsive-list-item-renderer')
        artists = [artist.text for artist in
                   artists_list.find_all('a', class_='yt-simple-endpoint style-scope yt-formatted-string')]
        duration = song.find('yt-formatted-string',
                             class_='fixed-column MUSIC_RESPONSIVE_LIST_ITEM_COLUMN_DISPLAY_PRIORITY_HIGH style-scope ytmusic-responsive-list-item-renderer').text
        song_dict = {
            'service': 'youtube',
            'rank': rank,
            'name': name,
            'artists': artists,
            'duration': duration,
            'album': None,
            'streams': None, }
        youtube.append(song_dict)
    return youtube
